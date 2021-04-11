"""
example: 

int a = 3;
if (x > 2) {
    int b = 3;
}
char b = 'b'
{
    float c;
}
=====>

global_scope:
    variable: a
    if_scope:
        variable: b    
    variable: b
    unnamed_scope:
        variable: c
"""





class argument:
    def __init__(self, type, name):
        self.type = type
        self.name = name


class variable:
    def __init__(self, node, type, init, const):
        self.name = node.value
        self.init = init
        self.type = type
        self.const = const
        self.isArray = node.isArray
        self.size = node.size                #size of the array

class Function:
    def __init__(self, name, init, arguments, returnType):
        self.name = name
        self.init = init
        self.arguments = arguments
        self.returnType = returnType
        
class scope:
    def __init__(self, parentScope = None):
        self.parentScope = parentScope
        self.symbolTable = []

    def addElement(self, element):
        self.symbolTable.append(element)
    
    def getAllElements(self):
        allElements = []
        for x in self.symbolTable:
            if not isinstance(x, scope):
                allElements.append(x)

        if self.parentScope is not None:
            return allElements + self.parentScope.getAllElements()

        return allElements

    def isInScope(self, name):
        allElements = self.getAllElements()

        for element in allElements:
            if element.name == name:
                return True
                
        return False

    def getElement(self, name):
        allElements = self.getAllElements()

        for element in allElements:
            if element.name == name:
                return element

        return None


class unnamed_scope(scope):
    def __init__(self, parentScope):
        scope.__init__(self, parentScope)

class global_scope(scope):
    def __init__(self):
        scope.__init__(self)

class for_scope(scope):
    def __init__(self, parentScope):
        scope.__init__(self, parentScope)
    
class while_scope(scope):
    def __init__(self, parentScope):
        scope.__init__(self, parentScope)
    
class if_scope(scope):
    def __init__(self, parentScope):
        scope.__init__(self, parentScope)
    
class elif_scope(scope):
    def __init__(self, parentScope):
        scope.__init__(self, parentScope)
    
class else_scope(scope):
    def __init__(self, parentScope):
        scope.__init__(self, parentScope)

class func_scope(scope):
    def __init__(self, parentScope):
        scope.__init__(self, parentScope)