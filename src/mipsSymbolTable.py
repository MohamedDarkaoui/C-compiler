
class variable:
    def __init__(self, name, type, offset):
        self.name = name
        self.type = type
        self.offset = offset

class function:
    def __init__(self):
        self.name = None
        self.arguments = None

class scope:
    def __init__(self, parentScope = None):
        self.parentScope = parentScope
        self.symbolTable = []
        self.offsetFree = 4
        self.offsetParent = None

    def addElement(self, element):
        self.symbolTable.append(element)

    def getFreeSpace(self):
        self.offsetFree += 4
        return self.offsetFree - 4
    
    def getAllElements(self):
        allElements = []
        for x in self.symbolTable:
            if not isinstance(x, scope):
                allElements.append(x)

        if self.parentScope is not None:
            return allElements + self.parentScope.getAllElements()

        return allElements

    def findElement(self, name, type):
        allElements = self.getAllElements()
        if type == 'variable':
            for element in allElements:
                if element.name == name and isinstance(element, variable):
                    return element
        else:
            for element in allElements:
                if element.name == name and isinstance(element, function):
                    return element
        return None

    def getElementOffSet(self, element):
        if element in self.symbolTable:
            return element.offset
        
        else:
            return self.parentScope.getElementOffSet(self, element) - self.offsetParent




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
