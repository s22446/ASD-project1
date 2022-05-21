class QuickSort:
    """
    QuickSort
    Responsible for quick sorting
    """

    def partition(self, array, start, end):
        end_element = array[end]
        i = start - 1
        for j in range(start, end):
            if (array[j] <= end_element):
                i += 1
                array[j], array[i] = array[i], array[j]
        array[i + 1], array[end] = array[end], array[i + 1]

        return i + 1

    def quicksort(self, array, start, end):
        if start < end:
            part = self.partition(array, start, end)
            self.quicksort(array, start, part - 1)
            self.quicksort(array, part + 1, end)
