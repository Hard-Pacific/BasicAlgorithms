"""
Сортировка вставками.

Алгоритм сортировки, похожий на BubbleSort, только
в нем мы сортируем элемент влево(сравниваем с соседов слева) до тех пор пока
не будет найдено место для вставки текущего элемента.

Пример:
[9, 0, 2, 5]
          ^
[9, 0, 5, 2]
       ^
[9, 5, 0, 2]
    ^
"""


class InsertationSort:
    """
    Класс для сортировки вставками.
    """

    def sort(self, mylist: list[int]) -> list[int]:
        """
        Метод сортировки вставками.
        """
        # Проходим по списку, начиная со второго элемента
        for list_index in range(1, len(mylist)):
            # Проходим по элементам слева от текущего,
            # пока не найдем правильное место для вставки
            for insert_index in range(list_index - 1, -1, -1):
                # Если текущий элемент больше следующего, меняем их местами
                if mylist[insert_index + 1] <= mylist[insert_index]:
                    mylist[insert_index + 1], mylist[insert_index] = (
                        mylist[insert_index],
                        mylist[insert_index + 1],
                    )
                else:
                    break

        return mylist
