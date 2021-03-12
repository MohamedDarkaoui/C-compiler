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


class ASTCreator:
    def __init__(self, tree, queue):
        self.tree = tree
        self.currentTreeNode = self.tree
        self.queue = queue
        self.queue_number = 0

    def generateTree(self):
        root = AST_Node(self.queue[0][0], self.queue[0][1])
        self.queue_number+=1
        self.generateTreeBody(root)
        for i in range(3):
            self.fixNode(root, i)
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
        if fixNumber == 0:
            if currentNode.value == '(' or currentNode.value == ')' or currentNode.value == ';':
                currentNode.parent.children.remove(currentNode)
        elif fixNumber == 1:
            if currentNode.value == 'arithmetic_expression' and currentNode.parent.value == 'arithmetic_expression' and len(currentNode.parent.children) == 1:
                index = currentNode.parent.parent.children.index(currentNode.parent)
                currentNode.parent = currentNode.parent.parent
                currentNode.parent.children[index] = currentNode
        elif fixNumber == 2:
            operators = ['+', '-', '/', '*', '%']
            if len(currentNode.children) == 3:
                if currentNode.children[1].value in operators:
                    currentNode.value = currentNode.children[1].value
                    currentNode.ctx = currentNode.children[1].ctx
                    del currentNode.children[1]

        for child in currentNode.children:
            self.fixNode(child, fixNumber)
