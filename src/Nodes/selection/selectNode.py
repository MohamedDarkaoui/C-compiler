from .. import Node
from .. import IfNode
from .. import ElseIfNode
from .. import ElseNode
class SelectNode(Node):
    def __init__(self, oldNode):
        Node.__init__(self,oldNode.value, oldNode.parent, oldNode.children)
        self.changeParent(oldNode)
        self.changeParentOfChildren()
        self.ifStatement = None
        self.elseIfStatements = []
        self.elseStatement = None

    def changeAttributes(self):
        for child in self.children:
            if (isinstance(child, IfNode)):
                self.ifStatement = child
            elif (isinstance(child, ElseIfNode)):
                self.elseIfStatements.append(child)
            else:
                self.elseStatement = child
            child.changeAttributes()