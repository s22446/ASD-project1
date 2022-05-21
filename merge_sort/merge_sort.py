class MergeSorter:
    """
    MergeSorter
    Responsible for merge-sort sorting
    """

    def merge_sort(self, array):
        if len(array) > 1:
            middle = len(array) // 2
            left_array = array[:middle]
            right_array = array[middle:]

            self.merge_sort(left_array)
            self.merge_sort(right_array)

            i = 0
            j = 0

            k = 0

            while i < len(left_array) and j < len(right_array):
                if left_array[i] <= right_array[j]:
                    array[k] = left_array[i]
                    i += 1
                else:
                    array[k] = right_array[j]
                    j += 1

                k += 1

            while i < len(left_array):
                array[k] = left_array[i]
                i += 1
                k += 1

            while j < len(right_array):
                array[k] = right_array[j]
                j += 1
                k += 1
