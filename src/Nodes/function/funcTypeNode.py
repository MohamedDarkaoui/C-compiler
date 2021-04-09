from .. import Node

class FuncTypeNode(Node):
    def __init__(self, oldNode):
        Node.__init__(self,oldNode.value, oldNode.parent, oldNode.children)
        self.changeParent(oldNode)
        self.changeParentOfChildren()

    def changeAttributes(self):
        self.value = self.children[0].value
        if self.value == "TYPE":
            self.value = self.children[0].children[0].value
        self.children = []
        for child in self.children:
            child.changeAttributes()

    def __str__ (self):
        return "FType: " + self.value