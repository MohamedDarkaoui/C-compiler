
class variable:
    def __init__(self, node, type, init, const, register=None):
        self.name = node.value
        self.init = init
        self.type = type
        self.const = const
        self.isArray = node.isArray
        self.size = node.size                #size of the array
        self.register = register

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

    def isInScope(self, name, type):
        allElements = self.getAllElements()

        if type == 'variable':
            for element in allElements:
                if element.name == name and isinstance(element, variable):
                    return True
        else:
            for element in allElements:
                if element.name == name and isinstance(element, Function):
                    return True

        return False

    def getElement(self, name, type):
        allElements = self.getAllElements()
        if type == 'variable':
            for element in allElements:
                if element.name == name and isinstance(element, variable):
                    return element
        else:
            for element in allElements:
                if element.name == name and isinstance(element, Function):
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
    def __init__(self, parentScope, arguments, returnType):
        scope.__init__(self, parentScope)
        self.arguments = arguments
        self.returnType = returnType
    
    def getAllElements(self):
        allElements = []
        for x in self.symbolTable:
            if not isinstance(x, scope):
                allElements.append(x)

        if self.parentScope is not None:
            return self.arguments + allElements + self.parentScope.getAllElements()