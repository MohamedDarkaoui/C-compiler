from node import Node

class AssignNode(Node):
    def __init__(self, oldNode):
        Node.__init__(self,oldNode.value, oldNode.parent, oldNode.children)
        self.changeParent(oldNode)
        self.changeParentOfChildren()
        self.var = None
        self.rvalue = None

    def changeAttributes(self):
        self.var = self.children[0]
        self.rvalue = self.children[1]
        for child in self.children:
            child.changeAttributes()