import unittest
from src.InsertationSort import InsertationSort


class TestInsertationSort(unittest.TestCase):
    """
    Набор юнит-тестов для класса сортировки вставками.
    """

    def setUp(self):
        self.sort_obj = InsertationSort.InsertationSort()

    def test_insertion_sort(self):
        """
        Тестирование сортировки различных списков.
        """
        self.assertEqual(
            self.sort_obj.sort([9, 2, 0, -100, 300, 10000, 0, 9]),
            [-100, 0, 0, 2, 9, 9, 300, 10000],
        )
        self.assertEqual(self.sort_obj.sort([-100, 100]), [-100, 100])
        self.assertEqual(self.sort_obj.sort([1, 0]), [0, 1])
        self.assertEqual(self.sort_obj.sort([]), [])
        self.assertEqual(self.sort_obj.sort([1]), [1])

    def test_insertion_sort_typeError(self):
        """
        Проверка возникновения ошибки
        TypeError при неверном типе входных данных.
        """
        with self.assertRaises(TypeError):
            self.sort_obj.sort("Hello World")


if __name__ == "__main__":
    unittest.main()
