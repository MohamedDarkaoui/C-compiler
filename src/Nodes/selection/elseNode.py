from .. import Node

class ElseNode(Node):
    def __init__(self, oldNode):
        Node.__init__(self,oldNode.value, oldNode.parent, oldNode.children)
        self.changeParent(oldNode)
        self.changeParentOfChildren()
        self.block = None

    def changeAttributes(self):
        self.block = self.children[0]
        for child in self.children:
            child.changeAttributes()