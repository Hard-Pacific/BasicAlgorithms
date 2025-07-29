from src.LinkedList import LinkedList
import pytest

class TestLinkedList:
    """
    Набор тестов для класса LinkedList, реализующего связный список.
    """

    @pytest.fixture
    def linked_list(self):
        """
        Фикстура, создающая экземпляр класса LinkedList для каждого теста.
        """
        yield LinkedList()

    def test_append(self, linked_list):
        """
        Проверяет, что append() добавляет элементы в конец списка.
        """
        linked_list.append(1)
        assert linked_list.get_list() == [1]
        linked_list.append(2)
        assert linked_list.get_list() == [1, 2]
        linked_list.append(3)
        assert linked_list.get_list() == [1, 2, 3]

    def test_remove_from_empty(self, linked_list):
        """Проверяем, что remove() ничего не делает с пустым списком"""
        linked_list.remove(5)
        assert linked_list.get_list() == []

    def test_remove_existing_element(self, linked_list):
        """
        Проверяет, что remove() удаляет существующий элемент из списка.
        """
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.remove(2)
        assert linked_list.get_list() == [1, 3]
        assert linked_list.contains(2) is False

    def test_remove_nonexistent_element(self, linked_list):
        """
        Проверяет, что remove() не делает ничего, если элемент не найден.
        """
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.remove(4)
        assert linked_list.get_list() == [1, 2, 3]

    def test_remove_first_element(self, linked_list):
        """
        Проверяет, что remove() правильно удаляет первый элемент списка.
        """
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.remove(1)
        assert linked_list.get_list() == [2, 3]
        assert linked_list.contains(1) is False

    def test_get_list(self, linked_list):
        """
        Проверяет, что get_list() возвращает правильный список элементов.
        """
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        assert linked_list.get_list() == [1, 2, 3]

    def test_get_list_empty(self, linked_list):
        """Проверяем, что get_list() возвращает пустой список, если список пуст"""
        assert linked_list.get_list() == []

    def test_len(self, linked_list):
        """
        Проверяет, что len() возвращает правильную длину списка.
        """
        assert len(linked_list) == 0
        linked_list.append(1)
        assert len(linked_list) == 1
        linked_list.append(2)
        linked_list.append(3)
        assert len(linked_list) == 3

    def test_contains(self, linked_list):
        """
        Проверяет, что contains() правильно определяет наличие элемента в списке.
        """
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        assert linked_list.contains(2) is True
        assert linked_list.contains(4) is False

    def test_contains_empty(self, linked_list):
      """Проверяем, что contains() возвращает False для пустого списка"""
      assert linked_list.contains(5) is False
