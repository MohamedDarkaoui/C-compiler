from node import Node

class DefNode(Node):
    def __init__(self, oldNode):
        Node.__init__(self,oldNode.value, oldNode.parent, oldNode.children)
        self.changeParent(oldNode)
        self.changeParentOfChildren()
        self.const = None
        self.type = None
        self.var = None
        self.rvalue = None
    
    def changeAttributes(self):
        self.const = len(self.children) == 4
        self.rvalue = self.children[-1]
        self.var = self.children[-2]
        self.type = self.children[-3]
        if self.const:
            self.children.pop(0)
        for child in self.children:
            child.changeAttributes()