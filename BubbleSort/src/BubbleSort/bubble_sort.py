class BubbleSort:
    """
    Класс, реализующий алгоритм сортировки пузырьком.
    """
    def sort(self, numbers: list[int]) -> list[int]:
        """
        Сортирует список целых чисел по возрастанию.
        """
        for i in range(len(numbers)): # Проходим по списку, начиная с первого элемента
            for j in range(len(numbers)-i-1): # Проходим по оставшейся части списка, начиная с текущего элемента i
                if numbers[j] > numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

        return numbers
