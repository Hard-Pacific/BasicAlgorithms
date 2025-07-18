import pytest
from src.LinearSearch import LinearSearch


class TestLinearSearch:
    """
    Набор юнит-тестов для класса линейного поиска.
    """
    @pytest.fixture
    def linear_class(self):
        """
        Фикстура, создающая экземпляр класса LinearSearch для каждого теста.
        """
        yield LinearSearch()

    def test_linear_search(self, linear_class):
        """
        Тестирование линейного поиска.
        """
        assert linear_class.search(1, [1, 2, 3]) == 0
        assert linear_class.search(9999, [9, 2, 0, -100, 300, 10000, 0, 9]) == -1
        assert linear_class.search(100, [-100, 100]) == 1
        assert linear_class.search(2, []) == -1
        assert linear_class.search(1, [1]) == 0
        assert linear_class.search(0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1

