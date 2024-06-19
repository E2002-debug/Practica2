class BinarySecuencial:
    def binary_primitive_secuencial(self, array, data, low, high):
        if low > high:
            return []

        mid = (low + high) // 2
        result = []

        # Si encontramos el dato, buscamos en ambas direcciones para encontrar todas las ocurrencias
        if array[mid] == data:
            # Agregar el valor encontrado
            result.append(array[mid])
            # Buscar hacia la izquierda del punto medio
            left = mid - 1
            while left >= low and array[left] == data:
                result.append(array[left])
                left -= 1
            # Buscar hacia la derecha del punto medio
            right = mid + 1
            while right <= high and array[right] == data:
                result.append(array[right])
                right += 1
            return result

        # Buscar en la mitad derecha
        if array[mid] < data:
            return self.binary_primitive_secuencial(array, data, mid + 1, high)
        # Buscar en la mitad izquierda
        else:
            return self.binary_primitive_secuencial(array, data, low, mid - 1)



    
