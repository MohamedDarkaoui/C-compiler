from symbolTable import *
from src.Nodes import *

class LLVM():
    def __init__(self, AST):
        self.root = AST.root
        self.code = ''
        self.currentScope = None
        self.counter = 1
        self.typeDict = { 
            'int':('i32',4),
            'float':('float',4),
            'char':('i8',1)
        }

    def toLLVM(self, filename):
        open(filename, "w+")
        with open(filename, 'w') as file:
            self.createLLVM(self.root)
            file.write(self.code)
        file.close()
        self.code = ""



    
    def createLLVM(self, currentNode):
        oldScope = self.currentScope
        if isinstance(currentNode, ScopeNode):
            #CREATE GLOBAL SCOPE
            if currentNode.value == 'global_scope':
                self.currentScope = global_scope()
                oldScope = self.currentScope
            elif currentNode.value == 'unnamed_scope':
                self.currentScope = unnamed_scope(self.currentScope)
                oldScope = self.currentScope
            elif currentNode.value == 'if_scope':
                self.currentScope = if_scope(self.currentScope)
                oldScope = self.currentScope
            elif currentNode.value == 'elif_scope':
                self.currentScope = elif_scope(self.currentScope)
                oldScope = self.currentScope
            elif currentNode.value == 'else_scope':
                self.currentScope = else_scope(self.currentScope)
                oldScope = self.currentScope
            elif currentNode.value == 'while_scope':
                self.currentScope = while_scope(self.currentScope)
                oldScope = self.currentScope

        if isinstance(currentNode, DecNode):
            self.translateDeclaration(currentNode)
        elif isinstance(currentNode, DefNode):
            self.translateDefinition(currentNode)
        elif isinstance(currentNode, AssignNode):
            self.translateAssignment(currentNode)


        for child in currentNode.children:
            self.createLLVM(child)
            if oldScope is not None:
                self.currentScope = oldScope
    


    def translateDeclaration(self, node):
        name, type = (node.var.value, node.type.value)
        if isinstance(self.currentScope, global_scope):
            self.code += '@' + name + ' = global ' + self.typeDict[type][0] + ' undef, align ' + str(self.typeDict[type][1]) + '\n'
            newVariable = variable(node.var, type, True, False, ('@' + name, type))
            self.currentScope.addElement(newVariable)
        else:
            self.code += '%' + str(self.counter) + ' = alloca ' + self.typeDict[type][0] + ', align ' + str(self.typeDict[type][1]) + '\n'
            newVariable = variable(node.var, type, True, False, ('%' + str(self.counter), type))
            self.currentScope.addElement(newVariable)
            self.counter += 1

        

    def translateDefinition(self, node):
        self.translateDeclaration(node)
        self.translateAssignment(node)
        
    def translateAssignment(self, node):
        element = self.currentScope.getElement(node.var.value, 'variable')
        resultReg = self.getRegFromRHS(node.children[-1])
        if resultReg[1] != element.type:
            if not resultReg[0][0] in ['%', '@']:
                if element.type == 'float':
                    resultReg = (str(float(int(resultReg[0]))), 'float')
                elif element.type == 'int':
                    resultReg = (str(int(float(resultReg[0]))), 'int')
            else:    
                newReg = '%' + str(self.counter)
                self.counter += 1
                if resultReg[1] == 'int':
                    #set to float
                    self.code += newReg + ' = sitofp i32 ' + resultReg[0] + ' to float\n'
                    resultReg = (newReg, 'float')
                elif resultReg[1] == 'float':
                    #set to int
                    self.code += newReg + ' = fptosi float ' + resultReg[0] + ' to i32\n'
                    resultReg = (newReg, 'int')

        self.code += 'store ' + self.typeDict[element.type][0] + ' ' + resultReg[0] + ', ' + self.typeDict[element.type][0] 
        self.code += '* ' + element.register[0] + ', align ' + str(self.typeDict[element.type][1]) + '\n'



    def getRegFromRHS(self, node):
        operators = ['+', '-', '*', '/', '%']

        if isinstance(node, ConstNode):
            if node.type == 'char':
                return ord(node.value)
            return (node.value, node.type)
        
        elif isinstance(node, VarNode):
            element = self.currentScope.getElement(node.value, 'variable')
            return element.register
        
        elif node.value in operators:
            leftOp = self.getRegFromRHS(node.leftOp)
            rightOp = self.getRegFromRHS(node.rightOp)

            isLeftOpVar = leftOp[0][0] in ['%','@']
            isRightOpVar = rightOp[0][0] in ['%','@']
            leftOpType = None
            rightOpType = None

            if isinstance(leftOp, int):
                leftOpType = 'int'
            elif isinstance(leftOp, float):
                leftOpType = 'float'
            else:
                leftOpType = leftOp[1]

            if isinstance(rightOp, int):
                rightOpType = 'int'
            elif isinstance(rightOp, float):
                rightOpType = 'float'
            else:
                rightOpType = rightOp[1]


            if leftOpType != rightOpType:
                if leftOpType == 'int':
                    if not isLeftOpVar:
                        leftOp[0] = float(leftOp[0])
                        leftOp[1] = 'float'
                        leftOpType = 'float'
                    else:
                        temp = '%' + str(self.counter)
                        self.counter += 1
                        self.code += temp + ' = sitofp i32 ' + leftOp[0] + ' to float\n'
                        leftOp = (temp, 'float')
                        leftOpType = 'float'
                else:
                    if not isRightOpVar:
                        rightOp[0] = float(rightOp[0])
                        rightOp[1] = 'float'
                        rightOpType = 'float'
                    else:
                        temp = '%' + str(self.counter)
                        self.counter += 1
                        self.code += temp + ' = sitofp i32 ' + rightOp[0] + ' to float\n'
                        rightOp = (temp, 'float')
                        rightOpType = 'float'


            resultReg = ('%' + str(self.counter), 'int')
            if leftOpType == 'float':
                resultReg = ('%' + str(self.counter), 'float')
            self.counter += 1

            if isinstance(node, PlusNode):
                if leftOpType == 'float':
                    self.code += resultReg[0] + ' = fadd float ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                else:
                    self.code += resultReg[0] + ' = add nsw i32 ' + leftOp[0] + ', ' + rightOp[0] + '\n'
            elif isinstance(node, MinusNode):
                if leftOpType == 'float':
                    self.code += resultReg[0] + ' = fsub float ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                else:
                    self.code += resultReg[0] + ' = sub nsw i32 ' + leftOp[0] + ', ' + rightOp[0] + '\n'
            elif isinstance(node, MulNode):
                if leftOpType == 'float':
                    self.code += resultReg[0] + ' = fmul float ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                else:
                    self.code += resultReg[0] + ' = mul nsw i32 ' + leftOp[0] + ', ' + rightOp[0] + '\n'
            elif isinstance(node, DivNode):
                if leftOpType == 'float':
                    self.code += resultReg[0] + ' = fdiv float ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                else:
                    self.code += resultReg[0] + ' = sdiv i32 ' + leftOp[0] + ', ' + rightOp[0] + '\n'
            elif isinstance(node, ModNode):
                    self.code += resultReg[0] + ' = srem i32 ' + leftOp[0] + ', ' + rightOp[0] + '\n'

            return resultReg