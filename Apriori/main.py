import sys
from argparse import ArgumentParser
from functions import apriori

parser = ArgumentParser(description="The Apriori Algorithm to Mine Association Rules")
parser.add_argument("filename", type=str, help="The dataset filename (as a .csv)")
parser.add_argument("support", type=float, help="The minimum support to reduce the search space")
parser.add_argument("confidence", type=float, help="The minimum confidence for mining ARs")
args = parser.parse_args()

dataset = []
with open(args.filename, "r", encoding="utf-8") as f:
    for line in f:
        dataset.append(line.strip().split(","))
itemlist = apriori(dataset, args.support)
print(itemlist)
