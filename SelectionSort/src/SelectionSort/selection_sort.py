"""
Алгоритм сортировки выбором заключается в поиске на необработанном 
срезе массива или списка минимального значения и в дальнейшем обмене 
этого значения с первым элементом необработанного среза 
(поиск минимума и перестановка). На следующем шаге необработанный 
срез уменьшается на один элемент.
"""


class SelectionSort:
    def sort(self, numbers: list[int]) -> list[int]:
        """
        Сортирует список чисел методом выбора.
        """
        # Проверка, пустой ли список
        if numbers == []:
            return numbers
        
        for i in range(len(numbers)):
            min_num = numbers[i] # Инициализируем минимальное значение как текущее число
            index = i # Инициализируем индекс минимального значения как текущий индекс
            for j in range(i, len(numbers)): # Проходим по остальной части списка
                if min_num > numbers[j]:
                    min_num = numbers[j]
                    index = j
            numbers[index], numbers[i] = numbers[i], numbers[index]
        return numbers
