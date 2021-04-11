from .. import Node

class FuncCallNode(Node):
    def __init__(self, oldNode):
        Node.__init__(self,oldNode.value, oldNode.parent, oldNode.children)
        self.changeParent(oldNode)
        self.changeParentOfChildren()
        self.name = None
        self.parameters = None

    def changeAttributes(self):
        self.name = self.children[0]
        self.parameters = self.children[1]
        for child in self.children:
            child.changeAttributes()
    
    def findVariable(self):
        return True