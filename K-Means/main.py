import matplotlib.pyplot as plt
import numpy as np
import time

from argparse import ArgumentParser
from functions import KMeans

parser = ArgumentParser(description="The K-Means Algorithm to Generate Clusters")
parser.add_argument("filename", type=str, help="The dataset filename (as a .csv)")
parser.add_argument("k", type=int, help="The number of clusters you want to generate")
parser.add_argument("sq_err", type=float, help="The termination criterion", default=0.001)
parser.add_argument("type", type=str, help="What is the datatype in the columns?", default="int")
parser.add_argument("-x", dest="x", type=int, help="The column in the dataset for the x axis", default=0)
parser.add_argument("-y", dest="y", type=int, help="The column in the dataset for the y axis", default=1)
parser.add_argument("-t", dest="t", action="store_true", help="Set if there are column titles")
parser.add_argument("-d", dest="delimiter", type=str, help="The delimiter", default=",")
args = parser.parse_args()

st = time.time()

dataset = np.genfromtxt(args.filename, delimiter=args.delimiter, dtype=args.type)

k_means = KMeans(args.k, dataset, args.t, args.sq_err)
k_means.run()

colors = 10*["b","g","r","c","m","y"]

for i in range(args.k):
    color = colors[i]
    cluster = k_means.clusters[i]

    for point in range(len(cluster)):
        plt.scatter(cluster[point][args.x], cluster[point][args.y], marker='+', c=color)

for i in range(args.k):
    plt.scatter(k_means.centers[i][args.x], k_means.centers[i][args.y],
        marker='o', color='k', s=35, linewidths=5)

print("Time: {:.5f} secs".format(time.time() - st))

plt.show()
