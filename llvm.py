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

    def toLLVM(self, filename):
        self.symbolTable = symbolTable()
        open(filename, "w+")
        with open(filename, 'w') as file:
            file.write(self.createLLVM(self.ast.root))
        file.close()

    def createLLVM(self, currentNode):
        code = ""
        if currentNode.value == "DEC":
            code += self.translateDeclaration(currentNode)
        elif currentNode.value == "DEF":
            code += self.translateDefinition(currentNode)
        elif currentNode.value == "ASSIGN":
            code += self.translateAssignment(currentNode)
        for child in currentNode.children:
            code += self.createLLVM(child)
        return code

    def translateDeclaration(self, node):
        #----
        _type, name = self.getTypeAndName(node)
        code = "%" + str(self.counter) + " = alloca " + self.typeDict[_type][0] + ", align " + str(self.typeDict[_type][1]) + "\n"
        self.symbolTable.table.append(symbolTableElement(name, _type, self.counter))
        self.counter += 1
        return code
        
    def translateDefinition(self, node):
        code = self.translateDeclaration(node)

        _type, name = self.getTypeAndName(node)
        exp = node.children[-1]
        tableElement = self.symbolTable.findElement(name)

        if _type == 'char':
            character  = exp.children[0].children[0].value[1]
            code += "store i8 " + str(ord(character)) + ", i8* %" + str(tableElement.variableNumber) + ", align 1\n" 
        
        elif _type == "int":
            usedVariables = self.getAllVariables(exp)
            if not usedVariables:
                code += "store i32 " + str(int(float(exp.children[0].children[0].children[0].value))) + ", i32* %" + str(tableElement.variableNumber) + ", align 4\n"
            else:
                #meer dan een store
                pass
        else:
            usedVariables = self.getAllVariables(exp)
            if not usedVariables:
                code += "store float " + str(float(exp.children[0].children[0].children[0].value)) + ", float* %" + str(tableElement.variableNumber) + ", align 4\n"
            else:
                #meer dan een store
                pass

        return code

    def translateAssignment(self, node):
        code = ""
        name = self.getTypeAndName(node)[1]
        tableElement = self.symbolTable.findElement(name)
        exp = node.children[-1]

        if tableElement.type == 'char':
            character  = exp.children[0].children[0].value[1]
            code += "store i8 " + str(ord(character)) + ", i8* %" + name + ", align 1\n" 

        elif tableElement.type == 'int':
            usedVariables = self.getAllVariables(exp)
            if not usedVariables:
                code += "store i32 " + str(int(float(exp.children[0].children[0].children[0].value))) + ", i32* %" + name + ", align 4\n"
            else:
                pass
        elif tableElement.type == 'float':
            usedVariables = self.getAllVariables(exp)
            if not usedVariables:
                code += "store float " + str(float(exp.children[0].children[0].children[0].value)) + ", float* %" + name + ", align 4\n"
            else:
                pass
        return code


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