class Node:
    def __init__(self, value, parent = None, children=None):
        self.value = value
        self.parent = parent
        self.children = children
        if not children:
            self.children = []
        
    def addChild(self, child):
        self.children.append(child)

    def changeParent(self, oldNode):
        index  = self.parent.children.index(oldNode)
        self.parent.children[index] = self

    def changeParentOfChildren(self):
        for child in self.children:
            child.parent = self

    def changeAttributes(self):
        for child in self.children:
            child.changeAttributes()
    
    def constantFolding(self):
        for child in self.children:
            child.constantFolding()

    def __str__ (self):
        return self.value
    
    def findVariable(self):
        for child in self.children:
            return child.findVariable()