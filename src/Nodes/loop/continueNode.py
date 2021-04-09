from .. import Node

class ContinueNode(Node):
    def __init__(self, oldNode):
        Node.__init__(self,oldNode.value, oldNode.parent, oldNode.children)
        self.changeParent(oldNode)
        self.changeParentOfChildren()

    def changeAttributes(self):
        self.children = []
        for child in self.children:
            child.changeAttributes()