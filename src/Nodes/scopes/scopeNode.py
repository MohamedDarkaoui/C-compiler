from .. import Node
from .. import ProgramNode, ForNode, WhileNode, IfNode, ElseIfNode, ElseNode, FuncDefNode
class ScopeNode(Node):
    def __init__(self, oldNode):
        Node.__init__(self,oldNode.value, oldNode.parent, oldNode.children)
        self.changeParent(oldNode)
        self.changeParentOfChildren()

    def changeAttributes(self):
        if isinstance(self.parent, ProgramNode):
            self.value = 'global_scope'
        elif isinstance(self.parent, ScopeNode):
            self.value = 'unnamed_scope'
        elif isinstance(self.parent, ForNode):
            self.value = 'for_scope'
        elif isinstance(self.parent, WhileNode):
            self.value = 'while_scope'
        elif isinstance(self.parent, IfNode):
            self.value = 'if_scope'
        elif isinstance(self.parent, ElseIfNode):
            self.value = 'elif_scope'
        elif isinstance(self.parent, ElseNode):
            self.value = 'else_scope'
        elif isinstance(self.parent, FuncDefNode):
            self.value = 'func_scope'     

        for child in self.children:
            child.changeAttributes()