from itertools import combinations

def apriori(dataset, mins):
    """
    ------------------------------------------------------
    The Apriori Algorithm.
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
    # itemlist is the list of large item sets
    _iset, iset, itemlist = {}, {}, []
    total = 0
    # go through the dataset and count the number of time a value is in the data
    for entry in dataset:
        for item in entry:
            _iset[item] = 1 if item not in _iset else _iset[item]+1
        total += 1 # since we're already going through the dataset we won't use len(dataset)
    # update the set of values above the minimum support and the values under the minimum support
    for key, value in _iset.items():
        if value/total >= mins: iset[tuple([key])] = value/total
    # iset = {key: (value/total) for key, value in iset.items() if value/total >= mins}
    itemlist.append(iset)
    itemlist = _apriori(dataset, mins, total, itemlist)
    return total, itemlist

def _new_itemsets(k, itemsets):
    """
    ------------------------------------------------------
    Creates the k+1 Combinations.
    ------------------------------------------------------
    Inputs:
        k - the size of the current set
        itemsets - the k itemset
    Returns:
        itemset - the k+1 frequent itemset (list)
    ------------------------------------------------------
    """
    large_itemsets = []
    item_set = set()

    # go through the k item set and look for k-1 combinations
    for item1 in itemsets:
        for item2 in itemsets:
            if (len(set(item1) & set(item2)) == (k-1)):
                union = set(item1) | set(item2)

                # if the length of the set is the size we are looking for then add it to the list
                if (len(union) == k+1):
                    large_itemsets.append(tuple(sorted(union)))

    # add the k+1 combinations to the set
    for i in large_itemsets:
        if (i not in item_set):
            item_set.add(i)

    return list(item_set)


def _apriori(dataset, mins, total, itemlist):
    """
    ------------------------------------------------------
    The Recursive Apriori Algorithm.
    ------------------------------------------------------
    Inputs:
        dataset - dataset of m transactions (2d-list)
        mins - minimum support
        total - the total number of entries in the
            dataset
        itemlist - the list of all the itemsets
    Returns:
        itemlist - the frequent itemlist
    ------------------------------------------------------
    """
    # _iset is the initial set of all items
    # iset is the new set of values above the minimum support
    _iset, iset = {}, {}

    # make sure we're still under the possible number of values
    if len(itemlist)+1 > len(itemlist[0]): return itemlist

    # creates the k+1 combinations
    iterlist = _new_itemsets(len(itemlist), itemlist[-1])
    if iterlist == []: return itemlist

    # for each item in the iterlist, check if those values are in the dataset
    for entry in dataset:
        for item in iterlist:
            if set(item).issubset(set(entry)): # checks if itemset is in the entry
                _iset[item] = 1 if item not in _iset else _iset[item]+1

    # check for minimum support
    for key, value in _iset.items():
        if value/total >= mins: iset[key] = value/total

    if iset == {}: return itemlist

    # add the itemset to the list of itemsets
    itemlist.append(iset)
    itemlist = _apriori(dataset, mins, total, itemlist)
    
    return itemlist

def associations(items, total, itemlist, confidence):
    """
    ------------------------------------------------------
    Mines the Association Rules.
    ------------------------------------------------------
    Inputs:
        items - the item combination
        total - the number of entries in the dataset
        itemlist - the frequent itemlist
        confidence - the minimum confidence
    Returns:
        associations - the association rules
    ------------------------------------------------------
    """
    associations = []
    main_item = [tuple(items)]

    # going through each item in the item combination
    for i in range(1, len(items)):
        # create all the possible combinations for this item combination
        combos = list(combinations(items, i))

        # going through each generated combination
        for combo in combos:

            # the confidence is bigger than the min confidence, add it to the list
            if (itemlist[len(items)-1][main_item[0]]/itemlist[i-1][combo] > confidence):
                final = tuple(set(items)-set(combo))
                associations.append("{} => {}".format(", ".join(combo), ", ".join(final)))

    return associations
