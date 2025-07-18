"""
Алгоритм бинарного поиска — это эффективный алгоритм для поиска 
заданного элемента (ключа) в отсортированном списке (массиве) данных.
Он работает, многократно деля пополам ту часть отсортированного списка, 
в которой может находиться искомый элемент.
"""


class BinarySearch:
    """
    Класс для линейного поиска.
    """
    def search(self, x: int, numbers: list[int], __distance=0) -> int:
        """
        Функция поиска x в списке numbers
        """
        if len(numbers) == 0:
            return -1
        
        middle = len(numbers)//2
        if x<numbers[middle]:
            return self.search(x, numbers[:middle], __distance)
        elif x>numbers[middle]:
            return self.search(x, numbers[middle:], __distance+middle)
        else:
            return middle + __distance

a = BinarySearch()
print(a.search(5, [1, 2, 3, 4, 5, 6, 7]))
