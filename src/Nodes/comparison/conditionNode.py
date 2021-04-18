from .. import Node

class ConditionNode(Node):
    def __init__(self, oldNode):
        Node.__init__(self,oldNode.value, oldNode.parent, oldNode.children)
        self.changeParent(oldNode)
        self.changeParentOfChildren()
        self.comparison = None
    
    def changeAttributes(self):
        self.comparison = self.children[0]
        for child in self.children:
            child.changeAttributes()