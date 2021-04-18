from .. import Node

class IncludeNode(Node):
    def __init__(self, oldNode):
        Node.__init__(self,oldNode.value, oldNode.parent, oldNode.children)
        self.changeParent(oldNode)
        self.changeParentOfChildren()

    def changeAttributes(self):
        self.value = '<studio.h>'
        for child in self.children:
            child.changeAttributes()

    def __str__ (self):
        return "Include: " + self.value