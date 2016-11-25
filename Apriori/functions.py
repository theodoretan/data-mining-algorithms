from itertools import combinations

def apriori(dataset, mins):
    """
    ------------------------------------------------------
    The Apriori Algorithm
    ------------------------------------------------------
    Inputs:
        dataset - dataset of m transactions (2d-list)
        mins - minimum support
    Returns:
        itemlist - the frequent itemlist
    ------------------------------------------------------
    """
    iset, itemlist = {}, []
    total = 0
    for entry in dataset:
        for item in entry:
            iset[item] = 1 if item not in iset else iset[item]+1
        total += 1 # since we're already going through the dataset we won't use len(dataset)
    iset = {key: (value/total) for key, value in iset.items() if value/total >= mins}
    itemlist.append(iset)
    itemlist = _apriori(dataset, mins, total, itemlist)
    return itemlist

def _apriori(dataset, mins, total, itemlist):
    iset = {}
    if len(itemlist)+1 > len(itemlist[0]): return itemlist
    iterlist = list(combinations(itemlist[0], len(itemlist)+1)) # creates the k+1 combinations
    # will have to check for anti-monotonicity and downward closure to reduce the search space
    # for each item in the iterlist, check if those values are in the dataset
    for entry in dataset:
        for item in iterlist:
            if set(item).issubset(set(entry)):
                iset[item] = 1 if item not in iset else iset[item]+1
    iset = {key: (value/total) for key, value in iset.items() if value/total >= mins}
    if iset == {}: return itemlist
    itemlist.append(iset)
    itemlist = _apriori(dataset, mins, total, itemlist)
    return itemlist
