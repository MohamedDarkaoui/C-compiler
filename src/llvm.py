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
        elif isinstance(currentNode, SelectNode):
            self.translateSelection(currentNode)
            return

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
                return (str(ord(node.value[1])), node.type)
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
                        leftOp = (float(leftOp[0]), 'float')
                        leftOpType = 'float'
                    else:
                        temp = '%' + str(self.counter)
                        self.counter += 1
                        self.code += temp + ' = sitofp i32 ' + leftOp[0] + ' to float\n'
                        leftOp = (temp, 'float')
                        leftOpType = 'float'
                else:
                    if not isRightOpVar:
                        rightOp = (float(rightOp[0]), 'float')
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


    def translateSelection(self, node):
        ifLabel = {
            'labelTrue': self.getNewCounter(),
            'labelFalse': None,
            'labelEnd' : None
        }

        elIfLabels = []
        for elIf in node.elseIfStatements:
            elIfLabels.append({
                                'labelCondition': self.getNewCounter(),
                                'labelTrue': self.getNewCounter(),
                                'labelFalse': None,
                                'labelEnd' : None
                            })

        elseLabel = None
        if node.elseStatement is not None:
            elseLabel = {
            'labelTrue': self.getNewCounter(),
            'labelFalse': None,
            'labelEnd' : None
        }

        endLabel = self.getNewCounter()

        #CHECK IF LABEL:
        if elIfLabels:
            ifLabel['labelFalse'] = elIfLabels[0]['labelCondition']
        elif elseLabel:
            ifLabel['labelFalse'] = elseLabel['labelTrue']
        else:
            ifLabel['labelFalse'] = endLabel
        ifLabel['labelEnd'] = endLabel

        #CHECK ELIF LABELS:
        for i in range(len(elIfLabels)):
            if i == len(elIfLabels) - 1:
                if elseLabel:
                    elIfLabels[i]['labelFalse'] = elseLabel['labelTrue']
                else:
                    elIfLabels[i]['labelFalse'] = endLabel
            else:
                elIfLabels[i]['labelFalse'] = elIfLabels[i+1]['labelCondition']

            elIfLabels[i]['labelEnd'] = endLabel
        #CHECK ELSE LABEL:
        if elseLabel:
            elseLabel['labelEnd'] = endLabel

        self.translateIf(node.ifStatement, ifLabel)
        for i in range(len(elIfLabels)):
            self.translateElseIf(node.elseIfStatements[i], elIfLabels[i])
        if elseLabel:
            self.translateElse(node.elseStatement, elseLabel)
        
        self.code += '\n; <label>:' + str(endLabel) + ':\n'



    def translateIf(self, node, labels):
        #create register with comparison result
        comparisonNode = node.condition.children[0]
        comparisonResult = self.getComparisonResult(comparisonNode)

        #br to labels['true'] if condition is true else br to labels['false']
        self.code += 'br i1 ' + comparisonResult +', label %' + str(labels['labelTrue']) + ', label %' + str(labels['labelFalse']) + '\n'

        #create label['true']
        self.code += '\n; <label>:' + str(labels['labelTrue']) + ':\n'
        #generate code inside the ifscope
        self.createLLVM(node.block)
        #br to labels['end']
        self.code += 'br label %' + str(labels['labelEnd']) + '\n'

    def translateElseIf(self, node, labels):
        #create label where the else if condition is being evaluated
        self.code += '\n; <label>:' + str(labels['labelCondition']) + ':\n'

        #create register with comparison result
        comparisonNode = node.condition.children[0]
        comparisonResult = self.getComparisonResult(comparisonNode)

        #br to labels['true'] if condition is true else br to labels['false']
        self.code += 'br i1 ' + comparisonResult +', label %' + str(labels['labelTrue']) + ', label %' + str(labels['labelFalse']) + '\n'

        #create label['true']
        self.code += '\n; <label>:' + str(labels['labelTrue']) + ':\n'
        #generate code inside the ifscope
        self.createLLVM(node.block)
        #br to labels['end']
        self.code += 'br label %' + str(labels['labelEnd']) + '\n'

    def translateElse(self, node, labels):
        #create label['true']
        self.code += '\n; <label>:' + str(labels['labelTrue']) + ':\n'
        #generate code inside the ifscope
        self.createLLVM(node.block)
        #br to labels['end']
        self.code += 'br label %' + str(labels['labelEnd']) + '\n'
        
        

    def getNewCounter(self):
        self.counter += 1
        return self.counter-1



    def getComparisonResult(self, comparisonNode):
        
        leftOpReg = self.getRegFromRHS(comparisonNode.leftOp)
        rightOpReg = self.getRegFromRHS(comparisonNode.rightOp)
        
        if leftOpReg[1] != rightOpReg[1]:
            if leftOpReg[1] == 'int':
                if leftOpReg[0][0] not in ['%', '@']:
                    leftOpReg = (float(leftOp[0]), 'float')
                else:
                    temp = '%' + str(self.getNewCounter())
                    self.code += temp + ' = sitofp i32 ' + leftOpReg[0] + ' to float\n'
                    leftOpReg = (temp, 'float')

            elif rightOpReg[1] == 'int':
                if rightOpReg[0][0] not in ['%', '@']:
                    rightOpReg = (float(rightOpReg[0]), 'float')
                else:
                    temp = '%' + str(self.getNewCounter())
                    self.code += temp + ' = sitofp i32 ' + rightOpReg[0] + ' to float\n'
                    rightOpReg = (temp, 'float')
        
        if leftOpReg[1] == 'char':
            if leftOpReg[0][0] in ['%', '@']:
                temp = '%' + str(self.getNewCounter())
                self.code += temp + ' = sext i8 ' + leftOpReg[0] + ' to i32\n'
                leftOpReg = (temp, 'int')
            else:
                leftOpReg = (leftOpReg[0], 'int')

        if rightOpReg[1] == 'char':
            if rightOpReg[0][0] in ['%', '@']:
                temp = '%' + str(self.getNewCounter())
                self.code += temp + ' = sext i8 ' + rightOpReg[0] + ' to i32\n'
                rightOpReg = (temp, 'int')
            else:
                rightOpReg = (rightOpReg[0], 'int')


        type = leftOpReg[1]
        conditionResult = '%' + str(self.getNewCounter())
        #create comparison
        if isinstance(comparisonNode, EqNode):
            if type == 'int':
                self.code += conditionResult + ' = icmp eq i32 ' + str(leftOpReg[0]) + ', ' + str(rightOpReg[0]) + '\n'
            elif type == 'float':
                self.code += conditionResult + ' = fcmp oeq float ' + str(leftOpReg[0]) + ', ' + str(rightOpReg[0]) + '\n'
        elif isinstance(comparisonNode, NeqNode):
            if type == 'int':
                self.code += conditionResult + ' = icmp ne i32 ' + str(leftOpReg[0]) + ', ' + str(rightOpReg[0]) + '\n'
            elif type == 'float':
                self.code += conditionResult + ' = fcmp une float ' + str(leftOpReg[0]) + ', ' + str(rightOpReg[0]) + '\n'
        elif isinstance(comparisonNode, GtNode):
            if type == 'int':
                self.code += conditionResult + ' = icmp sgt i32 ' + str(leftOpReg[0]) + ', ' + str(rightOpReg[0]) + '\n'
            elif type == 'float':
                self.code += conditionResult + ' = fcmp ogt float ' + str(leftOpReg[0]) + ', ' + str(rightOpReg[0]) + '\n'
        elif isinstance(comparisonNode, GetNode):
            if type == 'int':
                self.code += conditionResult + ' = icmp sge i32 ' + str(leftOpReg[0]) + ', ' + str(rightOpReg[0]) + '\n'
            elif type == 'float':
                self.code += conditionResult + ' = fcmp oge float ' + str(leftOpReg[0]) + ', ' + str(rightOpReg[0]) + '\n'
        elif isinstance(comparisonNode, StNode):
            if type == 'int':
                self.code += conditionResult + ' = icmp slt i32 ' + str(leftOpReg[0]) + ', ' + str(rightOpReg[0]) + '\n'
            elif type == 'float':
                self.code += conditionResult + ' = fcmp olt float ' + str(leftOpReg[0]) + ', ' + str(rightOpReg[0]) + '\n'
        elif isinstance(comparisonNode, SetNode):
            if type == 'int':
                self.code += conditionResult + ' = icmp sle i32 ' + str(leftOpReg[0]) + ', ' + str(rightOpReg[0]) + '\n'
            elif type == 'float':
                self.code += conditionResult + ' = fcmp ole float ' + str(leftOpReg[0]) + ', ' + str(rightOpReg[0]) + '\n'
        
        return conditionResult
