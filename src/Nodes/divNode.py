from node import Node

class DivNode(Node):
    def __init__(self, oldNode):
        Node.__init__(self,oldNode.value, oldNode.parent, oldNode.children)
        self.changeParent(oldNode)
        self.changeParentOfChildren()
        self.leftOp = None
        self.rightOp = None
    
    def changeAttributes(self):
        self.leftOp = self.children[0]
        self.rightOp = self.children[1]
        for child in self.children:
            child.changeAttributes()