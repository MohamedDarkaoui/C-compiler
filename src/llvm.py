from symbolTable import *
from src.Nodes import *

strCode = "@.strs = private unnamed_addr constant [3 x i8] c\"%s\\00\", align 1\n"
strCode += "@.stri = private unnamed_addr constant [3 x i8] c\"%i\\00\", align 1\n"
strCode += "@.strd = private unnamed_addr constant [3 x i8] c\"%d\\00\", align 1\n"
strCode += "@.strf = private unnamed_addr constant [3 x i8] c\"%f\\00\", align 1\n"
strCode += "@.strc = private unnamed_addr constant [3 x i8] c\"%c\\00\", align 1\n"
strCode += "declare i32 @printf(i8*, ...) #1\n"

class LLVM():
    def __init__(self, AST):
        self.root = AST.root
        self.strCode = ''
        self.code = ''
        self.currentScope = None
        self.stringCounter = 1
        self.counter = 1
        self.labelCounter = 0
        self.typeDict = { 
            'int':('i32',4),
            'float':('float',4),
            'char':('i8',1),
            'void':('void',1)
        }

    def toLLVM(self, filename):
        open(filename, "w+")
        root = self.root
        with open(filename, 'w') as file:
            self.createLLVM(self.root)
            file.write(self.strCode + self.code)
        file.close()

        self.code = ''
        self.strCode = ''
        self.counter = 1
        self.labelCounter = 0
        self.currentScope = None
        self.root = root

    def createLLVM(self, currentNode, endNumber=None, conditionNumber=None):
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
            self.translateSelection(currentNode, endNumber, conditionNumber)
        elif isinstance(currentNode, WhileNode):
            self.translateWhile(currentNode)
        elif isinstance(currentNode, ForNode):
            self.currentScope = for_scope(self.currentScope)
            oldScope = self.currentScope
            self.translateFor(currentNode)
        elif isinstance(currentNode, FuncDefNode):
            returnType = currentNode.type.value
            name = currentNode.name.value
            arguments = []
            for argument in currentNode.arguments.children:
                arguments.append(variable(node=argument.var, type=argument.type.value, init=True, const=False))

            newFunction = Function(name = name, returnType = returnType, arguments = arguments, init=True)
            self.currentScope.addElement(newFunction)
            self.currentScope = func_scope(self.currentScope, arguments, returnType)
            oldScope = self.currentScope
            self.translateFuncDef(currentNode, endNumber, conditionNumber)
        elif isinstance(currentNode, ReturnNode):
            self.translateReturn(currentNode)
        elif isinstance(currentNode, BreakNode):
            self.addBranch(endNumber)
        elif isinstance(currentNode, ContinueNode):
            self.addBranch(conditionNumber)
        elif isinstance(currentNode, FuncCallNode):
            self.translateFuncCall(currentNode)
        elif isinstance(currentNode, PrintNode):
            self.translatePrint(currentNode)
        elif currentNode.value == '#include <stdio.h>':
            if len(self.strCode) == 0:
                self.strCode = strCode

        else:
            for child in currentNode.children:
                self.createLLVM(child, endNumber, conditionNumber)
                if oldScope is not None:
                    self.currentScope = oldScope
    
    def translateDeclaration(self, node):
        name, type = (node.var.value, node.type.value)

        if isinstance(self.currentScope, global_scope):
            if not node.var.isArray:
                self.code += '@' + name + ' = global ' + self.typeDict[type][0] + ' undef, align ' + str(self.typeDict[type][1]) + '\n'
                newVariable = variable(node.var, type, True, False, ('@' + name, type))
                self.currentScope.addElement(newVariable)
            else:
                self.code += '@' + name + ' = global [' + str(node.var.size) + ' x ' + self.typeDict[type][0] + '] zeroinitializer, align 16\n'
                newVariable = variable(node.var, type, True, False, ('@' + name, type))
                self.currentScope.addElement(newVariable)

        else:
            if not node.var.isArray:
                self.code += '%.' + str(self.counter) + ' = alloca ' + self.typeDict[type][0] + ', align ' + str(self.typeDict[type][1]) + '\n'
                newVariable = variable(node.var, type, True, False, ('%.' + str(self.counter), type))
                self.currentScope.addElement(newVariable)
                self.counter += 1
            else:
                self.code += '%.' + str(self.counter) + ' = alloca [' + str(node.var.size) + ' x ' + self.typeDict[type][0] + '], align 16\n'
                newVariable = newVariable = variable(node.var, type, True, False, ('%.' + str(self.counter), type))
                self.currentScope.addElement(newVariable)
                self.counter += 1
       
    def translateDefinition(self, node):
        self.translateDeclaration(node)
        self.translateAssignment(node)
        
    def translateAssignment(self, node):
        element = self.currentScope.getElement(node.var.value, 'variable')

        if not element.isArray:
            resultReg = self.getRegFromRHS(node.children[-1])
            if resultReg[1] != element.type:
                if not resultReg[0][0] in ['%', '@']:
                    if element.type == 'float':
                        resultReg = (str(float(int(resultReg[0]))), 'float')
                    elif element.type == 'int':
                        resultReg = (str(int(float(resultReg[0]))), 'int')
                else:    
                    newReg = '%.' + str(self.counter)
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
        else:
            if node.children[-1].value == 'ARRAY_INIT':
                for index, rhs in enumerate(node.children[-1].children):
                    resultReg = self.getRegFromRHS(rhs)
                    if resultReg[1] != element.type:
                        resultReg = self.convertReg(resultReg[0], resultReg[1], element.type)

                    ptr = '%.' + str(self.getNewCounter())
                    self.code += ptr + ' = getelementptr inbounds [' + str(element.size) + ' x ' + str(self.typeDict[element.type][0]) + '], '
                    self.code += '[' + str(element.size) + ' x ' + str(self.typeDict[element.type][0]) + ']* ' + element.register[0] + ', i64 0, i64 ' + str(index)+ '\n'

                    self.code += 'store ' + self.typeDict[element.type][0] + ' ' + resultReg[0] + ', ' + self.typeDict[element.type][0] + '* ' + ptr + ', align '
                    self.code += str(self.typeDict[element.type][1]) + '\n'

            else:
                resultReg = self.getRegFromRHS(node.children[-1])
                if resultReg[1] != element.type:
                    resultReg = self.convertReg(resultReg[0], resultReg[1], element.type)

                ptr = '%.' + str(self.getNewCounter())
                self.code += ptr + ' = getelementptr inbounds [' + str(element.size) + ' x ' + str(self.typeDict[element.type][0]) + '], '
                self.code += '[' + str(element.size) + ' x ' + str(self.typeDict[element.type][0]) + ']* ' + element.register[0] + ', i64 0, i64 ' + str(node.var.size)+ '\n'
                self.code += 'store ' + self.typeDict[element.type][0] + ' ' + resultReg[0] + ', ' + self.typeDict[element.type][0] + '* ' + ptr + ', align '
                self.code += str(self.typeDict[element.type][1]) + '\n'

    def getRegFromRHS(self, node):
        operators = ['+', '-', '*', '/', '%']

        if isinstance(node, ConstNode):
            if node.type == 'char':
                return (str(ord(node.value[1])), node.type)
            return (node.value, node.type)
        
        elif isinstance(node, VarNode):
            element = self.currentScope.getElement(node.value, 'variable')
            if not element.isArray:
                newReg = '%.' + str(self.getNewCounter())
                self.code += newReg + ' = load ' + self.typeDict[element.register[1]][0] + ', ' + self.typeDict[element.register[1]][0]
                self.code += '* ' + element.register[0] + ', align ' + str(self.typeDict[element.register[1]][1]) + '\n'
                    
                return (newReg, element.register[1])

            else:
                ptr = '%.' + str(self.getNewCounter())
                self.code += ptr + ' = getelementptr inbounds [' + str(element.size) + ' x ' + str(self.typeDict[element.type][0]) + '], '
                self.code += '[' + str(element.size) + ' x ' + str(self.typeDict[element.type][0]) + ']* ' + element.register[0] + ', i64 0, i64 ' + str(node.size)+ '\n'
                newReg = '%.' + str(self.getNewCounter())

                self.code += newReg + ' = load ' + self.typeDict[element.register[1]][0] + ', ' + self.typeDict[element.register[1]][0]
                self.code += '* ' + ptr + ', align ' + str(self.typeDict[element.register[1]][1]) + '\n'
                return (newReg, element.register[1])


        elif isinstance(node, FuncCallNode):
            return self.translateFuncCall(node)

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
                        temp = '%.' + str(self.counter)
                        self.counter += 1
                        self.code += temp + ' = sitofp i32 ' + leftOp[0] + ' to float\n'
                        leftOp = (temp, 'float')
                        leftOpType = 'float'
                else:
                    if not isRightOpVar:
                        rightOp = (float(rightOp[0]), 'float')
                        rightOpType = 'float'
                    else:
                        temp = '%.' + str(self.counter)
                        self.counter += 1
                        self.code += temp + ' = sitofp i32 ' + rightOp[0] + ' to float\n'
                        rightOp = (temp, 'float')
                        rightOpType = 'float'


            resultReg = ('%.' + str(self.counter), 'int')
            if leftOpType == 'float':
                resultReg = ('%.' + str(self.counter), 'float')
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

    def translateSelection(self, node, endNumber, conditionNumber):
        ifLabel = {
            'labelTrue': self.getNewLabelCounter(),
            'labelFalse': None,
            'labelEnd' : None
        }

        elIfLabels = []
        for elIf in node.elseIfStatements:
            elIfLabels.append({
                                'labelCondition': self.getNewLabelCounter(),
                                'labelTrue': self.getNewLabelCounter(),
                                'labelFalse': None,
                                'labelEnd' : None
                            })

        elseLabel = None
        if node.elseStatement is not None:
            elseLabel = {
            'labelTrue': self.getNewLabelCounter(),
            'labelFalse': None,
            'labelEnd' : None
        }

        endLabel = self.getNewLabelCounter()

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

        self.translateIf(node.ifStatement, ifLabel, endNumber, conditionNumber)
        for i in range(len(elIfLabels)):
            self.translateElseIf(node.elseIfStatements[i], elIfLabels[i], endNumber, conditionNumber)
        if elseLabel:
            self.translateElse(node.elseStatement, elseLabel, endNumber, conditionNumber)
        
        self.code += '\nlabel' + str(endLabel) + ':\n'

    def translateIf(self, node, labels, endNumber, conditionNumber):
        #create register with comparison result
        comparisonNode = node.condition.children[0]
        comparisonResult = self.getComparisonResult(comparisonNode)

        #br to labels['true'] if condition is true else br to labels['false']
        self.code += 'br i1 ' + comparisonResult +', label %' + 'label' + str(labels['labelTrue']) + ', label %' + 'label' + str(labels['labelFalse']) + '\n'

        #create label['true']
        self.code += '\nlabel' + str(labels['labelTrue']) + ':\n'
        #generate code inside the ifscope
        self.createLLVM(node.block, endNumber, conditionNumber)
        #br to labels['end']
        self.code += 'br label %' + 'label' + str(labels['labelEnd']) + '\n'

    def translateElseIf(self, node, labels, endNumber, conditionNumber):
        #create label where the else if condition is being evaluated
        self.code += '\nlabel' + str(labels['labelCondition']) + ':\n'

        #create register with comparison result
        comparisonNode = node.condition.children[0]
        comparisonResult = self.getComparisonResult(comparisonNode)

        #br to labels['true'] if condition is true else br to labels['false']
        self.code += 'br i1 ' + comparisonResult +', label %' + 'label' + str(labels['labelTrue']) + ', label %' + 'label' + str(labels['labelFalse']) + '\n'

        #create label['true']
        self.code += '\nlabel' + str(labels['labelTrue']) + ':\n'
        #generate code inside the ifscope
        self.createLLVM(node.block, endNumber, conditionNumber)
        #br to labels['end']
        self.code += 'br label %' + 'label' + str(labels['labelEnd']) + '\n'

    def translateElse(self, node, labels, endNumber, conditionNumber):
        #create label['true']
        self.code += '\nlabel' + str(labels['labelTrue']) + ':\n'
        #generate code inside the ifscope
        self.createLLVM(node.block, endNumber, conditionNumber)
        #br to labels['end']
        self.code += 'br label %' + 'label' + str(labels['labelEnd']) + '\n'
               
    def getNewCounter(self):
        self.counter += 1
        return self.counter-1

    def getNewLabelCounter(self):
        self.labelCounter += 1
        return self.labelCounter-1
    
    def getNewStringCounter(self):
        self.stringCounter += 1
        return self.stringCounter-1

    def getComparisonResult(self, comparisonNode):
        
        leftOpReg = self.getRegFromRHS(comparisonNode.leftOp)
        rightOpReg = self.getRegFromRHS(comparisonNode.rightOp)
        
        if leftOpReg[1] != rightOpReg[1]:
            if leftOpReg[1] == 'int':
                if leftOpReg[0][0] not in ['%', '@']:
                    leftOpReg = (float(leftOp[0]), 'float')
                else:
                    temp = '%.' + str(self.getNewCounter())
                    self.code += temp + ' = sitofp i32 ' + leftOpReg[0] + ' to float\n'
                    leftOpReg = (temp, 'float')

            elif rightOpReg[1] == 'int':
                if rightOpReg[0][0] not in ['%', '@']:
                    rightOpReg = (float(rightOpReg[0]), 'float')
                else:
                    temp = '%.' + str(self.getNewCounter())
                    self.code += temp + ' = sitofp i32 ' + rightOpReg[0] + ' to float\n'
                    rightOpReg = (temp, 'float')
        
        if leftOpReg[1] == 'char':
            if leftOpReg[0][0] in ['%', '@']:
                temp = '%.' + str(self.getNewCounter())
                self.code += temp + ' = sext i8 ' + leftOpReg[0] + ' to i32\n'
                leftOpReg = (temp, 'int')
            else:
                leftOpReg = (leftOpReg[0], 'int')

        if rightOpReg[1] == 'char':
            if rightOpReg[0][0] in ['%', '@']:
                temp = '%.' + str(self.getNewCounter())
                self.code += temp + ' = sext i8 ' + rightOpReg[0] + ' to i32\n'
                rightOpReg = (temp, 'int')
            else:
                rightOpReg = (rightOpReg[0], 'int')


        type = leftOpReg[1]
        conditionResult = '%.' + str(self.getNewCounter())
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

    def translateWhile(self, node, increment = None):
        conditionLabel = self.getNewLabelCounter()
        trueLabel = self.getNewLabelCounter()
        endLabel = self.getNewLabelCounter()

        #br to condition label
        self.code += 'br label %' + 'label' + str(conditionLabel) + '\n'

        #create condition label
        self.code += '\nlabel' + str(conditionLabel) + ':\n'
        #get condition result
        comparisonNode = node.condition.children[0]
        comparisonResult = self.getComparisonResult(comparisonNode)
        
        #br to true label else to the end
        self.code += 'br i1 ' + comparisonResult +', label %' + 'label' + str(trueLabel) + ', label %' + 'label' + str(endLabel) + '\n'

        #create while label
        self.code += '\nlabel' + str(trueLabel) + ':\n'
        #generate while_scope code inside while label
        self.createLLVM(node.block, endLabel, conditionLabel)
        #add incrementor if its a for loop
        if increment:
            self.createLLVM(increment, endLabel, conditionLabel)
        #at the end set a branch to the condition
        self.code += 'br label %' + 'label' + str(conditionLabel) + '\n'

        #create an end label
        self.code += '\nlabel' + str(endLabel) + ':\n'

    def translateFor(self, node):
        self.createLLVM(node.initiator)
        self.translateWhile(node, node.increment)

    def translateFuncDef(self, node, endNumber, conditionNumber):
        element = self.currentScope.getElement(node.name.value, 'function')
        arguments = element.arguments
        parametersTypes = ''
        for argument in arguments:
            parametersTypes += self.typeDict[argument.type][0] + ', '
        #remove last comma
        if len(parametersTypes) > 0:
            parametersTypes = parametersTypes[:-2]

        #create function
        self.code += '\ndefine ' + self.typeDict[element.returnType][0] + ' @' + element.name + '(' + parametersTypes + ') #0 {\n'
        #add parameters to the new current scope
        for i in range(len(arguments)):
            newArgumentRegister = '%.' + str(self.getNewCounter())
            self.code += newArgumentRegister + ' = alloca ' + self.typeDict[arguments[i].type][0] + ', align ' + str(self.typeDict[arguments[i].type][1]) + '\n'
            self.code += 'store ' + self.typeDict[arguments[i].type][0] + ' %' + str(i) + ', ' + self.typeDict[arguments[i].type][0] + '* ' + newArgumentRegister
            self.code += ', align ' + str(self.typeDict[arguments[i].type][1]) + '\n'
            arguments[i].register = (newArgumentRegister, arguments[i].type)

        #generate code inside
        self.createLLVM(node.body, endNumber, conditionNumber)
        
        if element.returnType == 'void':
            self.code += 'ret void'
        elif element.returnType == 'int':
            self.code += 'ret i32 0'
        elif element.returnType == 'float':
            self.code += 'ret float 0'
        elif element.returnType == 'char':
            self.code += 'ret i8 0'
        #close function
        self.code += '}\n'

    def translateReturn(self, node):

        if node.returnExp:
            returnRegister = self.getRegFromRHS(node.returnExp)
            #get function scope 
            functionScope = self.currentScope
            while not isinstance(functionScope, func_scope):
                functionScope = functionScope.parentScope

    

            if functionScope.returnType != returnRegister[1]:
                #2 CASES
                ##RETURN REGISTER IS A CONSTANT -> CONVERTION INT->FLOAT OR FLOAT->INT
                if returnRegister[0][0] not in ['%', '@']:
                    if functionScope.returnType  == 'float':
                        returnRegister = (str(float(int(returnRegister[0]))), 'float')
                    elif functionScope.returnType == 'int':
                        returnRegister = (str(int(float(returnRegister[0]))), 'int')
                ##RETURN REGISTER IS A VARIABLE
                else:
                    newReg = '%.' + str(self.counter)
                    self.counter += 1
                    if returnRegister[1] == 'int':
                        #set to float
                        self.code += newReg + ' = sitofp i32 ' + returnRegister[0] + ' to float\n'
                        returnRegister = (newReg, 'float')
                    elif returnRegister[1] == 'float':
                        #set to int
                        self.code += newReg + ' = fptosi float ' + returnRegister[0] + ' to i32\n'
                        returnRegister = (newReg, 'int')

            self.code += 'ret ' + self.typeDict[returnRegister[1]][0] + ' ' + returnRegister[0] + '\n'

        else:
            self.code += 'ret void\n'

    def addBranch(self, labelNumber):
        self.code += 'br label %' + 'label' + str(labelNumber) + '\n'

    def translateFuncCall(self, node):
        result = '%.' + str(self.getNewCounter())
        element = self.currentScope.getElement(node.name.value, 'function')
        parameters = []
        for index, parameter in enumerate(node.parameters.children):
            paramReg = self.getRegFromRHS(parameter)
            if element.arguments[index].type != paramReg[1]:
                paramReg = self.convertReg(paramReg[0], paramReg[1], element.arguments[index].type)

            parameters.append(paramReg)

        parametersText = '('
        for parameter in parameters:
            parametersText += self.typeDict[parameter[1]][0] + ' ' + parameter[0] + ', '

        if len(parametersText) > 1:
            parametersText = parametersText[:-2] 
        
        parametersText += ')'
        
        if element.returnType == 'void':
            self.code += 'call ' + self.typeDict[element.returnType][0] + ' @' + element.name + parametersText + '\n'
        else:
            self.code += result + ' = call ' + self.typeDict[element.returnType][0] + ' @' + element.name + parametersText + '\n'

        return (result, element.returnType)
    
    def convertReg(self, regName, fromType, toType):
        returnRegister = (regName, toType)
        #2 CASES
        ##regName is a number
        if regName[0] not in ['%', '@']:
            if toType == 'float':
                returnRegister = (str(float(int(regName))), 'float')
            elif toType == 'int':
                returnRegister = (str(int(float(regName))), 'int')

        ##RETURN REGISTER IS A VARIABLE
        else:
            newReg = '%.' + str(self.getNewCounter())

            if fromType == 'int':
                #set to float
                self.code += newReg + ' = sitofp i32 ' + regName + ' to float\n'
                returnRegister = (newReg, 'float')

            elif fromType == 'float':
                #set to int
                self.code += newReg + ' = fptosi float ' + regName + ' to i32\n'
                returnRegister = (newReg, 'int')

        return returnRegister

    def translatePrint(self, node):
        if node.code == '"%s"':
            newReg = '%.' + str(self.getNewCounter())
            number = str(self.getNewStringCounter())
            string = node.exp.value.replace('"', "")
            size = str(len(string) + 1)
            self.strCode += '@.str.' + number + ' = private unnamed_addr constant [' + size + ' x i8] c"' + string + '\\00", align 1\n'
            self.code += newReg + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.strs, i32 0, i32 0), "
            self.code += "i8* getelementptr inbounds ([" + size + " x i8], [" + size +" x i8]* @.str." + number + ", i32 0, i32 0))\n"

        elif node.code == '"%i"':
            newReg = '%.' + str(self.getNewCounter())
            resultReg = self.getRegFromRHS(node.children[-1])

            if resultReg[1] != 'int':
                resultReg = self.convertReg(resultReg[0], resultReg[1], 'int')
            self.code += newReg + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.stri, i32 0, i32 0), i32 " + resultReg[0] + ")\n"
        
        elif node.code == '"%d"':
            newReg = '%.' + str(self.getNewCounter())

            resultReg = self.getRegFromRHS(node.children[-1])
            if resultReg[1] != 'int':
                resultReg = self.convertReg(resultReg[0], resultReg[1], 'int')
            self.code += newReg + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.strd, i32 0, i32 0), i32 " + resultReg[0] + ")\n"
        
        elif node.code == '"%f"':
            newReg = '%.' + str(self.getNewCounter())
            resultReg = self.getRegFromRHS(node.children[-1])
            if resultReg[1] != 'float':
                resultReg = self.convertReg(resultReg[0], resultReg[1], 'float')
            if resultReg[0][0] in ['%', '@']:
                temp = '%.' + str(self.getNewCounter())
                self.code += temp + ' = fpext float ' + resultReg[0] + " to double\n"
                resultReg = (temp, 'float')

            self.code += newReg + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.strf, i32 0, i32 0), double " + resultReg[0] + ")\n"
        
        elif node.code == '"%c"':
            newReg = '%.' + str(self.getNewCounter())
            resultReg = self.getRegFromRHS(node.children[-1])
            
            self.code += newReg + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.strc, i32 0, i32 0), i8 " + resultReg[0] + ")\n"

