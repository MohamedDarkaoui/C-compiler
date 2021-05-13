from src.Nodes import *
from mipsSymbolTable import *

class MIPS():
    def __init__(self, AST):
        self.root = AST.root
        self.code = ""
        self.data = ""
        self.floatCounter = 0
        self.currentScope = None
    
    def toMIPS(self, filename):
        open(filename, "w+")
        root = self.root
        with open(filename, 'w') as file:
            self.createMIPS(self.root)
            if self.data:
                self.data = '.data\n' + self.data + '.text\n\n\n\n'
            file.write(self.data + self.code)
        file.close()
        #RESET
        self.code = ""
        self.root = root


    def createMIPS(self, currentNode):
        oldScope = self.currentScope
        if isinstance(currentNode, ScopeNode):
            if currentNode.value == 'global_scope':
                self.currentScope = global_scope()
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
        
        else:
            for child in currentNode.children:
                self.createMIPS(child)
                if oldScope is not None:
                        self.currentScope = oldScope

        """
        elif isinstance(currentNode, SelectNode):
            pass
        elif isinstance(currentNode, WhileNode):
            pass
        elif isinstance(currentNode, ForNode):
            pass
        elif isinstance(currentNode, FuncDefNode):
            pass
        elif isinstance(currentNode, ReturnNode):
            pass
        elif isinstance(currentNode, BreakNode):
            pass

        elif isinstance(currentNode, ContinueNode):
            pass

        elif isinstance(currentNode, FuncCallNode):
            pass

        elif isinstance(currentNode, PrintNode):
            pass
        """
        
        



    def translateDeclaration(self, node):
        name, type = (node.var.value, node.type.value)
        newVar = variable(name, type, self.currentScope.getFreeSpace())
        self.currentScope.addElement(newVar)
        """
        - create variable
        - assign place for it in memory
        """

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
        resultReg = self.getRegFromRHS(node.rvalue, element.type)
        offset = self.currentScope.getElementOffSet(element)
        if element.type == "int":
            self.code += "\tsw " + resultReg + ", " + str(-offset) +  "($sp)\n"
        elif element.type == "float":
            self.code += "\ts.s " + resultReg + ", " + str(-offset) +  "($sp)\n"

    def getRegFromRHS(self, node, Target = ''):
        operators = ['+', '-', '*', '/', '%']

        if isinstance(node, ConstNode):
            if Target:
                if node.type == 'int' or node.type == 'float':
                    if Target == 'int':
                        result = int(float(node.value))
                        self.code += '\tli $t0, ' + str(result) + '\n' 
                        return '$t0'
                    
                    elif Target == 'float':
                        result = float(node.value)
                        data = 'float' + str(self.getFloatCounter())
                        self.data += '\t' + data + ': .float ' + str(result) + '\n'
                        self.code += '\tl.s $f0, ' + data + '\n'
                        return '$f0'
            
            else:
                if node.type == 'int':
                    self.code += '\tli $t0, ' + str(node.value) + '\n' 
                    return '$t0'
                
                elif node.type == 'float':
                    data = 'float' + str(self.getFloatCounter())
                    self.data += '\t' + data + ': .float ' + str(node.value) + '\n'
                    self.code += '\tl.s $f0, ' + data + '\n'
                    return '$f0'
                        
                

        
        elif isinstance(node, VarNode):
            """
                - lw in to a free register
                - return the register
            """
            element = self.currentScope.findElement(node.value, 'variable')
            offset = self.currentScope.getElementOffSet(element)

            if Target and element.type != Target:
                if element.type == 'int' or element.type == 'float':
                    #SET FLOAT TO INT
                    if element.type == 'float':
                        self.code += '\tl.s $f0, ' + str(-offset) +  "($sp)\n"
                        pass

                    #SET INT TO FLOAT
                    elif element.type == 'int':
                        self.code += '\tlw $t0, ' + str(-offset) +  "($sp)\n"
                        pass

            else:
                if element.type == 'int':
                    self.code += '\tlw $t0, ' + str(-offset) +  "($sp)\n"
                    return '$t0'
                
                elif element.type == 'float':
                    self.code += '\tl.s $f0, ' + str(-offset) +  "($sp)\n"
                    return '$f0'

        elif isinstance(node , FuncCallNode):
            """
                - load parameters to the right place in memory
                - call the function
                - move $v0 in to a free register
                - return the register
            """
            pass        

        elif node.value in operators:
            """
                - get leftOp and rightOp
                - do the operation in to a free register
                - return the register
            """
            leftOp = self.getRegFromRHS(node.leftOp)
            rightOp = self.getRegFromRHS(node.rightOp)

            #CONVERT IF THE TYPES ARE NOT THE SAME
            


            pass



    

    def getFloatCounter(self):
        self.floatCounter += 1
        return self.floatCounter - 1

        

