from symbolTable import symbolTableElement, symbolTable
class LLVMGenerator:
    def __init__(self, ast):
        self.ast = ast
        self.typeDict = { 
            'int':('i32',4),
            'float':('float',4),
            'char':('i8',1)
        }
        self.symbolTable = None
        self.counter = 1
        self.code = ""

    def toLLVM(self, filename):
        self.symbolTable = symbolTable()
        open(filename, "w+")
        with open(filename, 'w') as file:
            self.createLLVM(self.ast.root)
            file.write(self.code)
        file.close()
        self.code = ""

    def createLLVM(self, currentNode):
        if currentNode.value == "DEC":
            self.translateDeclaration(currentNode)
        elif currentNode.value == "DEF":
            self.translateDefinition(currentNode)
        elif currentNode.value == "ASSIGN":
            self.translateAssignment(currentNode)
        for child in currentNode.children:
            self.createLLVM(child)
        

    def translateDeclaration(self, node):
        #----
        _type, name = self.getTypeAndName(node)
        self.code += "%" + str(self.counter) + " = alloca " + self.typeDict[_type][0] + ", align " + str(self.typeDict[_type][1]) + "\n"
        self.symbolTable.table.append(symbolTableElement(name, _type, self.counter))
        self.counter += 1
        
    def translateDefinition(self, node):
        self.translateDeclaration(node)

        _type, name = self.getTypeAndName(node)
        exp = node.children[-1]
        tableElement = self.symbolTable.findElement(name)

        if _type == 'char':
            character  = exp.children[0].children[0].value[1]
            self.code += "store i8 " + str(ord(character)) + ", i8* %" + str(tableElement.variableNumber) + ", align 1\n" 
        
        elif _type == "int":
            usedVariables = self.getAllVariables(exp)
            if not usedVariables:
                self.code += "store i32 " + str(int(float(exp.children[0].children[0].children[0].value))) + ", i32* %" + str(tableElement.variableNumber) + ", align 4\n"
            else:
                resultVar = self.operationRecursion(exp.children[0], "i32")
                self.code += "store i32 " + resultVar + ", i32* %" + str(tableElement.variableNumber) + ", align 4\n"
        else:
            usedVariables = self.getAllVariables(exp)
            if not usedVariables:
                self.code += "store float " + str(float(exp.children[0].children[0].children[0].value)) + ", float* %" + str(tableElement.variableNumber) + ", align 4\n"
            else:
                resultVar = self.operationRecursion(exp.children[0], "float")
                self.code += "store float " + resultVar + ", float* %" + str(tableElement.variableNumber) + ", align 4\n"

    def translateAssignment(self, node):
        name = self.getTypeAndName(node)[1]
        tableElement = self.symbolTable.findElement(name)
        exp = node.children[-1]

        if tableElement.type == 'char':
            character  = exp.children[0].children[0].value[1]
            self.code += "store i8 " + str(ord(character)) + ", i8* %" + name + ", align 1\n" 

        elif tableElement.type == 'int':
            usedVariables = self.getAllVariables(exp)
            if not usedVariables:
                self.code += "store i32 " + str(int(float(exp.children[0].children[0].children[0].value))) + ", i32* %" + name + ", align 4\n"
            else:
                resultVar = self.operationRecursion(exp.children[0], "i32")
                self.code += "store i32 " + resultVar + ", i32* %" + str(tableElement.variableNumber) + ", align 4\n"

        elif tableElement.type == 'float':
            usedVariables = self.getAllVariables(exp)
            if not usedVariables:
                self.code += "store float " + str(float(exp.children[0].children[0].children[0].value)) + ", float* %" + name + ", align 4\n"
            else:
                resultVar = self.operationRecursion(exp.children[0], "float")
                self.code += "store float " + resultVar + ", float* %" + str(tableElement.variableNumber) + ", align 4\n"


    def getTypeAndName(self, node):
        _type = ""
        name = ""
        for child in node.children:
            if child.value == 'TYPE':
                _type = child.children[0].value
            elif child.value == 'VAR':
                name = child.children[0].value
        return _type, name

    #FUNCTION THAT RETURNS ALL VARIABLES USED IN A SUBTREE
    def getAllVariables(self, currentNode):
        variables = []
        if currentNode.value == "VAR":
            variables.append(currentNode.children[0].value)
        else:
            for child in currentNode.children:
                variables += self.getAllVariables(child)
        return variables

    def operationRecursion(self, node, _type):
        operators = ['+','-','/','*','%']
        if node.value in operators:
            leftOperandi = self.operationRecursion(node.children[0], _type)
            rightOperandi = self.operationRecursion(node.children[1], _type)

            operator_dict = {'+' : 'add nsw', '-' : 'sub nsw', '*' : 'mul nsw', '/' : 'sdiv', '%' : 'srem'}
            operator = node.value

            newVariable = "%" + str(self.counter)
            self.counter+=1
            self.code += newVariable + " = " + operator_dict[operator]+ ' ' + _type + " " +leftOperandi + ", " + rightOperandi + "\n"

            return newVariable

        elif node.value == 'A_EXP':
            if node.children[0].value == "VAR":
                newVar = None
                tableElement = self.symbolTable.findElement(node.children[0].children[0].value)
                name = "%" + str(tableElement.variableNumber)
                if _type == 'i32' and tableElement.type == 'float':
                    tempVar = '%' + str(self.counter)
                    self.counter+=1
                    newVar = '%' + str(self.counter) 
                    self.counter += 1
                    self.code += tempVar + ' = load float, float* ' + name + ', align 4\n'
                    self.code += newVar + ' = fptosi float ' + tempVar + ' to i32\n'
                elif _type == 'float' and tableElement.type == 'int':
                    tempVar = '%' + str(self.counter)
                    self.counter+=1
                    newVar = '%' + str(self.counter) 
                    self.counter += 1
                    self.code += tempVar + ' = load i32, i32* ' + name + ', align 4\n'
                    self.code += newVar + ' = sitofp i32 ' + tempVar + ' to float\n'
                else:  
                    newVar = '%' + str(self.counter) 
                    self.code += newVar + ' = load ' + _type + ', ' + _type + '* ' + name + ', align 4\n'
                    self.counter += 1 
                return newVar
            else:
                if _type == "i32":
                    return str(int(float(node.children[0].children[0].value)))
                elif _type == "float":
                    return str(float(node.children[0].children[0].value))