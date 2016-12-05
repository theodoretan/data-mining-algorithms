import math
import numpy as np


from random import randint

class KMeans:
    def __init__(self, k, dataset, x, y, t, sq_err=0.001):
        self._k = k
        self._dataset = dataset if not t else dataset[1:]
        self._size = np.shape(dataset)
        self._centers = {}
        self._clusters = {i: [[], []] for i in range(k)}
        self._x = x
        self._y = y
        self._squared_error = sq_err

    def set_centers(self):
        for i in range(self._k):
            c = randint(0, self._size[0] - 1)
            x, y = self._dataset[c, self._x], self._dataset[c, self._y]
            self._centers[i] = (x, y)
        return

    def assign(self):
        while True:

            for entry in self._dataset:
                # print(entry)
                # input()
                x, y = entry[self._x], entry[self._y]

                # compute distance and put in correct cluster
                self._distance(x, y)

            # Keep track of squared erros
            sq_error = [False for i in range(self._k)]

            # calculate the new cluster centers
            for i in range(self._k):
                l = len(self._clusters[i][0])
                if l == 0:
                    nx = self._centers[i][0]
                    ny = self._centers[i][1]
                else:
                    nx = sum(self._clusters[i][0]) / l
                    ny = sum(self._clusters[i][1]) / l

                # only return if all clusters are less than the sq_err
                if self._check_end(nx, ny, i):
                    sq_error[i] = True

                self._centers[i] = (nx, ny)

            if all(sq_error):
                return

            self._clear_clusters()
        return

    def _distance(self, x, y):
        m = math.sqrt((self._centers[0][0] - x)**2 + (self._centers[0][1] - y)**2)
        p = 0
        for i, j in self._centers.items():
            d = math.sqrt((j[0] - x)**2 + (j[1] - y)**2)
            if d < m:
                m = d
                p = i
        self._clusters[p][0].append(x)
        self._clusters[p][1].append(y)
        return

    def _check_end(self, nx, ny, i):
        d = math.sqrt((self._centers[i][0] - nx)**2 + (self._centers[i][1] - ny)**2)
        if d < self._squared_error:
            return True
        return False

    def _clear_clusters(self):
        for i in range(self._k):
            self._clusters[i][0] = []
            self._clusters[i][1] = []
        return
