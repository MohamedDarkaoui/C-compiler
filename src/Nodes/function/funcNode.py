from .. import Node

class FuncNode(Node):
    def __init__(self, oldNode):
        Node.__init__(self,oldNode.value, oldNode.parent, oldNode.children)
        self.changeParent(oldNode)
        self.changeParentOfChildren()
        self.parameters = None
        self.body = None
    
    def changeAttributes(self):
        self.parameters = self.children[0]
        self.body = self.children[1]
        for child in self.children:
            child.changeAttributes()