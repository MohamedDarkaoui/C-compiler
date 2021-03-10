
class cst:
    def __init__(self, root):
        self.root = root
        self.current = self.root
        self.count = 0

    def dot(self):
        dot = 'digraph G {\n'
        dot += self.generateDot()
        dot += "}"
        return dot
    
    def generateDot(self):
        
        parent = self.current
        dot = ''
        if parent.getChildCount() > 0:
            for child in parent.getChildren():
                dot += '"'
                dot += str(parent.getText())
                dot += '"'
                dot += '->' + '[label = ' + str(self.count) + ']'
                self.count +=1 
                dot += '"'
                dot += str(child.getText())
                dot += '"'
                dot += '\n'
                self.current = child
                dot += self.generateDot()

        return dot
