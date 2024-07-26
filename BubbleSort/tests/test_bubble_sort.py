from src.BubbleSort import BubbleSort
import pytest


class TestBubbleSort:
    """
    Набор тестов для класса BubbleSort, реализующего алгоритм сортировки пузырьком.
    """
    @pytest.fixture
    def bubble_class(self):
        """
        Фикстура, создающая экземпляр класса BubbleSort для каждого теста.
        """
        yield BubbleSort()

    def test_sort(self, bubble_class):
        """
        Проверяет, что метод sort() правильно сортирует различные списки.
        """
        assert bubble_class.sort([3, 2, 1]) == [1, 2, 3]
        assert bubble_class.sort([3, 2, 10, 190, -200, 1240, 0, 0, 3]) == [-200, 0, 0, 2, 3, 3, 10, 190, 1240]
        assert bubble_class.sort([1, 1, 1]) == [1, 1, 1]
        assert bubble_class.sort([]) == []
        assert bubble_class.sort([0]) == [0]
