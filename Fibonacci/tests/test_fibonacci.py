from src.Fibonacci import Fibonacci
import pytest

class TestFibonacci:
    @pytest.fixture
    def fibonacci(self):
        return Fibonacci()

    def test_generate_empty(self, fibonacci):
        """Проверяет, что функция возвращает [1, 1], если n <= 1."""
        assert fibonacci.generate(1) == [1, 1]
        assert fibonacci.generate(0) == [1, 1] # added edge case for n = 0

    def test_generate_small_n(self, fibonacci):
        """Проверяет, что функция генерирует правильную последовательность для небольших n."""
        assert fibonacci.generate(5) == [1, 1, 2, 3, 5]

    def test_generate_larger_n(self, fibonacci):
        """Проверяет, что функция генерирует правильную последовательность для больших n."""
        assert fibonacci.generate(20) == [1, 1, 2, 3, 5, 8, 13]

    def test_generate_equal_n(self, fibonacci):
        """Проверяет, что функция генерирует последовательность, включающую n, если n - число Фибоначчи."""
        assert fibonacci.generate(8) == [1, 1, 2, 3, 5, 8]

    def test_generate_large_n(self, fibonacci):
        assert fibonacci.generate(100) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

