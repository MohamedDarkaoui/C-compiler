from .. import Node

class VarNode(Node):
    def __init__(self, oldNode):
        Node.__init__(self, oldNode.value, oldNode.parent, oldNode.children)
        self.changeParent(oldNode)
        self.changeParentOfChildren()
        self.var = None
    
    def changeAttributes(self):
        self.value = self.children[0].value
        self.children = []
        for child in self.children:
            child.changeAttributes()

    def __str__ (self):
        return "Var: " + self.value

    def findVariable(self):
        return True