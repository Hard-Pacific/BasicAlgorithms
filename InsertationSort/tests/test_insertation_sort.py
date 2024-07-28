import pytest
from src.InsertationSort import InsertationSort


class TestInsertationSort:
    """
    Набор юнит-тестов для класса сортировки вставками.
    """
    @pytest.fixture
    def insertation_class(self):
        """
        Фикстура, создающая экземпляр класса InsertationSort для каждого теста.
        """
        yield InsertationSort()

    def test_insertion_sort(self, insertation_class):
        """
        Тестирование сортировки различных списков.
        """
        assert insertation_class.sort([1, 2, 3]) == [1, 2, 3]
        assert insertation_class.sort([9, 2, 0, -100, 300, 10000, 0, 9]) == [-100, 0, 0, 2, 9, 9, 300, 10000]
        assert insertation_class.sort([-100, 100]) == [-100, 100]
        assert insertation_class.sort([1, 0]) == [0, 1]
        assert insertation_class.sort([]) == []
        assert insertation_class.sort([1]) == [1]

    def test_insertion_sort_typeError(self, insertation_class):
        """
        Проверка возникновения ошибки
        TypeError при неверном типе входных данных.
        """
        with pytest.raises(TypeError):
            insertation_class.sort("Hello World")
