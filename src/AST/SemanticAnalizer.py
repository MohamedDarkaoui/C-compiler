from ..symbolTable import *
from src.Nodes import *

class SemanticAnalizer:
    def __init__(self, root):
        self.root = root
        self.currentScope = None

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
            self.currentScope = global_scope()
            oldScope = self.currentScope
        
        elif isinstance(currentNode, DecNode):
            #CHECK IF VARIABLE DOESNT ALREADY EXIST IN THE CURRENTSCOPE
            if self.currentScope.isInScope(currentNode.var.value):
                raise Exception("Semantic Error: Variable " + currentNode.var.value + " already exists in the current scope.")

            #ADD UNINITIALIZED VARIABLE TO CURRENTSCOPE
            newVariable = variable(node=currentNode.var, type=currentNode.type, init=False, const=False)
            self.currentScope.addElement(newVariable)

        elif isinstance(currentNode, DefNode):
            #CHECK IF VARIABLE DOESNT ALREADY EXIST IN THE CURRENTSCOPE
            if self.currentScope.isInScope(currentNode.var.value):
                raise Exception("Semantic Error: Variable " + currentNode.var.value + " already exists in the current scope.")

            #CHECK THAT THE RVALUE OF TYPE LVALUE IS 
            #SKIP FOR NOW

            #ADD INITIALIZED VARIABLE TO CURRENTSCOPE
            newVariable = variable(node=currentNode.var, type=currentNode.type, init=True, const=currentNode.const)
            self.currentScope.addElement(newVariable)
            
        elif isinstance(currentNode, AssignNode):
            #CHECK THAT THE VARIABLE EXISTS IN THE CURRENT SCOPE
            if not self.currentScope.isInScope(currentNode.var.value):
                raise Exception("Semantic Error: Variable " + currentNode.var.value + " doesn't exist in the current scope.")

            #CHECK THAT THE VARIABLE ISNT CONSTANT
            if self.currentScope.getElement(currentNode.var.value).const:
                raise Exception("Semantic Error: Variable " + currentNode.var.value + " is constant so its value cannot be changed.")

            #CHECK THAT THE RVALUE OF TYPE LVALUE IS 
            #SKIP FOR NOW

            #INITIALIZE VARIABLE IF ITS NOT INITIALIZED
            self.currentScope.getElement(currentNode.var.value).init = True
        
        elif isinstance(currentNode, FuncDecNode):
            returnType = currentNode.type.value
            name = currentNode.name.value
            arguments = []
            for declaration in currentNode.arguments.children:
                arguments.append(argument(declaration.type.value, declaration.var.value))
            newFunction = Function(name = name, returnType = returnType, arguments = arguments, init=False)
            self.currentScope.addElement(newFunction)
            return

        elif isinstance(currentNode, FuncDefNode):
            returnType = currentNode.type.value
            name = currentNode.name.value
            arguments = []
            for declaration in currentNode.arguments.children:
                arguments.append(argument(declaration.type.value, declaration.var.value))
            newFunction = Function(name = name, returnType = returnType, arguments = arguments, init=False)
            self.currentScope.addElement(newFunction)
            self.currentScope = func_scope(self.currentScope)
            oldScope = self.currentScope

        for child in currentNode.children:
            self.analize(child)
            if oldScope is not None:
                self.currentScope = oldScope
