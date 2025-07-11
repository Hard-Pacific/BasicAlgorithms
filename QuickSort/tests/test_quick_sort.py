import pytest
from src.QuickSort import QuickSort


class TestInsertationSort:
    """
    Набор юнит-тестов для класса сортировки вставками.
    """
    @pytest.fixture
    def quick_class(self):
        """
        Фикстура, создающая экземпляр класса QuickSort для каждого теста.
        """
        yield QuickSort()

    def test_quick_sort(self, quick_class):
        """
        Тестирование сортировки различных списков.
        """
        assert quick_class.sort([1, 2, 3]) == [1, 2, 3]
        assert quick_class.sort([9, 2, 0, -100, 300, 10000, 0, 9]) == [-100, 0, 0, 2, 9, 9, 300, 10000]
        assert quick_class.sort([-100, 100]) == [-100, 100]
        assert quick_class.sort([1, 0]) == [0, 1]
        assert quick_class.sort([]) == []
        assert quick_class.sort([1]) == [1]

    def test_quick_sort_typeError(self, quick_class):
        """
        Проверка возникновения ошибки
        TypeError при неверном типе входных данных.
        """
        with pytest.raises(TypeError):
            quick_class.sort("Hello World")