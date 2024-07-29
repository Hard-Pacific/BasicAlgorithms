from src.SelectionSort import SelectionSort
import pytest

class TestSelectionSort:
    @pytest.fixture
    def selection_class(self):
        yield SelectionSort()
    def test_sort(self, selection_class):
        assert selection_class.sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
        assert selection_class.sort([3, 2, 1]) == [1, 2, 3]
        assert selection_class.sort([2, 3, 1]) == [1, 2, 3]
        assert selection_class.sort([1, 1, 1]) == [1, 1, 1]
        assert selection_class.sort([0, 1, 0]) == [0, 0, 1]
        assert selection_class.sort([]) == []
        assert selection_class.sort([3999, 2999, 1999]) == [1999, 2999, 3999]
        