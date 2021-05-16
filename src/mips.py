from src.Nodes import *
from mipsSymbolTable import *

class MIPS():
    def __init__(self, AST):
        self.root = AST.root
        self.code = ""
        self.data = ""
        self.globalVariables = ""
        self.floatCounter = 0
        self.labelCounter = 0
        self.stringCounter = 0
        self.currentScope = None
    
    def toMIPS(self, filename):
        open(filename, "w+")
        root = self.root
        with open(filename, 'w') as file:
            self.createMIPS(self.root)
            if self.data:
                self.data = '.data\n' + self.data + '.text\n\n\n'
            globalScope = self.currentScope
            while not isinstance(self.currentScope, global_scope):
                globalScope = self.currentScope.parentScope
            self.jumpMain = "\n\n\taddi $sp, $sp, " + str(-globalScope.offsetFree) + '\n'
            self.jumpMain += '\tj $funcmain\n\n'
            file.write(self.data + self.globalVariables + self.jumpMain + self.code)
        file.close()
        #RESET
        self.code = "\n\tj main\n\n"
        self.globalVariables = ""
        self.data = ""
        self.floatCounter = 0
        self.labelCounter = 0
        self.stringCounter = 0
        self.currentScope = None
        self.root = root

    def createMIPS(self, currentNode, endLabel=None, loopLabel=None, incrementor=None, ifLabels=None):
        oldScope = self.currentScope
        if isinstance(currentNode, ScopeNode):
            if currentNode.value == 'global_scope':
                self.currentScope = global_scope()
                oldScope = self.currentScope

            elif currentNode.value == 'unnamed_scope':
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += '\taddi $sp, $sp, ' + str(-self.currentScope.offsetFree) + '\n'
                else:
                    self.code += '\taddi $sp, $sp, ' + str(-self.currentScope.offsetFree) + '\n'
                self.currentScope = unnamed_scope(self.currentScope)
                oldScope = self.currentScope                

        if isinstance(currentNode, DecNode):
            """
            Save an specific place in memory for the variable
            """
            self.translateDeclaration(currentNode)

        elif isinstance(currentNode, DefNode):
            """
            Save an specific place in memory for the variable
            Assign it to the rvalue
            """
            self.translateDefinition(currentNode)
            
        elif isinstance(currentNode, AssignNode):
            """
            Assign to the rvalue
            """
            self.translateAssignment(currentNode)
        
        elif isinstance(currentNode, SelectNode):
            self.translateSelection(currentNode, endLabel, loopLabel, incrementor)

        elif isinstance(currentNode, IfNode):
            #create label
            if isinstance(self.currentScope, global_scope):
                self.globalVariables += '\n' + ifLabels['label'] + ':\n'
                self.globalVariables += '\taddi $sp, $sp, ' + str(-self.currentScope.offsetFree) + '\n'
            else:
                self.code += '\n' + ifLabels['label'] + ':\n'
                self.code += '\taddi $sp, $sp, ' + str(-self.currentScope.offsetFree) + '\n'
            self.currentScope = if_scope(self.currentScope)
            oldScope = self.currentScope
            self.translateIf(currentNode, ifLabels, endLabel, loopLabel, incrementor)
        
        elif isinstance(currentNode, ElseIfNode):
            #create label
            if isinstance(self.currentScope, global_scope):
                self.globalVariables += '\n' + ifLabels['label'] + ':\n'
                #self.globalVariables += '\taddi $sp, $sp, ' + str(-self.currentScope.offsetFree) + '\n'
            else:
                self.code += '\n' + ifLabels['label'] + ':\n'
                #self.code += '\taddi $sp, $sp, ' + str(-self.currentScope.offsetFree) + '\n'
            self.currentScope = elif_scope(self.currentScope)
            self.translateElseIf(currentNode, ifLabels, endLabel, loopLabel, incrementor)

        elif isinstance(currentNode, ElseNode):
            #create label
            if isinstance(self.currentScope, global_scope):
                self.globalVariables += '\n' + ifLabels['label'] + ':\n'
                #self.globalVariables += '\taddi $sp, $sp, ' + str(-self.currentScope.offsetFree) + '\n'
            else:
                self.code += '\n' + ifLabels['label'] + ':\n'
                #self.code += '\taddi $sp, $sp, ' + str(-self.currentScope.offsetFree) + '\n'
            self.currentScope = else_scope(self.currentScope)
            self.translateElse(currentNode, ifLabels, endLabel, loopLabel, incrementor)

        elif isinstance(currentNode, WhileNode):
            if isinstance(self.currentScope, global_scope):
                self.globalVariables += '\taddi $sp, $sp, ' + str(-self.currentScope.offsetFree) + '\n'
            else:
                self.code += '\taddi $sp, $sp, ' + str(-self.currentScope.offsetFree) + '\n'
            self.currentScope = while_scope(self.currentScope)
            oldScope = self.currentScope
            self.translateWhile(currentNode)
        
        elif isinstance(currentNode, ForNode):
            if isinstance(self.currentScope, global_scope):
                self.globalVariables += '\taddi $sp, $sp, ' + str(-self.currentScope.offsetFree) + '\n'
            else:
                self.code += '\taddi $sp, $sp, ' + str(-self.currentScope.offsetFree) + '\n'
            self.currentScope = for_scope(self.currentScope)
            oldScope = self.currentScope
            self.translateFor(currentNode)

        elif isinstance(currentNode, PrintNode):
            self.translatePrint(currentNode)

        elif isinstance(currentNode, BreakNode):
            self.addJump(endLabel)

        elif isinstance(currentNode, ContinueNode):
            if incrementor:
                self.createMIPS(incrementor, endLabel, loopLabel, incrementor)
            self.addJump(loopLabel)
        
        elif isinstance(currentNode, FuncDefNode):
            returnType = currentNode.type.value
            name = currentNode.name.value
            arguments = []
            offset = 0
            for argument in currentNode.arguments.children:
                arguments.append(variable(argument.var.value, argument.type.value, offset))
                offset+=4
            newFunction = function(name, arguments, returnType)
            self.currentScope.addElement(newFunction)
            self.currentScope = func_scope(self.currentScope, arguments, returnType, name == 'main')
            self.currentScope.offsetFree = offset
            oldScope = self.currentScope
            self.translateFuncDef(currentNode)

        elif isinstance(currentNode, FuncCallNode):
            self.translateFuncCall(currentNode, False)
        
        elif isinstance(currentNode, ReturnNode):
            self.translateReturn(currentNode)

        else:
            for child in currentNode.children:
                self.createMIPS(child, endLabel, loopLabel, incrementor)
                if oldScope is not None:
                    if self.currentScope != oldScope:
                        if not isinstance(self.currentScope, func_scope):
                            if isinstance(self.currentScope, global_scope):
                                self.globalVariables = '\taddi $sp, $sp, ' + str(oldScope.offsetFree) + '\n'
                            else:
                                self.code += '\taddi $sp, $sp, ' + str(oldScope.offsetFree) + '\n'
                    self.currentScope = oldScope
        
    def translateDeclaration(self, node):
        """
        - create variable
        - assign place for it in memory
        """
        name, type = (node.var.value, node.type.value)
        newVar = variable(name, type, self.currentScope.getFreeSpace(), node.var.isArray, node.var.size)
        if node.var.isArray:
            self.currentScope.offsetFree += (node.var.size-1) * 4

        self.currentScope.addElement(newVar)

    def translateDefinition(self, node):
        self.translateDeclaration(node)
        self.translateAssignment(node)

    def translateAssignment(self, node):
        """
        - find variable in the scope
        - get the result of the rvalue in a register
        - save the result in the memory place to which the variable points
        """
        element = self.currentScope.findElement(node.var.value, 'variable')
        if not element.isArray:
            resultReg = self.getRegFromRHS(node.children[-1], element.type)
            offset = self.currentScope.getElementOffSet(element)
            if element.type == "int":
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += "\tsw " + resultReg[0] + ", " + str(-offset) +  "($sp)\n"
                else:
                    self.code += "\tsw " + resultReg[0] + ", " + str(-offset) +  "($sp)\n"
                self.currentScope.setRegister(resultReg[0], False)

            elif element.type == "float":
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += "\ts.s " + resultReg[0] + ", " + str(-offset) +  "($sp)\n"
                else:
                    self.code += "\ts.s " + resultReg[0] + ", " + str(-offset) +  "($sp)\n"
                self.currentScope.setFloatRegister(resultReg[0], False)

            elif element.type == "char":
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += "\tsb " + resultReg[0] + ", " + str(-offset) +  "($sp)\n"
                else:
                    self.code += "\tsb " + resultReg[0] + ", " + str(-offset) +  "($sp)\n"
                self.currentScope.setRegister(resultReg[0], False)

        else:
            if node.children[-1].value == 'ARRAY_INIT':
                for index, rhs in enumerate(node.children[-1].children):
                    resultReg = self.getRegFromRHS(rhs, element.type)
                    offset = self.currentScope.getElementOffSet(element)
                    offset = self.currentScope.getElementOffSet(element)
                    if element.type == "int":
                        if isinstance(self.currentScope, global_scope):
                            self.globalVariables += "\tsw " + resultReg[0] + ", " + str(-(offset+4*index)) +  "($sp)\n"
                        else:
                            self.code += "\tsw " + resultReg[0] + ", " + str(-(offset+4*index)) +  "($sp)\n"
                        self.currentScope.setRegister(resultReg[0], False)

                    elif element.type == "float":
                        if isinstance(self.currentScope, global_scope):
                            self.globalVariables += "\ts.s " + resultReg[0] + ", " + str(-(offset+4*index)) +  "($sp)\n"
                        else:
                            self.code += "\ts.s " + resultReg[0] + ", " + str(-(offset+4*index)) +  "($sp)\n"
                        self.currentScope.setFloatRegister(resultReg[0], False)

                    elif element.type == "char":
                        if isinstance(self.currentScope, global_scope):
                            self.globalVariables += "\tsb " + resultReg[0] + ", " + str(-(offset+4*index)) +  "($sp)\n"
                        else:
                            self.code += "\tsb " + resultReg[0] + ", " + str(-(offset+4*index)) +  "($sp)\n"
                        self.currentScope.setRegister(resultReg[0], False)
                        
            else:
                resultReg = self.getRegFromRHS(node.children[-1], element.type)
                offset = self.currentScope.getElementOffSet(element)
                if element.type == "int":
                    if isinstance(self.currentScope, global_scope):
                        self.globalVariables += "\tsw " + resultReg[0] + ", " + str(-(offset+4*node.var.size)) +  "($sp)\n"
                    else:
                        self.code += "\tsw " + resultReg[0] + ", " + str(-(offset+4*node.var.size)) +  "($sp)\n"
                    self.currentScope.setRegister(resultReg[0], False)

                elif element.type == "float":
                    if isinstance(self.currentScope, global_scope):
                        self.globalVariables += "\ts.s " + resultReg[0] + ", " + str(-(offset+4*node.var.size)) +  "($sp)\n"
                    else:
                        self.code += "\ts.s " + resultReg[0] + ", " + str(-(offset+4*node.var.size)) +  "($sp)\n"
                    self.currentScope.setFloatRegister(resultReg[0], False)

                elif element.type == "char":
                    if isinstance(self.currentScope, global_scope):
                        self.globalVariables += "\tsb " + resultReg[0] + ", " + str(-(offset+4*node.var.size)) +  "($sp)\n"
                    else:
                        self.code += "\tsb " + resultReg[0] + ", " + str(-(offset+4*node.var.size)) +  "($sp)\n"
                    self.currentScope.setRegister(resultReg[0], False)

    def translateSelection(self, node, labelEnd, labelLoop, incrementor):
        ifLabel = {
            'label': 'label' + str(self.getLabelCounter()),
            'labelFalse': None,
            'labelEnd' : None
        }

        elIfLabels = []
        for elIf in node.elseIfStatements:
            elIfLabels.append({
                                'label': 'label' + str(self.getLabelCounter()),
                                'labelFalse': None,
                                'labelEnd' : None
                            })

        elseLabel = None
        if node.elseStatement is not None:
            elseLabel = {
            'label': 'label' + str(self.getLabelCounter()),
            'labelEnd' : None
        }

        endLabel = 'label' + str(self.getLabelCounter())

        #CHECK IF LABEL:
        if elIfLabels:
            ifLabel['labelFalse'] = elIfLabels[0]['label']
        elif elseLabel:
            ifLabel['labelFalse'] = elseLabel['label']
        else:
            ifLabel['labelFalse'] = endLabel
        ifLabel['labelEnd'] = endLabel

        #CHECK ELIF LABELS:
        for i in range(len(elIfLabels)):
            if i == len(elIfLabels) - 1:
                if elseLabel:
                    elIfLabels[i]['labelFalse'] = elseLabel['label']
                else:
                    elIfLabels[i]['labelFalse'] = endLabel
            else:
                elIfLabels[i]['labelFalse'] = elIfLabels[i+1]['label']

            elIfLabels[i]['labelEnd'] = endLabel

        #CHECK ELSE LABEL:
        if elseLabel:
            elseLabel['labelEnd'] = endLabel

        self.createMIPS(node.ifStatement,  labelEnd, labelLoop, incrementor, ifLabel)
        for i in range(len(elIfLabels)):
            self.createMIPS(node.elseIfStatements[i], labelEnd, labelLoop, incrementor, elIfLabels[i])
        if elseLabel:
            self.createMIPS(node.elseStatement,  labelEnd, labelLoop, incrementor, elseLabel)
        
        if isinstance(self.currentScope, global_scope):
            self.globalVariables += '\n' + endLabel + ':\n'
        else:
            self.code += '\n' + endLabel + ':\n'
    
    def translateIf(self, node, labels, labelEnd, labelLoop, incrementor):
        #generate condition
        comparisonNode = node.condition.children[0]
        comparisonResult = self.getComparisonResult(comparisonNode)
        if comparisonResult[1] == 'int':
            if isinstance(self.currentScope, global_scope):
                self.globalVariables = '\tbeqz ' + comparisonResult[0] + ', ' + labels['labelFalse'] + '\n'
            else:
                self.code += '\tbeqz ' + comparisonResult[0] + ', ' + labels['labelFalse'] + '\n'
            self.currentScope.setRegister(comparisonResult[0], False)

        elif comparisonResult[1] == 'bc1':
            if isinstance(self.currentScope, global_scope):
                self.globalVariables = '\t' + comparisonResult[0] + ' ' + labels['labelFalse'] + '\n'
            else:
                self.code += '\t' + comparisonResult[0] + ' ' + labels['labelFalse'] + '\n'

        #generate code inside
        self.createMIPS(node.block, labelEnd, labelLoop, incrementor)

        #jump to end 
        self.addJump(labels['labelEnd'])

    def translateElseIf(self, node, labels, labelEnd, labelLoop, incrementor):
        #generate condition
        comparisonNode = node.condition.children[0]
        comparisonResult = self.getComparisonResult(comparisonNode)
        if comparisonResult[1] == 'int':
            if isinstance(self.currentScope, global_scope):
                self.globalVariables = '\tbeqz ' + comparisonResult[0] + ', ' + labels['labelFalse'] + '\n'
            else:
                self.code += '\tbeqz ' + comparisonResult[0] + ', ' + labels['labelFalse'] + '\n'
            self.currentScope.setRegister(comparisonResult[0], False)

        elif comparisonResult[1] == 'bc1':
            if isinstance(self.currentScope, global_scope):
                self.globalVariables = '\t' + comparisonResult[0] + ' ' + labels['labelFalse'] + '\n'
            else:
                self.code += '\t' + comparisonResult[0] + ' ' + labels['labelFalse'] + '\n'
        
        #generate code inside
        self.createMIPS(node.block, labelEnd, labelLoop, incrementor)

        #jump to end 
        self.addJump(labels['labelEnd'])

    def translateElse(self, node, labels, labelEnd, labelLoop, incrementor):
        #generate code inside
        self.createMIPS(node.block, labelEnd, labelLoop, incrementor)

        #jump to end 
        self.addJump(labels['labelEnd'])

    def translateWhile(self, node, increment = None):
        loopLabel = 'label' + str(self.getLabelCounter())
        endLabel = 'label' + str(self.getLabelCounter())
        #Create label for the loop
        if isinstance(self.currentScope, global_scope):
            self.globalVariables = '\n' + loopLabel + ':\n'
        else:
            self.code += '\n' + loopLabel + ':\n'

        #Generate condition
        comparisonNode = node.condition.children[0]
        comparisonResult = self.getComparisonResult(comparisonNode)
        if comparisonResult[1] == 'int':
            if isinstance(self.currentScope, global_scope):
                self.globalVariables = '\tbeqz ' + comparisonResult[0] + ', ' + endLabel + '\n'
            else:
                self.code += '\tbeqz ' + comparisonResult[0] + ', ' + endLabel + '\n'
            self.currentScope.setRegister(comparisonResult[0], False)

        elif comparisonResult[1] == 'bc1':
            if isinstance(self.currentScope, global_scope):
                self.globalVariables = '\t' + comparisonResult[0] + ' ' + endLabel + '\n'
            else:
                self.code += '\t' + comparisonResult[0] + ' ' + endLabel + '\n'


        self.createMIPS(node.block, endLabel, loopLabel, increment)
        #Generate code inside
        if increment:
            self.createMIPS(increment, endLabel, loopLabel, increment)

        #Go back to loop
        self.addJump(loopLabel)

        #Create label for the end
        if isinstance(self.currentScope, global_scope):
            self.globalVariables = '\n' + endLabel + ':\n'
        else:
            self.code += '\n' + endLabel + ':\n'

    def translateFor(self, node):
        self.createMIPS(node.initiator)
        self.translateWhile(node, node.increment)

    def translatePrint(self, node):
        if node.code == '"%s"':
            label = '$string' + str(self.getStringCounter())
            string = node.exp.value.replace('"', "")
            self.data += '\t' + label + ': .asciiz "' + string + '"\n'
            if isinstance(self.currentScope, global_scope):
                self.globalVariables += '\tli $v0, 4\n'
                self.globalVariables += '\tla $a0, ' + label + '\n'
                self.globalVariables += '\tsyscall\n'
            else:
                self.code += '\tli $v0, 4\n'
                self.code += '\tla $a0, ' + label + '\n'
                self.code += '\tsyscall\n'

        elif node.code == '"%i"':
            resultReg = self.getRegFromRHS(node.children[-1], 'int')
            if isinstance(self.currentScope, global_scope):
                self.globalVariables += '\tli $v0, 1\n'
                self.globalVariables += '\tmove $a0, ' + resultReg[0] + '\n'
                self.globalVariables += '\tsyscall\n'
            else:
                self.code += '\tli $v0, 1\n'
                self.code += '\tmove $a0, ' + resultReg[0] + '\n'
                self.code += '\tsyscall\n'
            self.currentScope.setRegister(resultReg[0], False)

        elif node.code == '"%d"' or node.code == '"%f"':
            resultReg = self.getRegFromRHS(node.children[-1], 'float')
            if isinstance(self.currentScope, global_scope):
                self.globalVariables += '\tli $v0, 2\n'
                self.globalVariables += '\tmov.s $f12, ' + resultReg[0] + '\n'
                self.globalVariables += '\tsyscall\n'
            else:
                self.code += '\tli $v0, 2\n'
                self.code += '\tmov.s $f12, ' + resultReg[0] + '\n'
                self.code += '\tsyscall\n'
            self.currentScope.setFloatRegister(resultReg[0], False)

        elif node.code == '"%c"':
            resultReg = self.getRegFromRHS(node.children[-1], 'char')
            if isinstance(self.currentScope, global_scope):
                self.globalVariables += '\tli $v0, 11\n'
                self.globalVariables += '\tmove $a0, ' + resultReg[0] + '\n'
                self.globalVariables += '\tsyscall\n'
            else:
                self.code += '\tli $v0, 11\n'
                self.code += '\tmove $a0, ' + resultReg[0] + '\n'
                self.code += '\tsyscall\n'
            self.currentScope.setRegister(resultReg[0], False)
    
    def translateFuncDef(self, node):
        element = self.currentScope.findElement(node.name.value, 'function')
        if isinstance(self.currentScope, global_scope):
            self.globalVariables += '$func' + element.name + ':\n'
        else:
            self.code += '$func' + element.name + ':\n'

        if element.name != 'main':
            offset = self.currentScope.getFreeSpace()
            if isinstance(self.currentScope, global_scope):
                self.globalVariables += '\tsw $ra, ' + str(-offset) + '($sp)\n'
            else:
                self.code += '\tsw $ra, ' + str(-offset) + '($sp)\n'
            returnAdress = variable('$ra', 'returnAdress', offset)
            self.currentScope.addElement(returnAdress)

        #GENERATE CODE INSIDE
        self.createMIPS(node.body)

        if element.name != 'main':
            #JUMP BACK IF RETURN NOT ACCESED
            if isinstance(self.currentScope, global_scope):
                self.globalVariables += '\tlw $ra, ' + str(-offset) + '($sp)\n'
                self.globalVariables += '\tjr $ra\n'
            else:
                self.code += '\tlw $ra, ' + str(-offset) + '($sp)\n'
                self.code += '\tjr $ra\n'
        else:
            if isinstance(self.currentScope, global_scope):
                self.globalVariables += '\tli $v0, 10\n'
                self.globalVariables += '\tsyscall\n'
            else:
                self.code += '\tli $v0, 10\n'
                self.code += '\tsyscall\n'
    
    def translateFuncCall(self, node, save):
        element = self.currentScope.findElement(node.name.value, 'function')

        offsetSave = 0
        #FIRST SAVE THE REGISTERS THAT ARE BEING USED
        for register in self.currentScope.registers:
            if self.currentScope.registers[register]:
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += "\tsw " + register + ", " + str(-(self.currentScope.offsetFree + offsetSave)) +  "($sp)\n"                
                else:
                    self.code += "\tsw " + register + ", " + str(-(self.currentScope.offsetFree + offsetSave)) +  "($sp)\n"
                offsetSave += 4

        for register in self.currentScope.floatRegisters:
            if self.currentScope.floatRegisters[register]:
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += "\ts.s " + register + ", " + str(-(self.currentScope.offsetFree + offsetSave)) +  "($sp)\n"              
                else:
                    self.code += "\ts.s " + register + ", " + str(-(self.currentScope.offsetFree + offsetSave)) +  "($sp)\n"
                
                offsetSave += 4        

        #LOAD PARAMETERS IN MEMORY
        offset = 0
        for index, parameter in enumerate(node.parameters.children):
            resultReg = self.getRegFromRHS(parameter, element.arguments[index].type)
            if element.arguments[index].type == "int":
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += "\tsw " + resultReg[0] + ", " + str(-(self.currentScope.offsetFree + offsetSave + offset)) +  "($sp)\n"            
                else:
                    self.code += "\tsw " + resultReg[0] + ", " + str(-(self.currentScope.offsetFree + offsetSave + offset)) +  "($sp)\n"
                self.currentScope.setRegister(resultReg[0], False)
            elif element.arguments[index].type == "float":
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += "\ts.s " + resultReg[0] + ", " + str(-(self.currentScope.offsetFree + offsetSave + offset)) +  "($sp)\n"           
                else:
                    self.code += "\ts.s " + resultReg[0] + ", " + str(-(self.currentScope.offsetFree + offsetSave + offset)) +  "($sp)\n"
                self.currentScope.setFloatRegister(resultReg[0], False)
            elif element.arguments[index].type == "char":
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += "\tsb " + resultReg[0] + ", " + str(-(self.currentScope.offsetFree + offsetSave + offset)) +  "($sp)\n"          
                else:
                    self.code += "\tsb " + resultReg[0] + ", " + str(-(self.currentScope.offsetFree + offsetSave + offset)) +  "($sp)\n"
                self.currentScope.setRegister(resultReg[0], False)
            offset += 4

        #add sp for function
        if isinstance(self.currentScope, global_scope):
            self.globalVariables += '\taddi $sp, $sp, ' + str(-(self.currentScope.offsetFree + offsetSave)) + '\n'
            self.globalVariables += '\tjal $func' + element.name + '\n'
            self.globalVariables += '\taddi $sp, $sp, ' + str(self.currentScope.offsetFree + offsetSave) + '\n'         
        else:
            self.code += '\taddi $sp, $sp, ' + str(-(self.currentScope.offsetFree + offsetSave)) + '\n'
            self.code += '\tjal $func' + element.name + '\n'
            self.code += '\taddi $sp, $sp, ' + str(self.currentScope.offsetFree + offsetSave) + '\n'
        
        #GET RESULT
        resultReg = 0
        if save:
            if element.returnType in ['int', 'char']:
                resultReg = self.currentScope.getFreeRegister(False)
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += '\tmove ' + resultReg + ', $v0\n'
                else:
                    self.code += '\tmove ' + resultReg + ', $v0\n'
            elif element.returnType == 'float':
                resultReg = self.currentScope.getFreeRegister(True)
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += '\tmov.s ' + resultReg + ', $f1\n'
                else:
                    self.code += '\tmov.s ' + resultReg + ', $f1\n'
            else:
                pass

        #SET REGISTERS BACK
        offsetSave = 0
        for register in self.currentScope.registers:
            if self.currentScope.registers[register] and register != resultReg:
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += "\tlw " + register + ", " + str(-(self.currentScope.offsetFree + offsetSave)) +  "($sp)\n"
                else:
                    self.code += "\tlw " + register + ", " + str(-(self.currentScope.offsetFree + offsetSave)) +  "($sp)\n"
                offsetSave += 4

        for register in self.currentScope.floatRegisters:
            if self.currentScope.floatRegisters[register]:
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += "\tl.s " + register + ", " + str(-(self.currentScope.offsetFree + offsetSave)) +  "($sp)\n"
                else:
                    self.code += "\tl.s " + register + ", " + str(-(self.currentScope.offsetFree + offsetSave)) +  "($sp)\n"
                offsetSave += 4

        #RETURN THE RESULT REGISTER
        return (resultReg, element.returnType)

    def translateReturn(self, node):
        functionScope = self.currentScope
        offSetFunctionScope = 0
        while not isinstance(functionScope, func_scope):
            offSetFunctionScope += functionScope.parentScope.offsetFree
            functionScope = functionScope.parentScope
        if not functionScope.mainScope:
            if node.returnExp:           
                returnRegister = self.getRegFromRHS(node.returnExp, functionScope.returnType)             
                if functionScope.returnType in ['int', 'char']:
                    if isinstance(self.currentScope, global_scope):
                        self.globalVariables += '\tmove $v0, ' + returnRegister[0] + '\n'
                    else:
                        self.code += '\tmove $v0, ' + returnRegister[0] + '\n'
                else:
                    if isinstance(self.currentScope, global_scope):
                        self.globalVariables += '\tmov.s $f1, ' + returnRegister[0] + '\n'
                    else:
                        self.code += '\tmov.s $f1, ' + returnRegister[0] + '\n'
                
            returnAdress = self.currentScope.findElement('$ra', 'variable')
            if isinstance(self.currentScope, global_scope):
                self.globalVariables += '\tlw $ra, ' + str(-self.currentScope.getElementOffSet(returnAdress)) + '($sp)\n'
                self.globalVariables += '\taddi $sp, $sp, ' + str(offSetFunctionScope) + '\n'
                self.globalVariables += '\tjr $ra\n'
            else:
                self.code += '\tlw $ra, ' + str(-self.currentScope.getElementOffSet(returnAdress)) + '($sp)\n'
                self.code += '\taddi $sp, $sp, ' + str(offSetFunctionScope) + '\n'
                self.code += '\tjr $ra\n'
                       
        else:
            if isinstance(self.currentScope, global_scope):
                self.globalVariables += '\tli $v0, 10\n'
                self.globalVariables += '\tsyscall\n'
            else:
                self.code += '\tli $v0, 10\n'
                self.code += '\tsyscall\n'

