import json
from controls.tda.linked.linkedList import Linked_List
from controls.exception.linkedEmpty import LinkedEmpty

class StackOperation(Linked_List):
    def __init__(self, tope=20):  # Establecer el límite predeterminado a 20
        super().__init__()
        self.__tope = tope

    @property
    def _tope(self):
        return self.__tope

    @_tope.setter
    def _tope(self, value):
        self.__tope = value

    @property
    def verifyTop(self):
        return self._length <= self.__tope

    def push(self, data):
        if self._length < self.__tope:
            self.add(data)
        else:
            self.delete(0)  # Eliminar el primer elemento
            self.add(data)

    @property    
    def pop(self):
        if self.isEmpty:
            raise LinkedEmpty("Stack empty")
        else:
            return self.delete()
        
    def __iter__(self):
        current = self._head
        while current is not None:
            yield current._data
            current = current._next   
        
    def to_json(self, file_path=None):
        stack_list = [self.get(i) for i in range(self._length)]
        
        json_data = json.dumps(stack_list)
        
        if file_path is None:
            file_path = r"C:\Users\USUARIO_PC\Escritorio\ProyectosEstructura3\Practica1\Practica1\data\stack_data.json"
        
        with open(file_path, "w") as file:
            file.write(json_data)

        print("JSON guardado en", file_path)
        return stack_list
    
    @staticmethod
    def from_json(file_path):
        try:
            with open(file_path, "r") as file:
                json_data = file.read()
            stack_list = json.loads(json_data)
            stack_operation = StackOperation()
            for data in stack_list:
                stack_operation.push(data)
            return stack_operation
        except FileNotFoundError:
            return StackOperation()
        except Exception as e:
            raise e
