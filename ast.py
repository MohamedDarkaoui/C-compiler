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
    def __init__(self, Const, Init, Name, Type):
        self.const = Const
        self.init = Init
        self.name = Name
        self.type = Type


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


    def semanticsAnalizer(self, currentNode):
        if currentNode.value == "DEC":
            currentScope = self.getScope(self.scope)
            _type = ""
            name = ""
            for child in currentNode.children:
                if child.value == "TYPE":
                    _type = child.children[0].value
                elif child.value == "VAR":
                    name = child.children[0].value
            
            for var in currentScope:
                if var.name == name:
                    raise Exception("Variable " + name + " is already declared")

            newVar = variable(False, False, name, _type)
            self.scope.append(newVar)

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
            pass

        else:
            for child in currentNode.children:
                self.semanticsAnalizer(child)

    def definition_analyser(self, node):
        """
        analyses the definition statements and throws semantic exceptions when needed
        """
        
        types = { # move to self.types or give as a parameter?
            'int' : 'INT',
            'float' : 'FLOAT',
            'char' : 'CHAR'
        }

        scope = self.getScope(self.scope)
        _type, name, cst = '','', False
        
        for child in node.children:
            if child.value == 'TYPE':
                _type = child.children[0].value
            elif child.value == 'VAR':
                name = child.children[0].value
            elif child.value == 'const':
                cst = True

        exp = node.children[-1]
        # int a = b
        if exp.children[0].children[0].value == 'VAR':
            variable_name = exp.children[0].children[0].children[0].value
            var = None
            for element in scope:
                if element.name == variable_name:
                    var = element
            # b is niet gedefinieerd in de scope
            if var == None:
                raise Exception ('Variable ' + variable_name + ' is not defined')
            # a en b hebben niet dezelfde type
            elif var.type != _type:
                raise Exception ('Variable ' + name + ' does not have type ' + var.type)

        # int a = 5
        else:
            #voor int, float is er een A_EXP node meer dan bij char 
            if not types[_type] == exp.children[0].value and not types[_type] == exp.children[0].children[0].value:
                raise Exception("Variable " + name + " not matching type " + _type)

        for var in scope:
                if var.name == name:
                    raise Exception("Variable " + name + " is already declared")
    
        self.scope.append(variable(cst, False, name, _type))

    
    