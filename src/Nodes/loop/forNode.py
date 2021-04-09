from .. import Node

class ForNode(Node):
    def __init__(self, oldNode):
        Node.__init__(self,oldNode.value, oldNode.parent, oldNode.children)
        self.changeParent(oldNode)
        self.changeParentOfChildren()
        self.initiator = None
        self.condition = None
        self.increment = None
        self.block = None

    def changeAttributes(self):
        self.initiator = self.children[0]
        self.condition = self.children[1]
        self.increment = self.children[2]
        self.block = self.children[3]
        for child in self.children:
            child.changeAttributes()