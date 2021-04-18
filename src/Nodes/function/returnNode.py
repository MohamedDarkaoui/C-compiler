from .. import Node

class ReturnNode(Node):
    def __init__(self, oldNode):
        Node.__init__(self,oldNode.value, oldNode.parent, oldNode.children)
        self.changeParent(oldNode)
        self.changeParentOfChildren()
        self.returnExp = None

    def changeAttributes(self):
        if len(self.children) > 0:
            self.returnExp = self.children[0]

        index = self.parent.children.index(self)
        self.parent.children = self.parent.children[:index+1]

        for child in self.children:
            child.changeAttributes()