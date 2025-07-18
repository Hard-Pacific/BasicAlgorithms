import pytest
from src.BinarySearch import BinarySearch


class TestBinarySearch:
    """
    Набор юнит-тестов для класса бинарного поиска.
    """
    @pytest.fixture
    def binary_class(self):
        """
        Фикстура, создающая экземпляр класса BinarySearch для каждого теста.
        """
        yield BinarySearch()

    def test_binary_search(self, binary_class):
        """
        Тестирование линейного поиска.
        """
        assert binary_class.search(1, [1, 2, 3]) == 0
        assert binary_class.search(9999, [-100, -55, -1, 1, 9823, 99999]) == -1
        assert binary_class.search(100, [-100, 100]) == 1
        assert binary_class.search(2, []) == -1
        assert binary_class.search(1, [1]) == 0
        assert binary_class.search(0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1

