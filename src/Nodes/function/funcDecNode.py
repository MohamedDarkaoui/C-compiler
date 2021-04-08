from .. import Node

class FuncDecNode(Node):
    def __init__(self, oldNode):
        Node.__init__(self,oldNode.value, oldNode.parent, oldNode.children)
        self.changeParent(oldNode)
        self.changeParentOfChildren()
        self.type = None
        self.name = None
        self.arguments = None
    
    def changeAttributes(self):
        self.type = self.children[0]
        self.name = self.children[1]
        if len(self.children) >= 3 is not None:
            self.arguments = self.children[2]
        for child in self.children:
            child.changeAttributes()