# import matplotlib.pyplot as plt
import numpy as np
import random
import time

from argparse import ArgumentParser
from functions import KMeans
from numpy import genfromtxt

parser = ArgumentParser(description="The K-Means Algorithm to Generate Clusters")
parser.add_argument("filename", type=str, help="The dataset filename (as a .csv)")
parser.add_argument("k", type=int, help="The number of clusters you want to generate")
parser.add_argument("-d", dest="delimiter", type=str, help="The delimiter", default=",")
args = parser.parse_args()

st = time.time()
dataset = genfromtxt(args.filename, delimiter=args.delimiter)

k_means = KMeans(args.k, dataset)
k_means.set_centers()
print(k_means._dataset[0:3])
# k_means.assign()

# print(time.time() - st)

# NOTE
# 3. assign all points to one of the Clusters
# 4. calculate new cluster centers
# 5. repeat 3 & 4
