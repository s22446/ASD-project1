# IMPORTS
import config

from array_generator.array_generator import ArrayGenerator

from heap_sort.heap_sort import HeapSort
from quick_sort.quick_sort import QuickSort
from merge_sort.merge_sort import MergeSorter
from bubble_sort.bubble_sort import BubbleSorter

import time


class Sorter:
    """
    Sorter Class
    Responsible for starting and processing sort exercises
    """

    def __init__(self):
        elements_count = config.ARRAY_ELEMENTS_COUNT
        array_generator = ArrayGenerator(elements_count)
        self.array = array_generator.get_array()

        print("STARTING SORTING. GENERATED ARRAY ELEMENTS COUNT: ", elements_count)

        heap_sort_array = self.array.copy()
        quick_sort_array = self.array.copy()
        merge_sort_array = self.array.copy()
        bubble_sort_array = self.array.copy()

        self.heap_sorting(heap_sort_array)
        self.quick_sorting(quick_sort_array)
        self.merge_sorting(merge_sort_array)
        self.bubble_sorting(bubble_sort_array)

        print("\nFINISHED")

    def heap_sorting(self, given_array):
        # Creating sorter
        heap_sorter = HeapSort()

        # Sorting unordered array
        print("\nHEAP SORT START")
        start_time = time.time()
        heap_sorter.heap_sort(given_array)
        end_time = time.time()
        print("HEAP SORT END. TIME: ", end_time - start_time)

        # Making copy of ordered array
        reversed_given_array = given_array.copy()
        reversed_given_array.reverse()

        # Sorting ordered array
        print("\nORDERED HEAP SORT START")
        start_time = time.time()
        heap_sorter.heap_sort(given_array)
        end_time = time.time()
        print("ORDERED HEAP SORT END. TIME: ", end_time - start_time)

        # Sorting reversed ordered array
        print("\nREVERSED ORDER HEAP SORT START")
        start_time = time.time()
        heap_sorter.heap_sort(reversed_given_array)
        end_time = time.time()
        print("REVERSED ORDER HEAP SORT END. TIME: ", end_time - start_time)

    def quick_sorting(self, given_array):
        # Creating sorter
        quick_sorter = QuickSort()

        # Sorting unordered array
        print("\nQUICK SORT START")
        start_time = time.time()
        quick_sorter.quicksort(given_array, 0, len(given_array) - 1)
        end_time = time.time()
        print("QUICK SORT END. TIME: ", end_time - start_time)

        # Making copy of ordered array
        reversed_given_array = given_array.copy()
        reversed_given_array.reverse()

        # Sorting ordered array (Expecting error)
        try:
            print("\nORDERED QUICK SORT START")
            start_time = time.time()
            quick_sorter.quicksort(given_array, 0, len(given_array) - 1)
            end_time = time.time()
            print("ORDERED QUICK SORT END. TIME: ", end_time - start_time)
        except:
            print("Quicksort ordered recursion depth error")
            end_time = time.time()
            print("ORDERED QUICK SORT END. TIME: ", end_time - start_time)

        # Sorting reversed ordered array (Expecting error)
        try:
            print("\nREVERSED ORDER QUICK SORT START")
            start_time = time.time()
            quick_sorter.quicksort(reversed_given_array, 0, len(reversed_given_array) - 1)
            end_time = time.time()
            print("REVERSED ORDER QUICK SORT END. TIME: ", end_time - start_time)

        except:
            print("Quicksort reversed order recursion depth error")
            end_time = time.time()
            print("REVERSED ORDER QUICK SORT END. TIME: ", end_time - start_time)

    def merge_sorting(self, given_array):
        # Creating sorter
        merge_sorter = MergeSorter()

        # Sorting unordered array
        print("\nMERGE SORT START")
        start_time = time.time()
        merge_sorter.merge_sort(given_array)
        end_time = time.time()
        print("MERGE SORT END. TIME: ", end_time - start_time)

        # Making copy of ordered array
        reversed_given_array = given_array.copy()
        reversed_given_array.reverse()

        # Sorting ordered array
        print("\nORDERED MERGE SORT START")
        start_time = time.time()
        merge_sorter.merge_sort(given_array)
        end_time = time.time()
        print("ORDERED MERGE SORT END. TIME: ", end_time - start_time)

        # Sorting reversed ordered array
        print("\nREVERSED ORDER MERGE SORT START")
        start_time = time.time()
        merge_sorter.merge_sort(reversed_given_array)
        end_time = time.time()
        print("REVERSED ORDER MERGE SORT END. TIME: ", end_time - start_time)

    def bubble_sorting(self, given_array):
        # Creating sorter
        bubble_sorter = BubbleSorter()

        # Sorting unordered array
        print("\nBUBBLE SORT START")
        start_time = time.time()
        bubble_sorter.bubble_sort(given_array)
        end_time = time.time()
        print("BUBBLE SORT END. TIME: ", end_time - start_time)

        # Making copy of ordered array
        reversed_given_array = given_array.copy()
        reversed_given_array.reverse()

        # Sorting ordered array
        print("\nORDERED BUBBLE SORT START")
        start_time = time.time()
        bubble_sorter.bubble_sort(given_array)
        end_time = time.time()
        print("ORDERED BUBBLE SORT END. TIME: ", end_time - start_time)

        # Sorting reversed ordered array
        print("\nREVERSED ORDER BUBBLE SORT START")
        start_time = time.time()
        bubble_sorter.bubble_sort(reversed_given_array)
        end_time = time.time()
        print("REVERSED ORDER BUBBLE SORT END. TIME: ", end_time - start_time)
