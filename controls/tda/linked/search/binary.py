class Binary:
    def binary_primitive(self, array, data, low, high):
        if low > high:
            print("Valor no encontrado en la lista")
            return -1
        mid = (low + high) // 2
        if array[mid] == data:
            print(f"Valor encontrado en la posicion: {mid}")
            return mid
        elif array[mid-1] == data:
            print(f"Valor encontrado en la posicion: {mid-1}")
            return mid-1    
        elif array[mid+1] == data:
            print(f"Valor encontrado en la posicion: {mid+1}")
            return mid+1   
        elif array[mid] < data:
            return self.binary_primitive(array, data, mid + 1, high)
        else:
            return self.binary_primitive(array, data, low, mid - 1)
        
   
        
    
    def binary_string(self, array, data, low, high):
        if low > high:
            print("Valor no encontrado en la lista")
            return -1

        mid = (low + high) // 2

        # Asegurarse de que los elementos son cadenas de texto
        mid_val = str(array[mid]).lower()
        data = str(data).lower()

        if mid_val.endswith(data):
            print(f"Valor encontrado en la posicion: {mid}")
            return mid
        elif mid + 1 < len(array) and str(array[mid+1]).lower().endswith(data):
            print(f"Valor encontrado en la posicion: {mid+1}")
            return mid+1
        elif mid - 1 >= 0 and str(array[mid-1]).lower().endswith(data):
            print(f"Valor encontrado en la posicion: {mid-1}")
            return mid-1
        elif mid_val > data:
            return self.binary_string(array, data, low, mid - 1)
        else:
            return self.binary_string(array, data, mid + 1, high)

    