import numpy as np

from random import randint

class KMeans:
    def __init__(self, k, dataset):
        self._k = k
        self._dataset = dataset
        self._size = np.shape(dataset)
        self._centers = {}
        self._clusters = {i: set() for i in range(k)}

    def set_centers(self):
        for i in range(self._k):
            c = randint(0, self._size[0] - 1)
            self._centers[i] = (self._dataset[c, 0], self._dataset[c, 1])
        return

    # def assign(self):
    #     i = self._size[1] if self._size[1] % 2 == 0 else self._size[1] - 1
    # 
    #     for entry in self._dataset:
    #         for index in range(0, i, 2):
    #             x, y = entry
    #     return
