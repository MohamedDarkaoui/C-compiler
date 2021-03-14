import os

class AST_Node:
    def __init__(self, value, parent, ctx=None):
        self.value = value
        self.parent = parent
        self.ctx = ctx
        self.children = []

    def addChild(self, child):
        self.children.append(child)


class AST:
    def __init__(self, root):
        self.root = root
        self.count = 0

    def dot(self, filename):
        dot = 'digraph G {\n'
        dot += str(self.count) + '[label="' + self.root.value + '"]\n'
        dot += self.generateDot(self.root)
        dot += "}"
        open(filename + ".dot", "w+")
        with open(filename + ".dot", 'w') as file:
            file.write(dot)
        file.close()

        os.system("dot -Tpng " + filename + ".dot > " + filename +  ".png")
        os.system("rm " + filename + ".dot") 
        

    def generateDot(self, currentNode):
        parentCount = self.count
        dot = ''
        for child in currentNode.children:
            self.count += 1
            dot += str(self.count) + '[label="' + child.value + '"]\n'
            dot += str(parentCount) + "->" + str(self.count) + "\n"
            dot += self.generateDot(child)
    
        return dot
    

class variable:
    def __init__(self, Const, Init, Name, Type, Pointer=False):
        self.const = Const
        self.init = Init
        self.name = Name
        self.type = Type
        self.pointer = Pointer

