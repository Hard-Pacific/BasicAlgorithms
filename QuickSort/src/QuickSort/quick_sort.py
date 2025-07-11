from random import choice

class QuickSort:
    """
    Implements the QuickSort algorithm for sorting a list of integers.

    QuickSort is a divide-and-conquer algorithm that works by selecting a 'pivot' element from the list
    and partitioning the other elements into two sub-lists, according to whether they are less than or
    greater than the pivot.  The sub-lists are then recursively sorted.

    This implementation uses a randomly chosen element as the pivot to help avoid worst-case scenarios
    (e.g., already sorted lists) that can degrade performance.
    """

    def sort(self, numbers: list[int]) -> list[int]:
        """
        Sorts a list of integers using the QuickSort algorithm.
        """
        # Base case:  If the list has 0 or 1 elements, it's already sorted.
        if len(numbers) <= 1:
            return numbers

        # Choose a random pivot element to avoid worst-case scenarios with sorted/nearly sorted data.
        pivot = choice(numbers)

        # Initialize lists to store elements less than, greater than, and equal to the pivot.
        left_nums = []
        right_nums = []
        equals_nums = []

        # Partition the list based on the pivot.  This is the core of the QuickSort algorithm.
        for num in numbers:
            if num < pivot:
                left_nums.append(num)
            elif num > pivot:
                right_nums.append(num)
            else:
                equals_nums.append(num)

        # Recursively sort the sub-lists and combine the results.
        # Note the use of 'self' to call the sort method recursively.  While 'QuickSort.sort(self, ...)'
        # would also work, using 'self.sort(...)' is more idiomatic and facilitates subclassing.
        # This implementation creates new lists during each partition and concatenation, resulting in
        # O(n log n) space complexity in the average case and O(n^2) in the worst case.  In-place partitioning
        # can reduce space complexity to O(log n).
        return self.sort(left_nums) + equals_nums + self.sort(right_nums)
