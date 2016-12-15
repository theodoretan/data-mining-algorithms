import matplotlib.pyplot as plt
import numpy as np
import os
import random
import time

from argparse import ArgumentParser
from functions import KMeans
from matplotlib import style
from numpy import genfromtxt

parser = ArgumentParser(description="The K-Means Algorithm to Generate Clusters")
parser.add_argument("filename", type=str, help="The dataset filename (as a .csv)")
parser.add_argument("k", type=int, help="The number of clusters you want to generate")
parser.add_argument("sq_err", type=float, help="The termination criterion", default=1)
# parser.add_argument("type", type=str, help="What is the datatype in the columns?", default="int")
parser.add_argument("-x", dest="x", type=int, help="The column in the dataset for the x axis", default=0)
parser.add_argument("-y", dest="y", type=int, help="The column in the dataset for the y axis", default=1)
parser.add_argument("-t", dest="t", action="store_true", help="Set if there are column titles")
parser.add_argument("-d", dest="delimiter", type=str, help="The delimiter", default=",")
args = parser.parse_args()

st = time.time()
# <<<<<<< Updated upstream
# dataset = genfromtxt(args.filename, delimiter=args.delimiter, dtype=t)
# =======
dataset = genfromtxt(args.filename, delimiter=args.delimiter, dtype=float)
# print(dataset)
# >>>>>>> Stashed changes

# Test to see if it actually works
# l = [[random.randint(0, 100) for i in range(0,5)] for j in range(100)]
# for j in range(50):
#     l.append([random.randint(450,600) for i in range(0,5)])
# for j in range(100): l.append([random.randint(700, 1000) for i in range(0,5)])
# dataset = np.array(l)

k_means = KMeans(args.k, dataset, args.x, args.y, args.t, args.sq_err)
# k_means.run()
k_means.set_centers()
# print(k_means._dataset[0:3])
k_means.assign()

colors = 10*["b","g","r","c","m","y"]
# print(k_means._clusters)
for i in range(args.k):
    color = colors[i]
    x_list = k_means._clusters[i][0]
    y_list = k_means._clusters[i][1]
    # cluster = k_means._clusters[i]

    # for index in ra:
    for i2 in range(np.size(x_list)):
    # for i2 in range(np.size(cluster)):
        plt.scatter(x_list[i2], y_list[i2], marker='+', c=color)
        # plt.scatter(cluster[args.x], cluster[args.y], marker='+', c=color)

for i in range(args.k):#k_means._centers:
    plt.scatter(k_means._centers[i][0], k_means._centers[i][1],
    # plt.scatter(k_means._centers[i][args.x], k_means._centers[i][args.y],
        marker='o', color='k', s=35, linewidths=5)
#
# # print(time.time() - st)
#
# os.system('espeak "K Means has found the clusters"')
# # NOTE
# # 3. assign all points to one of the Clusters
# # 4. calculate new cluster centers
# # 5. repeat 3 & 4
plt.show()
