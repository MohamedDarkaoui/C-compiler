from .. import Node

class VarNode(Node):
    def __init__(self, oldNode):
        Node.__init__(self, oldNode.value, oldNode.parent, oldNode.children)
        self.changeParent(oldNode)
        self.changeParentOfChildren()
        self.var = None
    
    def changeAttributes(self):
        self.value = self.children[0].value
        self.children = []
        for child in self.children:
            child.changeAttributes()

    def __str__ (self):
        
        return "Name: " + self.value if self.parent.value == 'FUNC_DEC' or self.parent.value == 'FUNC_DEF' or self.parent.value == 'FUNC_CALL' else 'Var: ' + self.value

    def findVariable(self):
        return True