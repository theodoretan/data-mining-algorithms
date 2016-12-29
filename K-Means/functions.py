import math
import numpy as np

from random import randint

class KMeans:
    """
    ------------------------------------------------------
    The K-Means Implementation.
    ------------------------------------------------------
    Functions:
        run(): runs the K-Means algorithm
    Variables:
        centers: dict of the cluster centers
        clusters: dict of the points in the cluster
    ------------------------------------------------------
    """
    def __init__(self, k, dataset, t, sq_err=0.0001):
        self._k = k
        self._dataset = dataset if not t else dataset[1:]
        self._size = np.shape(dataset)
        self._squared_error = sq_err
        self.centers = {}
        self.clusters = {i: [] for i in range(k)}
        return

    def run(self):
        """
        ------------------------------------------------------
        Runs the K-Means Algorithm.
        ------------------------------------------------------
        """
        self._set_centers()
        self._assign()
        return


    def _set_centers(self):
        """
        ------------------------------------------------------
        Set the centers of the k-clusters.
        ------------------------------------------------------
        """
        for i in range(self._k):
            c = randint(0, self._size[0] - 1)
            self.centers[i] = self._dataset[c]
        return


    def _assign(self):
        """
        ------------------------------------------------------
        Assign the points to a cluster.
        ------------------------------------------------------
        """
        # set max steps to 500
        for loop in range(500):
            # calculate the distance for each point
            for entry in self._dataset:
                self._distance(entry)

            # Keep track of squared errors
            sq_error = [False for i in range(self._k)]

            # calculate the new cluster centers
            for i in range(self._k):
                l = len(self.clusters[i])
                if l == 0:
                    nv = self.centers[i]
                else:
                    nv = np.average(self.clusters[i], axis=0)
                # only return if all clusters are less than the sq_err
                if self._check_end(nv, i):
                    sq_error[i] = True

                self.centers[i] = nv

            if all(sq_error):
                return

            self._clear_clusters()
        return


    def _distance(self, vector):
        """
        ------------------------------------------------------
        Calculates the distance of the vector and adds it to
        the corresponding cluster.
        ------------------------------------------------------
        Inputs:
            vector - the vector we're calculating the
                distance of
        ------------------------------------------------------
        """
        min_dis = np.linalg.norm(vector-self.centers[0])
        p = 0

        for i, j in self.centers.items():
            if (i == 0): continue # skip the first center
            dis = np.linalg.norm(vector-j)
            if dis < min_dis:
                min_dis = dis
                p = i
        self.clusters[p].append(vector)
        return


    def _check_end(self, nv, i):
        """
        ------------------------------------------------------
        Set a queen on the board.
        ------------------------------------------------------
        Inputs:
            nv - the new center vector
            i - the index of the old center vector
        Returns:
            If the algorithm is complete (bool)
        ------------------------------------------------------
        """
        d = np.linalg.norm(nv-self.centers[i])

        return d < self._squared_error


    def _clear_clusters(self):
        """
        ------------------------------------------------------
        Clears the clusters to repeat the algorithm.
        ------------------------------------------------------
        """
        for i in range(self._k):
            self.clusters[i]=[]
        return
