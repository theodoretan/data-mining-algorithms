import sys, time

from argparse import ArgumentParser
from functions import apriori, associations

# Argument parser for command line arguments
parser = ArgumentParser(description="The Apriori Algorithm to Mine Association Rules")
parser.add_argument("filename", type=str, help="The dataset filename (as a .csv)")
parser.add_argument("support", type=float, help="The minimum support to reduce the search space")
parser.add_argument("confidence", type=float, help="The minimum confidence for mining ARs")
parser.add_argument("-d", dest="delimiter", type=str, help="The delimiter", default=",")
args = parser.parse_args()

# read the dataset and store it in dataset
dataset = []
with open(args.filename, "r", encoding="utf-8") as f:
    for line in f:
        dataset.append(line.strip().split(args.delimiter))

start_time = time.time()

# run the apriori algorithm to find the large itemsets
total, itemlist = apriori(dataset, args.support)

# if there are items with a support greater than the minimum support
if (len(itemlist[0]) >= 1):
    print ("ITEMSETS & SUPPORT")
    for items in itemlist[0]:
        print("{}: {}".format(" ".join(items), itemlist[0][items]))

    # mine all the association rules for those items in the itemset
    association = []
    for items in itemlist[1:]:
        for item in items:
            a = associations(list(item), total, itemlist, args.confidence)
            if a != []: association.append(a)

            # print the itemset and it's support
            print("{}: {}".format(", ".join(item), items[item]))
    print()

    # print out the mined association rules with a confidence bigger than the minimum confidnence
    if association:
        print ("RULES")
    # print (association)
        for rulelist in association:
            for rule in rulelist:
                print(rule)
    else:
        print("NO RULES")
else:
    print("There are no large itemsets.")

print()
print("Time: {:0.5f} secs".format(time.time() - start_time))
