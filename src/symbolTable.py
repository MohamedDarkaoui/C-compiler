


class symbolTableElement:
    def __init__(self, symbolName, _type, variableNumber):
        self.symbolName = symbolName
        self.type = _type
        self.variableNumber = variableNumber
        


class symbolTable:
    def __init__(self):
        self.table = []

    def findElement(self, name):
        for element in self.table:
            if element.symbolName == name:
                return element
        return None