from src.SelectionSort import SelectionSort
import pytest

class TestSelectionSort:
    """
    Набор юнит-тестов для класса сортировки вставками.
    """
    @pytest.fixture
    def selection_class(self):
        """
        Фикстура, создающая экземпляр класса InsertationSort для каждого теста.
        """
        yield SelectionSort()
    
    def test_sort(self, selection_class):
        """
        Тестирование сортировки различных списков.
        """
        assert selection_class.sort([]) == []
        assert selection_class.sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
        assert selection_class.sort([5, 2, 8, 1, 9, 3]) == [1, 2, 3, 5, 8, 9]
        assert selection_class.sort([5, 2, 2, 1, 9, 3]) == [1, 2, 2, 3, 5, 9]
        assert selection_class.sort([-5, 2, -8, 1, 9, 3]) == [-8, -5, 1, 2, 3, 9]
