class BubbleSorter:
    """
    BubbleSorter
    Responsible for bubble sorting
    """

    def bubble_sort(self, array):
        array_length = len(array)

        for i in range(array_length - 1):
            for j in range(0, array_length - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