class ASTCreator:
    def __init__(self, tree, queue):
        self.tree = tree
        self.currentTreeNode = self.tree
        self.queue = queue
        self.queue_number = 0
        self.scope = []


    def generateTree(self):
        root = AST_Node(self.queue[0][0], self.queue[0][1])
        self.queue_number+=1
        self.generateTreeBody(root)
        for i in range(4):
            self.fixNode(root, i)
        self.semanticsAnalizer(root)

        self.constantFolding(root)
        return AST(root)

    def generateTreeBody(self, currentNode):
        parent = self.currentTreeNode
        if parent.getChildCount() > 0:
            for child in parent.getChildren():
                newChild = AST_Node(child.getText(), currentNode)
                if child.getChildCount() > 0:
                    newChild = AST_Node(self.queue[self.queue_number][0], currentNode,self.queue[self.queue_number][1])
                    self.queue_number += 1
                currentNode.addChild(newChild)
                self.currentTreeNode = child
                self.generateTreeBody(newChild)

    def fixNode(self, currentNode, fixNumber):
        #FIX USELESS NODES
        if fixNumber == 0:
            uselessNodes = ['(', ')', ';', '=']
            for child in currentNode.children:
                if child.value in uselessNodes:
                    currentNode.children.remove(child)

        #FIX A_EXPR -> A_EXPR        
        elif fixNumber == 1:
            if currentNode.value == 'A_EXP' and len(currentNode.children) == 1:
                if currentNode.children[0].value == 'A_EXP':
                    currentNode.children = currentNode.children[0].children
                    for child in currentNode.children:
                        child.parent = currentNode
            
        #FIX OPERATOR ALS ROOT
        elif fixNumber == 2:
            operators = ['+', '-', '/', '*', '%']
            if len(currentNode.children) == 3:
                if currentNode.children[1].value in operators:
                    currentNode.value = currentNode.children[1].value
                    currentNode.ctx = currentNode.children[1].ctx
                    del currentNode.children[1]

        #FIX INTEGERS AND FLOATS
        elif fixNumber == 3:
            if currentNode.value == "INT" or currentNode.value == "FLOAT":
                value = ""
                for child in currentNode.children:
                    value += child.value
                currentNode.children = [currentNode.children[0]]
                currentNode.children[0].value = value
                currentNode.children[0].ctx = None

        for child in currentNode.children:
            self.fixNode(child, fixNumber)

    def getScope(self, scopes):
        """
        turns a nested list into one big list 
        """
        returnlist = []
        for item in scopes:
            if not isinstance(item,list):
                returnlist.append(item)
            else:
                returnlist += self.getScope(item)

        return returnlist



    def constantFolding(self, currentNode):
        operators = ['+', '-', '/', '*', '%']
        if currentNode.value in operators:
            if not self.getAllVariables(currentNode.children[0]) and not self.getAllVariables(currentNode.children[1]):
                result = 0
                result1 = float(self.constantFolding(currentNode.children[0]))
                result2 = float(self.constantFolding(currentNode.children[1]))
                if currentNode.value == '+':
                    result = result1 + result2
                elif currentNode.value == '-':
                    result = result1 - result2
                elif currentNode.value == '/':
                    result = result1 / result2
                elif currentNode.value == '*':
                    result = result1 * result2  
                else:
                    result = result1 % result2
                currentNode.value = "A_EXP"
                currentNode.children = [AST_Node('FLOAT', currentNode)]
                currentNode.children[0].children = [AST_Node(str(result), currentNode.children[0])]
                return result   
            else:
                self.constantFolding(currentNode.children[0])
                self.constantFolding(currentNode.children[1])
        elif currentNode.value == 'A_EXP':
            return currentNode.children[0].children[0].value
        else:
            for child in currentNode.children:
                self.constantFolding(child)                

    def semanticsAnalizer(self, currentNode):
        if currentNode.value == "DEC":
            #CHECK VARIABLE DOESNT EXIST ALREADY IN THE SCOPE
            self.declaration_analyser(currentNode)

        elif currentNode.value == "DEF":
            #CHECK VARIABLE DOESNT EXIST ALREADY IN THE SCOPE
            #CHECK RVALUE HAS THE SAME TYPE AS THE TYPE OF THE VARIABLE
            #CHECK Use of an undefined or uninitialized variable in the RVALUE of the assignment
            self.definition_analyser(currentNode)
            

        elif currentNode.value == "ASSIGN":
            #CHECK VARIABLE ALREADY EXISTS IN THE SCOPE
            #CHECK RVALUE HAS THE SAME TYPE AS THE TYPE OF THE VARIABLE
            #CHECK Use of an undefined or uninitialized variable in the RVALUE of the assignment
            #CHECK VARIABLE IS NOT CONST
            self.assignment_analyser(currentNode)

        else:
            for child in currentNode.children:
                self.semanticsAnalizer(child)

    def declaration_analyser(self, node):
        """
        analyses the declarion statements and throws semantic exceptions when needed
        """
        currentScope = self.getScope(self.scope)
        _type = ""
        name = ""
        for child in node.children:
            if child.value == "TYPE":
                _type = child.children[0].value
            elif child.value == "VAR":
                name = child.children[0].value
        
        for var in currentScope:
            if var.name == name:
                raise Exception("[Semantic Error] Variable " + name + " is already declared")

        newVar = variable(False, False, name, _type)
        self.scope.append(newVar)



    def definition_analyser(self, node):
        """
        analyses the definition statements and throws semantic exceptions when needed
        """

        _type, name, cst = '','', False
        currentScope = self.getScope(self.scope)

        #GET INFO OVER VARIABLE
        for child in node.children:
            if child.value == 'TYPE':
                _type = child.children[0].value
            elif child.value == 'VAR':
                name = child.children[0].value
            elif child.value == 'const':
                cst = True

        #GET RIGHTVALUE
        exp = node.children[-1]

        #CHECK IF VARIABLE DOESNT EXISTS IN THE SCOPE
        for var in currentScope:
            if var.name == name:
                    raise Exception("[Semantic Error] Variable " + name + " is already declared")

        #CHECK RVALUE HAS THE SAME TYPE AS THE TYPE OF THE VARIABLE
        if (_type == "int" or _type == "float") and exp.children[0].value == "CHAR":
            raise Exception("[Semantic Error] Variable " + name + " is of type " + _type + " but his rvalue is of type char.")
        elif (_type == "char") and not exp.children[0].value == "CHAR":
            raise Exception("[Semantic Error] Variable " + name + " is of type " + _type + " but his rvalue is of type int or float.")
        
        #CHECK Use of an undefined or uninitialized variable in the RVALUE of the assignment
        usedVariables =  self.getAllVariables(exp)
        for var in usedVariables:
            checkDef = False
            for var2 in currentScope:
                if var == var2.name:
                    checkDef = True
                    #CHECK INITIALIZED
                    if not var2.init:
                        raise Exception("[Semantic Error] Variable " + var + " is not initialized.")
            #CHECK DEFINED        
            if not checkDef:
                raise Exception("[Semantic Error] Variable " + var + " is not defined.")

        self.scope.append(variable(cst, True, name, _type))

    def assignment_analyser(self, node):
        currentScope = self.getScope(self.scope)
        name = ""
        _type = ""
        for child in node.children:
            if child.value == 'VAR':
                name = child.children[0].value
        exp = node.children[-1]

        #FIND VARIABLE IN SCOPE AND CHECK THAT IT IS NOT A CONST VARIABLE
        check = False
        usedVar = None
        for var in currentScope:
            if var.name == name:
                _type = var.type
                check = True
                usedVar = var
                #CHECK THE VARIABLE IS NOT CONST
                if var.const:
                    raise Exception("[Semantic Error] Variable " + name + " is constant so its value cannot be changed.")
                break
        #CHECK VARIABLE EXISTS IN THE SCOPE
        if not check:
            raise Exception("[Semantic Error] Variable " + name + " doesnt exist in the scope.")


        #CHECK RVALUE HAS THE SAME TYPE AS THE TYPE OF THE VARIABLE
        if (_type == "int" or _type == "float") and exp.children[0].value == "CHAR":
            raise Exception("[Semantic Error] Variable " + name + " is of type " + _type + " but his rvalue is of type char.")
        elif (_type == "char") and not exp.children[0].value == "CHAR":
            raise Exception("[Semantic Error] Variable " + name + " is of type " + _type + " but his rvalue is of type int or float.")
        
        #CHECK Use of an undefined or uninitialized variable in the RVALUE of the assignment
        usedVariables =  self.getAllVariables(exp)
        for var in usedVariables:
            checkDef = False
            for var2 in currentScope:
                if var == var2.name:
                    checkDef = True
                    #CHECK INITIALIZED
                    if not var2.init:
                        raise Exception("[Semantic Error] Variable " + var + " is not initialized.")
            #CHECK DEFINED        
            if not checkDef:
                raise Exception("[Semantic Error] Variable " + var + " is not defined.")
        
        #SET THE VARIABLE TO INITIALIZED IF IT ISNT
        if not usedVar.init:
            usedVar.init = True        



    #FUNCTION THAT RETURNS ALL VARIABLES USED IN A SUBTREE
    def getAllVariables(self, currentNode):
        variables = []
        if currentNode.value == "VAR":
            variables.append(currentNode.children[0].value)
        else:
            for child in currentNode.children:
                variables += self.getAllVariables(child)
        return variables
