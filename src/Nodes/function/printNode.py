from .. import Node

class PrintNode(Node):
    def __init__(self, oldNode):
        Node.__init__(self,oldNode.value, oldNode.parent, oldNode.children)
        self.code = None
        self.exp = None
        self.changeParent(oldNode)
        self.changeParentOfChildren()

    def changeAttributes(self):
        self.code = self.children[0].value
        self.exp = self.children[1]
        self.children = [self.exp]
        for child in self.children:
            child.changeAttributes()