
class variable:
    def __init__(self, name, type, offset, isArray = False, size = None):
        self.name = name
        self.type = type
        self.offset = offset
        self.isArray = isArray
        self.size = size

class function:
    def __init__(self, name , arguments, returnType):
        self.name = name
        self.arguments = arguments
        self.returnType = returnType

class scope:
    def __init__(self, parentScope = None):
        self.parentScope = parentScope
        self.symbolTable = []
        self.offsetFree = 0
        self.registers = {}
        self.floatRegisters = {}
        self.resetRegisters()
                
    def resetRegisters(self):
        for i in range(32):
            self.floatRegisters['$f' + str(i)] = False
            if i <=9:
                self.registers['$t' + str(i)] = False
            if i <= 7:
                self.registers['$s' + str(i)] = False

    def getFreeRegister(self, float):
        if float:
            for register in self.floatRegisters:
                if not self.floatRegisters[register]:
                    self.setFloatRegister(register, True)
                    return register
        else:
            for register in self.registers:
                if not self.registers[register]:
                    self.setRegister(register, True)
                    return register

        return None

    def setRegister(self, register, used):
        self.registers[register] = used
    
    def setFloatRegister(self, register, used):
        self.floatRegisters[register] = used

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
            return self.parentScope.getElementOffSet(element) - self.parentScope.offsetFree




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
    def __init__(self, parentScope, arguments, returnType, mainScope = False):
        scope.__init__(self, parentScope)
        self.arguments = arguments
        self.returnType = returnType
        self.mainScope = mainScope

    def getAllElements(self):
        allElements = []
        for x in self.symbolTable:
            if not isinstance(x, scope):
                allElements.append(x)

        if self.parentScope is not None:
            return self.arguments + allElements + self.parentScope.getAllElements()
    
    def getElementOffSet(self, element):
        if element in self.symbolTable + self.arguments:
            return element.offset
        
        else:
            return self.parentScope.getElementOffSet(element) - self.parentScope.offsetFree