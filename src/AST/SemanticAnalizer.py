from ..symbolTable import *
from src.Nodes import *

class SemanticAnalizer:
    def __init__(self):
        self.root = None
        self.currentScope = None
        self.studioh = False
        self.main = False

    def analizeAST(self, AST):
        self.root = AST.root
        self.analize(self.root)
        if not self.main:
            raise Exception("Semantic Error: There isn't a main function.")

        #RESET
        self.currentScope = None
        self.studioh = False
        self.main = False

    def analize(self, currentNode):
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
            
        elif isinstance(currentNode, ForNode):
            self.currentScope = for_scope(self.currentScope)
            oldScope = self.currentScope
        
        elif isinstance(currentNode, DecNode):
            #CHECK IF VARIABLE DOESNT ALREADY EXIST IN THE CURRENTSCOPE
            self.checkNotExistence(currentNode.var.value , 'variable')

            #ADD UNINITIALIZED VARIABLE TO CURRENTSCOPE
            init = False
            if currentNode.var.isArray:
                init = True
            newVariable = variable(node=currentNode.var, type=currentNode.type.value, init=init, const=False)
            self.currentScope.addElement(newVariable)

        elif isinstance(currentNode, DefNode):
            #CHECK IF VARIABLE DOESNT ALREADY EXIST IN THE CURRENTSCOPE
            self.checkNotExistence(currentNode.var.value , 'variable')

            #CHECK OF THE RVALUE:
            if currentNode.var.isArray:
                if len(currentNode.rvalue.children) != currentNode.var.size:
                    raise Exception('Semantic Error: Array ' + currentNode.var.value + ' is of size ' + str(currentNode.var.size) + ' but the initializator ' 
                        + 'is of size ' + str(len(currentNode.rvalue.children)))
            self.analizeRHS(currentNode.rvalue, currentNode.type.value)

            #ADD INITIALIZED VARIABLE TO CURRENTSCOPE
            newVariable = variable(node=currentNode.var, type=currentNode.type.value, init=True, const=currentNode.const)
            self.currentScope.addElement(newVariable)
            
        elif isinstance(currentNode, AssignNode):
            #CHECK THAT THE VARIABLE EXISTS IN THE CURRENT SCOPE
            self.checkExistence(currentNode.var.value, 'variable')
            element = self.currentScope.getElement(currentNode.var.value, 'variable')
            #CHECK THAT THE VARIABLE ISN'T CONSTANT
            if self.currentScope.getElement(currentNode.var.value, 'variable').const:
                raise Exception("Semantic Error: Variable " + currentNode.var.value + " is constant so its value cannot be changed.")

            #CHECK THE RHS
            self.analizeRHS(currentNode.rvalue, self.currentScope.getElement(currentNode.var.value, 'variable').type)
            
            #SPECIAL CASE IF ITS AN ARRAY
            #CHECK INDEX < ARRAY SIZE (CASE ITS AN ARRAY)
            if element.isArray:
                if currentNode.var.size >= element.size:
                    raise Exception('Semantic Error: Index is greater than the array size.')

            #CHECK WRONG ASSIGN VARIABLE/ARRAY
            element = self.currentScope.getElement(currentNode.var.value, 'variable')
            if element.isArray != currentNode.var.isArray:
                raise Exception('Variable ' + element.name + ' is an array.')
            
            #ARRAY CASE
            if element.isArray != currentNode.var.isArray:
                raise Exception('Semantic Error: ' + element.name + ' is an array.')

            #CHECK INDEX < ARRAY SIZE (CASE ITS AN ARRAY)
            if element.isArray:
                if currentNode.var.size >= element.size:
                    raise Exception('Index is greater than the array size.')

            #INITIALIZE VARIABLE IF ITS NOT INITIALIZED
            self.currentScope.getElement(currentNode.var.value, 'variable').init = True
        
        elif isinstance(currentNode, FuncDefNode):
            if not isinstance(self.currentScope, global_scope):
                raise Exception("Semantic error: Function definition not inside of a global scope.")
        
            #RETRIEVE DATA
            returnType = currentNode.type.value
            name = currentNode.name.value
            if name == 'main':
                self.main = True

            arguments = []
            for argument in currentNode.arguments.children:
                arguments.append(variable(node=argument.var, type=argument.type.value, init=True, const=False))
            
            for argument in arguments:
                for argument2 in arguments:
                    if argument.name == argument2.name and argument != argument2:
                        raise Exception('Semantic Error: Redefinition of argument ' + argument.name)

            #CHECK EXISTENCE
            self.checkNotExistence(name, 'function')

            #CREATE NEW FUNCTION AND CHANGE SCOPE
            newFunction = Function(name = name, returnType = returnType, arguments = arguments, init=True)
            self.currentScope.addElement(newFunction)
            self.currentScope = func_scope(self.currentScope, arguments, returnType)
            oldScope = self.currentScope

        elif isinstance(currentNode, FuncCallNode):
            self.analizeFuncCall(currentNode)

        elif isinstance(currentNode, ReturnNode):
            #CHECK RETURN IS INSIDE A FUNCTION SCOPE
            temp = self.currentScope
            while not isinstance(temp, global_scope):
                if isinstance(temp, func_scope):
                    break
                temp = temp.parentScope
            
            if isinstance(temp, global_scope):
                raise Exception("Semantic error: return statement outside a function scope.")

            #CHECK THE RHS OF THE RETURN IS OF TYPE func_scope.returnType:
            if temp.returnType == 'void':
                if currentNode.returnExp is not None:
                    raise Exception("return error")
            else:
                if currentNode.returnExp is None:
                    raise Exception("return error")
                else:
                    self.analizeRHS(currentNode.returnExp, temp.returnType)

        elif isinstance(currentNode, BreakNode) or isinstance(currentNode, ContinueNode):
            #CHECK BREAK OR CONTINUE IS INSIDE A LOOP
            temp = self.currentScope
            while not isinstance(temp, global_scope):
                if isinstance(temp, for_scope) or isinstance(temp, while_scope):
                    break
                temp = temp.parentScope

            if isinstance(temp, global_scope):
                if isinstance(currentNode, BreakNode):
                    raise Exception("Semantic error: break statement outside a loop scope.")
                raise Exception("Semantic error: continue statement outside a loop scope.")
        
        elif isinstance(currentNode, PrintNode):
            if not self.studioh:
                raise Exception("Semantic error: unknown function printf.")
        
        elif isinstance(currentNode, IncludeNode):
            if currentNode.value == '<studio.h>':
                self.studioh = True

        elif isinstance(currentNode, ConditionNode):
            self.analizeCondition(currentNode)

        if isinstance(currentNode, PrintNode):
            self.analizePrint(currentNode)


        for child in currentNode.children:
            self.analize(child)
            if oldScope is not None:
                self.currentScope = oldScope
    
    def analizeRHS(self, currentNode, type):
        if isinstance(currentNode, VarNode):                # VARIABLES
            #EXISTENCE CHECKING
            self.checkExistence(currentNode.value, 'variable')

            #INIT CHECKING    
            self.checkInit(currentNode.value, 'variable')
            element = self.currentScope.getElement(currentNode.value, 'variable')
            # TYPE CHECKING
            if element.type in ['int', 'float']:
                if type == 'char':
                    raise Exception("Semantic Error: Variable " + currentNode.value + " is of type " + element.type + ' but it should be of type char.')
            elif element.type == 'char':
                if type in ['int', 'float']:
                    raise Exception("Semantic Error: Variable " + currentNode.value + " is of type " + element.type + ' but it should be of type int or float.')
            
            #SPECIAL CASE ARRAY
            if element.isArray != currentNode.isArray:
                if element.isArray:
                    raise Exception('Semantic Error: ' + element.name + ' is an array.')
                else:
                    raise Exception('Semantic Error: ' + element.name + ' is not an array.')
            
            #CHECK INDEX < ARRAY SIZE (CASE ITS AN ARRAY)
            if element.isArray:
                if currentNode.size >= element.size:
                    raise Exception('Semantic Error: Index is greater than the array size.')

        elif isinstance(currentNode, FuncCallNode):         # FUNCTION CALLS
            # ANALIZE FUNCTION
            self.analizeFuncCall(currentNode)
            # ANALIZE RETURN TYPE
            returnType = self.currentScope.getElement(currentNode.name.value, 'function').returnType
            if returnType in ['int', 'float']:
                if type == 'char':
                    raise Exception("Semantic Error: Variable " + currentNode.name.value + " is of type " + returnType + ' but it should be of type char.')
            elif returnType == 'char':
                if type in ['int', 'float']:
                    raise Exception("Semantic Error: Variable " + currentNode.name.value + " is of type " + returnType + ' but it should be of type int or float.')
            elif returnType == 'void':
                raise Exception("Semantic Error:")

        elif isinstance(currentNode, ConstNode):            # CONSTANTS (int, float, char)
            if currentNode.type in ['int', 'float']:
                if type == 'char':
                    raise Exception('Semantic Error: Assignment of a variable of type char to a constant of type int or float.')
            elif currentNode.type == 'char':
                if type in ['int', 'float']:
                    raise Exception('Semantic Error: Assignment of a variable of type ' + type + ' to a constant of type char.')
                
        else:
            for child in currentNode.children:
                self.analizeRHS(child, type)

    # ANALIZE AN FUNCTION CALL IN THE CURRENT SCOPE
    def analizeFuncCall(self, node): 
        #CHECK EXISTENCE
        self.checkExistence(node.name.value, 'function')

        element = self.currentScope.getElement(node.name.value, 'function') 
        #CHECK PARAMETERS
        ## CHECK NUMBER OF PARAMETERS
        if not len(element.arguments) == len(node.parameters.children):
            raise Exception("Semantic Error: Function " + node.name.value + " expects " + str(len(element.arguments)) + ' parameters but ' + 
                str(len(node.parameters.children)) + ' parameters were given.')

        ## CHECK TYPES OF PARAMETERS
        for i in range(len(element.arguments)):
            argument = element.arguments[i]
            parameter = node.parameters.children[i]
            self.analizeRHS(parameter, argument.type)

    #CHECKS OF A VARIABLE OR FUNCTION EXISTS IN THE CURRENT SCOPE
    def checkExistence(self, name, type):
        if not self.currentScope.isInScope(name, type):
            if type == 'function':
                raise Exception("Semantic Error: Function " + name + " doesn't exist in the current scope.")
            else:
                raise Exception("Semantic Error: Variable " + name + " doesn't exist in the current scope.")

    #CHECKS OF A VARIABLE OR FUNCTION DOESNT EXISTS IN THE CURRENT SCOPE
    def checkNotExistence(self, name, type):
        if self.currentScope.isInScope(name, type):
            if type == 'function':
                raise Exception("Semantic Error: Function " + name + " already exists in the current scope.")
            else:
                raise Exception("Semantic Error: Variable " + name + " already exist in the current scope.") 
    
    #CHECKS OF A VARIABLE OR FUNCTION IS INITIALIZED
    def checkInit(self, name, type):
        element = self.currentScope.getElement(name, type)
        if not element.init:
            raise Exception("Semantic Error: Variable " + name + " isn't initialized.")
  
    def analizeCondition(self, node):
        leftOp = node.comparison.leftOp
        rightOp = node.comparison.rightOp
        
        #CHECK IF ITS A CHARACTERS COMPARISON
        if isinstance(leftOp, ConstNode):
            if leftOp.type == 'char':
                self.analizeRHS(rightOp, 'char')

            elif leftOp.type in ['int','float']:
                self.analizeRHS(rightOp, 'int')

        elif isinstance(leftOp, VarNode):
            element = self.currentScope.getElement(leftOp.value, 'variable')
            if not element:
                raise Exception('Semantic Error')
            self.analizeRHS(rightOp, element.type)

        elif isinstance(leftOp, FuncCallNode):
            element = self.currentScope.getElement(leftOp.name.value, 'function')
            if not element:
                raise Exception('Semantic Error')
            self.analizeRHS(rightOp, element.returnType)
        else:
            self.analizeRHS(leftOp, 'float')
            self.analizeRHS(rightOp, 'float')


        #CHECK IF ITS A CHARACTERS COMPARISON
        if isinstance(rightOp, ConstNode):
            if rightOp.type == 'char':
                self.analizeRHS(leftOp, 'char')

            elif rightOp.type in ['int','float']:
                self.analizeRHS(leftOp, 'int')

        elif isinstance(rightOp, VarNode):
            element = self.currentScope.getElement(rightOp.value, 'variable')
            if not element:
                raise Exception('Semantic Error')
            self.analizeRHS(leftOp, element.type)

        elif isinstance(rightOp, FuncCallNode):
            element = self.currentScope.getElement(rightOp.name.value, 'function')
            if not element:
                raise Exception('Semantic Error')
            self.analizeRHS(leftOp, element.returnType)
        else:
            self.analizeRHS(rightOp, 'float')
            self.analizeRHS(leftOp, 'float')
        
    def analizePrint(self, node):
        if node.code == "\"%s\"":
            if not isinstance(node.exp, StringNode):
                raise Exception("Semantic Error: ")
        elif node.code == "\"%f\"":
            if isinstance(node.exp, StringNode):
                raise Exception("Semantic Error")

            self.analizeRHS(node.exp, 'float')

        elif node.code == "\"%i\"":
            if isinstance(node.exp, StringNode):
                raise Exception("Semantic Error")
            self.analizeRHS(node.exp, 'int')

        elif node.code == "\"%d\"":
            if isinstance(node.exp, StringNode):
                raise Exception("Semantic Error")
            self.analizeRHS(node.exp, 'int')

        elif node.code == "\"%c\"":
            if isinstance(node.exp, StringNode):
                raise Exception("Semantic Error")
            
            self.analizeRHS(node.exp, 'char')


    