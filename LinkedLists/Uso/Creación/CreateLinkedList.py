class Node:
    def __init__(self, data=None):
        self.data = data  # Valor del nodo
        self.next = None  # Referencia al siguiente nodo

class LinkedList:
    def __init__(self):
        self.head = None  # Inicialmente, la lista está vacía

    def append(self, data):
        new_node = Node(data)  # Crear un nuevo nodo
        if not self.head:
            # Si la lista está vacía, el nuevo nodo se convierte en el primer nodo
            self.head = new_node
            return
        # Si la lista no está vacía, recorre la lista hasta el final
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        # Asigna el nuevo nodo al siguiente del último nodo
        last_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()  # Nueva línea al final de la impresión

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una nueva lista enlazada
    ll = LinkedList()

    # Agregar elementos a la lista
    ll.append(10)
    ll.append(20)
    ll.append(30)

    # Imprimir la lista
    ll.print_list()  # Salida: 10 20 30
