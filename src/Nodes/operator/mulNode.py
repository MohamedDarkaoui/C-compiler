from .. import Node
from .. import ConstNode

class MulNode(Node):
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
    
    def constantFolding(self):
        if self.leftOp.findVariable() or self.rightOp.findVariable():
            self.leftOp.constantFolding()
            self.rightOp.constantFolding()
        else:
            leftValue = float(self.leftOp.constantFolding())
            rightValue = float(self.rightOp.constantFolding())
            result = leftValue * rightValue
            newNode = ConstNode(self)
            newNode.value = str(result)
            newNode.type = "FLOAT"
            newNode.children = []
            
        
            
        
