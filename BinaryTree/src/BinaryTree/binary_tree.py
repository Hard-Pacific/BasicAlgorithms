"""
Дерево — это иерархическая структура данных, состоящая из узлов,
соединенных ребрами. Каждый узел содержит значение и ссылки 
на свои дочерние узлы.

Двоичное дерево — это тип древовидной структуры данных, в которой
каждый узел может иметь максимум два дочерних узла: 
левый дочерний узел и правый дочерний узел.
"""

class Node:
    def __init__(self, root: int):
        self.root = root
        self.left = None
        self.right = None

class BinaryTree:
    """
    Класс, реализующий бинарное дерево.
    """
    def __init__(self):
        self.node = None

    def add_node(self, x: int):
        """
        Метод добавляющий новый узел дерева
        """
        if self.node == None:
            self.node = Node(x)
            return
        return self.__add_node(x, self.node)

    def __add_node(self, x: int, node: Node):
        if node == None:
            return 1
        if x >= node.root:
            if node.right == None:
                node.right = Node(x)
            else:
                node = node.right
                return self.__add_node(x, node)
        elif x < node.root:
            if node.left == None:
                node.left = Node(x)
            else:
                node = node.left
                return self.__add_node(x, node)
        return 1

    def get_numbers(self):
        if self.node == None:
            return []
        numbers = []
        self.__get_numbers(self.node, numbers)
        return numbers

    def __get_numbers(self, node: Node, numbers=[]):
        if node == None:
            return 
        self.__get_numbers(node.right, numbers)
        numbers.append(node.root)
        self.__get_numbers(node.left, numbers)

        return numbers
    




