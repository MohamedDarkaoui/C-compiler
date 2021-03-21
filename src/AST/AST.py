import os
from src.Nodes.node import Node

class AST:
    def __init__(self, root):
        self.root = root
        self.count = 0

    def dot(self, filename):
        dot = 'digraph G {\n'
        dot += str(self.count) + '[label="' + str(self.root) + '"]\n'
        dot += self.generateDot(self.root)
        dot += "}"
        open(filename + ".dot", "w+")
        with open(filename + ".dot", 'w') as file:
            file.write(dot)
        file.close()

        os.system("dot -Tpng " + filename + ".dot > " + filename +  ".png")
        os.system("rm " + filename + ".dot") 
        

    def generateDot(self, currentNode):
        parentCount = self.count
        dot = ''
        for child in currentNode.children:
            self.count += 1
            dot += str(self.count) + '[label="' + str(child) + '"]\n'
            dot += str(parentCount) + "->" + str(self.count) + "\n"
            dot += self.generateDot(child)
    
        return dot
    
"""
class variable:
    def __init__(self, Const, Init, Name, Type, Pointer=False):
        self.const = Const
        self.init = Init
        self.name = Name
        self.type = Type
        self.pointer = Pointer
"""

