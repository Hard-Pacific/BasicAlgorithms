class SelectionSort:
    def sort(self, numbers: list[int]) -> list[int]:
        if numbers == []:
            return numbers
        
        
        for i in range(len(numbers)):
            min_num = numbers[i]
            index = i
            for j in range(i, len(numbers)):
                if min_num > numbers[j]:
                    min_num = numbers[j]
                    index = j
            numbers[index], numbers[i] = numbers[i], numbers[index]
        return numbers