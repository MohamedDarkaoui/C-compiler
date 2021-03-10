
class ast_node:
    def __init__(self, content=None, children = None):
        self.content = content
        if children == None:
            self.children = []
        else:
            self.children = children


class ast:
    def __init__(self):
        self.root = None

