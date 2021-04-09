from .. import Node

class ArgNode(Node):
    def __init__(self, oldNode):
        Node.__init__(self,oldNode.value, oldNode.parent, oldNode.children)
        self.changeParent(oldNode)
        self.changeParentOfChildren()
        self.type = None
        self.var = None

    def changeAttributes(self):
        self.type = self.children[0]
        self.var = self.children[1]
        for child in self.children:
            child.changeAttributes()