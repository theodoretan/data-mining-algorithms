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
    # _iset is the initial set of all items
    # iset is the new set of values above the minimum support
    # monotonicity is the list of values that are under the minimum support
    # itemlist is the list of large item sets
    _iset, iset, monotonicity, itemlist = {}, {}, [], []
    total = 0
    # go through the dataset and count the number of time a value is in the data
    for entry in dataset:
        for item in entry:
            _iset[item] = 1 if item not in _iset else _iset[item]+1
        total += 1 # since we're already going through the dataset we won't use len(dataset)
    # update the set of values above the minimum support and the values under the minimum support
    for key, value in _iset.items():
        if value/total >= mins: iset[key] = value/total
        else: monotonicity.append(key)
    # iset = {key: (value/total) for key, value in iset.items() if value/total >= mins}
    itemlist.append(iset)
    itemlist = _apriori(dataset, mins, total, itemlist, monotonicity)
    return itemlist

# NOTE: this is a recursive function
def _apriori(dataset, mins, total, itemlist, monotonicity):
    # _iset is the initial set of all items
    # iset is the new set of values above the minimum support
    _iset, iset = {}, {}

    # make sure we're still under the possible number of values
    if len(itemlist)+1 > len(itemlist[0]): return itemlist
    iterlist = list(combinations(itemlist[0], len(itemlist)+1)) # creates the k+1 combinations

    # anti-monotonicity
    iterlist = [x for x in iterlist if not any(set(m).issubset(set(x)) for m in monotonicity)]

    # for each item in the iterlist, check if those values are in the dataset
    for entry in dataset:
        for item in iterlist:
            if set(item).issubset(set(entry)): # checks if itemset is in the entry
                _iset[item] = 1 if item not in _iset else _iset[item]+1
    # check for minimum support
    for key, value in _iset.items():
        if value/total >= mins: iset[key] = value/total
        else: monotonicity.append(key)
    # iset = {key: (value/total) for key, value in iset.items() if value/total >= mins}
    if iset == {}: return itemlist
    itemlist.append(iset)
    itemlist = _apriori(dataset, mins, total, itemlist, monotonicity)
    return itemlist
