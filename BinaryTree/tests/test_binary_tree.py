from src.BinaryTree import BinaryTree
import pytest


class TestBinaryTree:
    """
    Набор тестов для класса BinaryTree, реализующего бинарное дерево.
    """
    @pytest.fixture
    def binary_tree(self):
        """
        Фикстура, создающая экземпляр класса BinaryTree для каждого теста.
        """
        yield BinaryTree()

    def test_add_node_empty_tree(self, binary_tree):
        """
        Проверяет, что метод add_node() правильно добавляет первый узел в пустое дерево.
        """
        binary_tree.add_node(5)
        assert binary_tree.node.root == 5
        assert binary_tree.node.left is None
        assert binary_tree.node.right is None

    def test_add_node_greater_than_root(self, binary_tree):
        """
        Проверяет, что метод add_node() правильно добавляет узел больше, чем корень, в правое поддерево.
        """
        binary_tree.add_node(5)
        binary_tree.add_node(10)
        assert binary_tree.node.right.root == 10
        assert binary_tree.node.right.left is None
        assert binary_tree.node.right.right is None
    def test_add_node_equal_to_root(self, binary_tree):
        """
        Проверяет, что метод add_node() правильно добавляет узел, равный корню, в правое поддерево (по условию >=).
        """
        binary_tree.add_node(5)
        binary_tree.add_node(5)
        assert binary_tree.node.right.root == 5
        assert binary_tree.node.right.left is None
        assert binary_tree.node.right.right is None

    def test_get_numbers_empty_tree(self, binary_tree):
        """
        Проверяет, что метод get_numbers() возвращает пустой список для пустого дерева.
        """
        assert binary_tree.get_numbers() == []

    def test_get_numbers_single_node_tree(self, binary_tree):
        """
        Проверяет, что метод get_numbers() возвращает список с единственным узлом для дерева с одним узлом.
        """
        binary_tree.add_node(5)
        assert binary_tree.get_numbers() == [5]

    def test_get_numbers_multiple_nodes_tree(self, binary_tree):
        """
        Проверяет, что метод get_numbers() возвращает список отсортированных чисел в порядке убывания для дерева с несколькими узлами.
        """
        binary_tree.add_node(5)
        binary_tree.add_node(2)
        binary_tree.add_node(10)
        binary_tree.add_node(1)
        binary_tree.add_node(3)
        binary_tree.add_node(7)
        binary_tree.add_node(12)
        assert binary_tree.get_numbers() == [12, 10, 7, 5, 3, 2, 1]
