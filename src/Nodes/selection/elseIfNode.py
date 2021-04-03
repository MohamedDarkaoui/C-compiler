from .. import Node


class ElseIfNode(Node):
    def __init__(self, oldNode):
        Node.__init__(self,oldNode.value, oldNode.parent, oldNode.children)
        self.changeParent(oldNode)
        self.changeParentOfChildren()
        self.condition = None
        self.block = None

    def changeAttributes(self):
        self.condition = self.children[0]
        self.block = self.children[1]
        for child in self.children:
            child.changeAttributes()