# Data Mining Algorithms

## Setup

Linux:
```
cd data-mining-algorithms
$ sudo ./setup.sh
```
This will set up pypy3.3, pip3, matplotlib, and numpy.

---

## Apriori Algorithm
To run the algorithm:

```
$ pypy3.3 Apriori/main.py [filename] [support] [confidence] -d D
```

- _filename_: the filename of the dataset [a .csv file]
- _support_: the minimum support for the apriori algorithm [float]
- _confidence_: the minimum confidence to mine association rules [float]
- _-d D_: the delimiter (default: ,) [str]

Example:

```
$ pypy3.3 Apriori/main.py Datasets/Apriori/apr.fpg.retail.comma.txt 0.5 0.5
```

---

## K-Means
To run the algorithm:

```
$ python3 K-Means/main.py [filename] [k] [squared error] [type] -x X -y Y -d D -t
```

- _filename_: the filename of the dataset [a .csv file]
- _k_: the number of clusters you want to generate [int]
- _squared error_: the termination criterion [float]
- _type_: the datatype of the data (int/float) [str]
- _-x X_: the column in the dataset for the x axis (default: 0) [int]
- _-y Y_: the column in the dataset for the y axis (default: 1) [int]
- _-d D_: the delimiter (default: ,) [str]
- _-t_: if the dataset has titles (flag)

Example:

```
$ python3 K-Means/main.py Datasets/K-Means/airports-titles.dat 6 0.0001 float -t
$ python3 K-Means/main.py Datasets/K-Means/km.comma.txt 4 0.0001 int -d ,
```
