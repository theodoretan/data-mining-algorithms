
def apriori(dataset, mins):
    """
    ------------------------------------------------------
    The Apriori Algorithm
    ------------------------------------------------------
    Inputs:
        dataset - dataset of m transactions
        mins - minimum support
    Returns:
        itemset - the frequent itemset
    ------------------------------------------------------
    """
    iset = {}
    total = 0
    # assuming each item in an entry is unique for the dataset
    # iset = {j: (1 if j not in iset else iset[j]+=1) for i in dataset for j in i}
    for entry in dataset:
        for item in entry:
            if item not in iset: iset[item] = 1
            else: iset[item] += 1
            total += 1
    iset = {key: value for key, value in iset.items() if value/total >= mins}
    itemset = _apriori(dataset, mins, itemset.append(iset))
    return itemset

def _apriori(dataset, mins, itemset):
    iset = []

    if iset == []: return itemset
    itemset = _apriori(dataset, mins, itemset.append(iset))
    return False
