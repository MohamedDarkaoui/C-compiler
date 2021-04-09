from .. import Node

class FuncDefNode(Node):
    def __init__(self, oldNode):
        Node.__init__(self,oldNode.value, oldNode.parent, oldNode.children)
        self.changeParent(oldNode)
        self.changeParentOfChildren()
        self.type = None
        self.name = None
        self.arguments = None
        self.body = None

    def changeAttributes(self):
        self.type = self.children[0]
        self.name = self.children[1]
        self.arguments = self.children[2]
        self.body = self.children[3]
        for child in self.children:
            child.changeAttributes()