class HeapSort:
    """
    HeapSort
    Responsible for heapsort sorting
    """

    def max_heapify(self, array, heap_size, position):
        left_element_position = 2 * position + 1
        right_element_position = 2 * position + 2

        if (left_element_position <= heap_size - 1 and array[left_element_position] > array[position]):
            largest = left_element_position
        else:
            largest = position

        if (right_element_position <= heap_size - 1 and array[right_element_position] > array[largest]):
            largest = right_element_position

        if (largest != position):
            array[position], array[largest] = array[largest], array[position]
            self.max_heapify(array, heap_size, largest)

    def heap_sort(self, array):
        heap_size = len(array)
        for i in range((heap_size - 1) // 2, -1, -1):
            self.max_heapify(array, heap_size, i)

        for i in range(heap_size - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self.max_heapify(array, i, 0)
