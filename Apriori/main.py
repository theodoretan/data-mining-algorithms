import sys
from argparse import ArgumentParser
from functions import apriori, associations

parser = ArgumentParser(description="The Apriori Algorithm to Mine Association Rules")
parser.add_argument("filename", type=str, help="The dataset filename (as a .csv)")
parser.add_argument("support", type=float, help="The minimum support to reduce the search space")
parser.add_argument("confidence", type=float, help="The minimum confidence for mining ARs")
parser.add_argument("-d", dest="delimiter", type=str, help="The delimiter", default=",")
args = parser.parse_args()

dataset = []
with open(args.filename, "r", encoding="utf-8") as f:
    for line in f:
        dataset.append(line.strip().split(args.delimiter))
total, itemlist = apriori(dataset, args.support)

# print(itemlist[0])
if (len(itemlist) > 1):
    print ("SUPPORT")
    for items in itemlist[0]:
        print("{}: {}".format(items, itemlist[0][items]))


    itemlist1 = itemlist[1:]
    association = []
    for items in itemlist1:
        for item in items:
            a = associations(list(item), total, itemlist, args.confidence)
            if a != []: association.append(a)
            print("{}: {}".format(item, items[item]))
    print()

    print ("RULES")
    for rulelist in association:
        for rule in rulelist:
            print(rule)
