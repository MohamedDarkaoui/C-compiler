from src.AST.AST import AST
from src.Nodes import *


class ASTCreator:
    def __init__(self, tree, queue):
        self.tree = tree
        self.currentTreeNode = self.tree
        self.queue = queue
        self.queue_number = 0


    def generateAST(self):
        """ 
        This function first generates an cst and then transforms it into an AST.
        """
        root = Node(self.queue[0])
        self.queue_number+=1
        #GENERATES CST
        self.generateCST(root)
        #GENERATES AST
        for i in range(4):
            self.fixNode(root, i)
        #SWITCHS NODES
        self.changeNode(root)
        #SET ATTRIBUTES
        root.changeAttributes()

        #SYMBOL TABLE
        #CREATE SYMBOL TABLE
        ###MORE CODE

        #CONSTANT FOLDING
        root.constantFolding()
        #RESET ASTCREATOR
        self.currentTreeNode = self.tree
        self.queue_number = 0
        
        #RETURN AN AST WITH root AS ROOT
        return AST(root)

    def generateCST(self, currentNode):
        """
        Recursion function that generates the cst
        """
        parent = self.currentTreeNode
        if parent.getChildCount() > 0:
            for child in parent.getChildren():
                newChild = Node(child.getText(), currentNode)
                if child.getChildCount() > 0:
                    newChild = Node(self.queue[self.queue_number], currentNode)
                    self.queue_number += 1
                currentNode.addChild(newChild)
                self.currentTreeNode = child
                self.generateCST(newChild)

    def fixNode(self, currentNode, fixNumber):
        """ 
        This function removes the unnecessary nodes and gives a beter structure to
        the tree so it becomes an AST
        """

        #REMOVE USELESS NODES
        if fixNumber == 0:
            uselessNodes = ['(', ')', ';', '=', '<EOF>', '{', '}', 'if', 'else', 'while']
            for child in currentNode.children:
                if child.value in uselessNodes:
                    currentNode.children.remove(child)
                    self.fixNode(currentNode, fixNumber)

        #FIX OPERATOR ALS ROOT
        elif fixNumber == 1:
            operators = ['+', '-', '/', '*', '%', '==', '!=', '>', '>=', '<', '<=']
            if len(currentNode.children) == 3:
                if currentNode.children[1].value in operators:
                    currentNode.value = currentNode.children[1].value
                    del currentNode.children[1]

        #REMOVE A_EXPR, EXP AND STATEMENT NODES     
        elif fixNumber == 2:
            for child in currentNode.children:
                if child.value == "A_EXP" or child.value == "STATEMENT" or child.value == "EXP":
                    index = currentNode.children.index(child)
                    child.children[0].parent = currentNode
                    currentNode.children[index] = child.children[0]
                    self.fixNode(currentNode, fixNumber)
        
        #FIX INTEGERS AND FLOATS
        elif fixNumber == 3:
            if currentNode.value == "INT" or currentNode.value == "FLOAT":
                value = ""
                for child in currentNode.children:
                    value += child.value
                currentNode.children = [currentNode.children[0]]
                currentNode.children[0].value = value
                
        for child in currentNode.children:
            self.fixNode(child, fixNumber)

        
    def changeNode(self, currentNode):
        """
        Recursion function that replaces the nodes in the AST with the corresponding node object.
        """
        constTypes = ['INT', 'FLOAT', 'CHAR']

        if currentNode.value == "ASSIGN":
            AssignNode(currentNode)

        elif currentNode.value == "DEF":
            DefNode(currentNode)
        
        elif currentNode.value == "DEC":
            DecNode(currentNode)
        
        elif currentNode.value == "+":
            PlusNode(currentNode)
        
        elif currentNode.value == "-":
            MinusNode(currentNode)
        
        elif currentNode.value == "/":
            DivNode(currentNode)
        
        elif currentNode.value == "*":
            MulNode(currentNode)

        elif currentNode.value == "%":
            ModNode(currentNode)

        elif currentNode.value == "TYPE":
            TypeNode(currentNode)
        
        elif currentNode.value == "VAR":
            VarNode(currentNode)

        elif currentNode.value == "IF":
            IfNode(currentNode)

        elif currentNode.value == "ELSE IF":
            ElseIfNode(currentNode)

        elif currentNode.value == "ELSE":
            ElseNode(currentNode)

        elif currentNode.value == "WHILE":
            WhileNode(currentNode)
    
        elif currentNode.value == "==":
            EqNode(currentNode)

        elif currentNode.value == "!=":
            NeqNode(currentNode)
        
        elif currentNode.value == ">":
            GtNode(currentNode)
        
        elif currentNode.value == ">=":
            GetNode(currentNode)
        
        elif currentNode.value == "<":
            StNode(currentNode)
        
        elif currentNode.value == "<=":
            SetNode(currentNode)

        elif currentNode.value == "SELECT":
            SelectNode(currentNode)
        
        elif currentNode.value in constTypes:
            ConstNode(currentNode)

        for child in currentNode.children:
            self.changeNode(child)
            