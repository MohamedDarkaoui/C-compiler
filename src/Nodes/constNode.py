from node import Node

class ConstNode(Node):
    def __init__(self, oldNode):
        Node.__init__(self, oldNode.value, oldNode.parent, oldNode.children)
        self.changeParent(oldNode)
        self.changeParentOfChildren()
        self.type = self.value

    def changeAttributes(self):
        self.value = self.children[0].value
        self.children = []
        for child in self.children:
            child.changeAttributes()
    
    def __str__ (self):
        return self.type + ": " + self.value

    def constantFolding(self):
        return self.value