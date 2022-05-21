# IMPORTS
import random


class ArrayGenerator:
    """
    ArrayGenerator
    Responsible for generating and returning array for sorting
    """

    def __init__(self, elements_count):
        self.array = [random.randint(1, 100000) for _ in range(elements_count)]

    def get_array(self):
        return self.array
