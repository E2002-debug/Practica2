from controls.tda.stack.stackOperation import StackOperation

class Stack():
    
    def __init__(self, tope ):

        self.tope = StackOperation._tope 
        self.__stack = StackOperation(self.tope)

    def push(self, data):    
        self.__stack.push(data)

    def pop(self):
        return self.__stack.pop

    def print(self):
        self.__stack.print

    def verify(self):
        return self.__stack.verifyTop        