#HELPFUL FUNCTIONS

    def addJump(self, label):
        if isinstance(self.currentScope, global_scope):
            self.globalVariables += '\tj ' + label + '\n'
        else:   
            self.code += '\tj ' + label + '\n'

    def getComparisonResult(self, comparisonNode):
        leftOp = self.getRegFromRHS(comparisonNode.leftOp)
        rightOp = self.getRegFromRHS(comparisonNode.rightOp)

        if leftOp[1] != rightOp[1]:
            if leftOp[1] in ['int', 'float'] and rightOp[1] in ['int', 'float']:
                if leftOp[1] == 'int':
                    leftOp = (self.convertRegister(leftOp[0], 'float'), 'float')
                elif rightOp[1] == 'int':
                    rightOp = (self.convertRegister(rightOp[0], 'float'), 'float')

        type = leftOp[1]
        bc1 = "bc1f"

        if isinstance(comparisonNode, EqNode):
            if type == 'int':
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += '\tseq ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                else:
                    self.code += '\tseq ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'
            elif type == 'float':
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += '\tc.eq.s ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                else:
                    self.code += '\tc.eq.s ' + leftOp[0] + ', ' + rightOp[0] + '\n'

        elif isinstance(comparisonNode, NeqNode):
            if type == 'int':
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += '\tsne ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                else:
                    self.code += '\tsne ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'

            elif type == 'float':
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += '\tc.eq.s ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                else:
                    self.code += '\tc.eq.s ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                bc1 = "bc1t"

        elif isinstance(comparisonNode, GtNode):
            if type == 'int':
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += '\tsgt ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                else:
                    self.code += '\tsgt ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'
            elif type == 'float':
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += '\tc.le.s ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                else:
                    self.code += '\tc.le.s ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                bc1 = "bc1t"

        elif isinstance(comparisonNode, GetNode):
            if type == 'int':
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += '\tsge ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                else:
                    self.code += '\tsge ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'

            elif type == 'float':
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += '\tc.lt.s ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                else:
                    self.code += '\tc.lt.s ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                bc1 = "bc1t"

        elif isinstance(comparisonNode, StNode):
            if type == 'int':
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += '\tslt ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                else:
                    self.code += '\tslt ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'

            elif type == 'float':
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += '\tc.lt.s ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                else:
                    self.code += '\tc.lt.s ' + leftOp[0] + ', ' + rightOp[0] + '\n'

        elif isinstance(comparisonNode, SetNode):
            if type == 'int':
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += '\tsle ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                else:
                    self.code += '\tsle ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'
            elif type == 'float':
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += '\tc.le.s ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                else:
                    self.code += '\tc.le.s ' + leftOp[0] + ', ' + rightOp[0] + '\n'
        
        
        if type == 'float':
            self.currentScope.setFloatRegister(rightOp[0], False)
            self.currentScope.setFloatRegister(leftOp[0], False)
            return (bc1, 'bc1')
        else:
            self.currentScope.setRegister(rightOp[0], False)
            return leftOp 

    def getRegFromRHS(self, node, Target = ''):
        operators = ['+', '-', '*', '/', '%']

        if isinstance(node, ConstNode):
            if Target and node.type != Target:
                if Target == 'int':
                    result = int(float(node.value))
                    register = self.currentScope.getFreeRegister(False)
                    if isinstance(self.currentScope, global_scope):
                        self.globalVariables += '\tli '+ register +', ' + str(result) + '\n'
                    else:
                        self.code += '\tli '+ register +', ' + str(result) + '\n'
                    return (register, 'int')
                
                elif Target == 'float':
                    result = float(node.value)
                    register = self.currentScope.getFreeRegister(True)
                    data = '$float' + str(self.getFloatCounter())
                    self.data += '\t' + data + ': .float ' + str(result) + '\n'
                    if isinstance(self.currentScope, global_scope):
                        self.globalVariables += '\tl.s ' + register + ', ' + data + '\n'
                    else:
                        self.code += '\tl.s ' + register + ', ' + data + '\n'
                    return (register, 'float')
            
            else:
                if node.type == 'int':
                    register = self.currentScope.getFreeRegister(False)
                    if isinstance(self.currentScope, global_scope):
                        self.globalVariables += '\tli '+ register +', ' + str(node.value) + '\n'
                    else:
                        self.code += '\tli '+ register +', ' + str(node.value) + '\n'
                    return (register, 'int')
                    
                elif node.type == 'float':
                    register = self.currentScope.getFreeRegister(True)
                    data = '$float' + str(self.getFloatCounter())
                    self.data += '\t' + data + ': .float ' + str(node.value) + '\n'
                    if isinstance(self.currentScope, global_scope):
                        self.globalVariables += '\tl.s ' + register + ', ' + data + '\n'
                    else:
                        self.code += '\tl.s ' + register + ', ' + data + '\n'
                    return (register, 'float')

                elif node.type == 'char':
                    register = self.currentScope.getFreeRegister(False)
                    if isinstance(self.currentScope, global_scope):
                        self.globalVariables += '\tli ' + register + ', '+ str(ord(node.value[1])) + '\n'
                    else:
                        self.code += '\tli ' + register + ', '+ str(ord(node.value[1])) + '\n'
                    return (register, 'char')
                        
                
        elif isinstance(node, VarNode):
            element = self.currentScope.findElement(node.value, 'variable')
            offset = self.currentScope.getElementOffSet(element)
            if element.isArray:
                offset += node.size * 4

            if Target and element.type != Target:
                if element.type == 'int' or element.type == 'float':
                    #SET FLOAT TO INT
                    if element.type == 'float':
                        floatRegister = self.currentScope.getFreeRegister(True)
                        if isinstance(self.currentScope, global_scope):
                            self.globalVariables += '\tl.s ' + floatRegister + ', ' + str(-offset) +  "($sp)\n"
                        else:
                            self.code += '\tl.s ' + floatRegister + ', ' + str(-offset) +  "($sp)\n"
                        intRegister = self.convertRegister(floatRegister, 'int')
                        return (intRegister, 'int')

                    #SET INT TO FLOAT
                    elif element.type == 'int':
                        intRegister = self.currentScope.getFreeRegister(False)
                        if isinstance(self.currentScope, global_scope):
                            self.globalVariables += '\tlw ' + intRegister + ', ' + str(-offset) +  "($sp)\n"
                        else:
                            self.code += '\tlw ' + intRegister + ', ' + str(-offset) +  "($sp)\n"
                        floatRegister = self.convertRegister(intRegister, 'float')
                        return (floatRegister, 'float')

            else:
                if element.type == 'int':
                    register = self.currentScope.getFreeRegister(False)
                    if isinstance(self.currentScope, global_scope):
                        self.globalVariables += '\tlw ' + register + ', ' + str(-offset) +  "($sp)\n"
                    else:
                        self.code += '\tlw ' + register + ', ' + str(-offset) +  "($sp)\n"
                    return (register, 'int')
                
                elif element.type == 'float':
                    register = self.currentScope.getFreeRegister(True)
                    if isinstance(self.currentScope, global_scope):
                        self.globalVariables += '\tl.s ' + register + ', ' + str(-offset) +  "($sp)\n"
                    else:
                        self.code += '\tl.s ' + register + ', ' + str(-offset) +  "($sp)\n"
                    return (register, 'float')
                
                elif element.type == 'char':
                    register = self.currentScope.getFreeRegister(False)
                    if isinstance(self.currentScope, global_scope):
                        self.globalVariables += '\tlb ' + register + ', ' + str(-offset) + "($sp)\n"
                    else:
                        self.code += '\tlb ' + register + ', ' + str(-offset) + "($sp)\n"
                    return (register, 'char')


        elif isinstance(node , FuncCallNode):
            result = self.translateFuncCall(node, True)
            if Target and result[1] != Target:
                if Target == 'int':
                    intRegister = self.convertRegister(result[0], 'int')
                    return (intRegister, 'int')

                elif Target == 'float':
                    floatRegister = self.convertRegister(result[0], 'float')
                    return (floatRegister, 'float')

            else:
                return result        

        elif node.value in operators:
            leftOp = self.getRegFromRHS(node.leftOp) #this reg will also be the result
            rightOp = self.getRegFromRHS(node.rightOp)

            if leftOp[1] != rightOp[1]:
                if leftOp[1] == 'int':
                    leftOp = (self.convertRegister(leftOp[0], 'float'), 'float')
                    
                elif rightOp[1] == 'int':
                    rightOp = (self.convertRegister(rightOp[0], 'float'), 'float')
            
            if isinstance(node, PlusNode):
                if leftOp[1]== 'float':
                    if isinstance(self.currentScope, global_scope):
                        self.globalVariables += '\tadd.s ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                    else:
                        self.code += '\tadd.s ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'

                elif leftOp[1] == 'int':
                    if isinstance(self.currentScope, global_scope):
                        self.globalVariables += '\tadd ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                    else:
                        self.code += '\tadd ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'

            elif isinstance(node, MinusNode):
                if leftOp[1]== 'float':
                    if isinstance(self.currentScope, global_scope):
                        self.globalVariables += '\tsub.s ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                    else:
                        self.code += '\tsub.s ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'


                elif leftOp[1]== 'int':
                    if isinstance(self.currentScope, global_scope):
                        self.globalVariables += '\tsub ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                    else:
                        self.code += '\tsub ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'

            elif isinstance(node, MulNode):
                if leftOp[1]== 'float':
                    if isinstance(self.currentScope, global_scope):
                        self.globalVariables += '\tmul.s ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                    else:
                        self.code += '\tmul.s ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'

                elif leftOp[1]== 'int':
                    if isinstance(self.currentScope, global_scope):
                        self.globalVariables += '\tmul ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                    else:
                        self.code += '\tmul ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'


            elif isinstance(node, DivNode):
                if leftOp[1]== 'float':
                    if isinstance(self.currentScope, global_scope):
                        self.globalVariables += '\tdiv.s ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                    else:
                        self.code += '\tdiv.s ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'

                elif leftOp[1]== 'int':
                    if isinstance(self.currentScope, global_scope):
                        self.globalVariables += '\tdiv ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                    else:
                        self.code += '\tdiv ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'


            elif isinstance(node, ModNode):
                if isinstance(self.currentScope, global_scope):
                    self.globalVariables += '\trem ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'
                else:
                    self.code += '\trem ' + leftOp[0] + ', ' + leftOp[0] + ', ' + rightOp[0] + '\n'

            #DELETE REG RIGHTOP
            if rightOp[1] == 'float':
                self.currentScope.setFloatRegister(rightOp[0], False)
            else:
                self.currentScope.setRegister(rightOp[0], False)

            #CONVERT IF TARGET
            if Target and leftOp[1] != Target:
                if Target == 'int':
                    intRegister = self.convertRegister(leftOp[0], 'int')
                    return (intRegister, 'int')

                elif Target == 'float':
                    floatRegister = self.convertRegister(leftOp[0], 'float')
                    return (floatRegister, 'float')

            else:
                return leftOp

    def getFloatCounter(self):
        self.floatCounter += 1
        return self.floatCounter - 1
    
    def getLabelCounter(self):
        self.labelCounter += 1
        return self.labelCounter - 1
    
    def getStringCounter(self):
        self.stringCounter += 1
        return self.stringCounter - 1
        
    def convertRegister(self, register, target):

        #CONVERT FLOAT TO INT
        if target == 'int':
            intRegister = self.currentScope.getFreeRegister(False)
            if isinstance(self.currentScope, global_scope):
                self.globalVariables += '\tcvt.w.s ' + register + ', ' + register + '\n'
                self.globalVariables += '\tmfc1 ' + intRegister + ', ' + register + '\n'
            else:
                self.code += '\tcvt.w.s ' + register + ', ' + register + '\n'
                self.code += '\tmfc1 ' + intRegister + ', ' + register + '\n'
            self.currentScope.setFloatRegister(register, False)
            return intRegister


        #CONVERT INT TO FLOAT
        elif target == 'float':
            floatRegister = self.currentScope.getFreeRegister(True)
            if isinstance(self.currentScope, global_scope):
                self.globalVariables += '\tmtc1 ' + register + ', ' + floatRegister + '\n'
                self.globalVariables += '\tcvt.s.w ' + floatRegister + ', ' + floatRegister + '\n'
            else:
                self.code += '\tmtc1 ' + register + ', ' + floatRegister + '\n'
                self.code += '\tcvt.s.w ' + floatRegister + ', ' + floatRegister + '\n'
            self.currentScope.setRegister(register, False)
            return floatRegister
