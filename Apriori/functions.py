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
        if value/total >= mins: iset[tuple([key])] = value/total
        else: monotonicity.append(key)
    # iset = {key: (value/total) for key, value in iset.items() if value/total >= mins}
    itemlist.append(iset)
    itemlist = _apriori(dataset, mins, total, itemlist, monotonicity)
    return total, itemlist

def _new_itemsets(k, itemsets):
    large_itemsets = []
    item_set = set()
    # print(k)
    # print(itemsets)
    for item1 in itemsets:
        for item2 in itemsets:
            # print(item1, item2)
            # print(set(item1) & set(item2))
            # input()

            if (len(set(item1) & set(item2)) == (k-1)):
                union = set(item1) | set(item2)
                # print(union)
                if (len(union) == k+1):
                    large_itemsets.append(tuple(sorted(union)))

    for i in large_itemsets:
        if (i not in item_set):
            item_set.add(i)


    # print (item_set)
    return list(item_set)

# NOTE: this is a recursive function
def _apriori(dataset, mins, total, itemlist, monotonicity):
    # _iset is the initial set of all items
    # iset is the new set of values above the minimum support
    _iset, iset = {}, {}
    # print(itemlist)
    # make sure we're still under the possible number of values
    if len(itemlist)+1 > len(itemlist[0]): return itemlist
    # iterlist = list(combinations(itemlist[0], len(itemlist)+1)) # creates the k+1 combinations
    iterlist = _new_itemsets(len(itemlist), itemlist[-1])
    if iterlist == []: return itemlist
    # anti-monotonicity
    # iterlist = [x for x in iterlist if not any(set(m).issubset(set(x)) for m in monotonicity)]

    # print(iterlist)

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

    # print(iset)

    itemlist.append(iset)
    itemlist = _apriori(dataset, mins, total, itemlist, monotonicity)
    return itemlist

def associations(items, total, itemlist, confidence):

    associations = []
    main_item = list(combinations(items, len(items)))
    # print(main_item)
    for i in range(1, len(items)):
        # print(items)
        combos = list(combinations(items, i))
        # print(combos)
        for combo in combos:
            # if (len(combo) == 1):
            #     combo, *r = combo
            # print(combo)
            if (itemlist[len(items)-1][main_item[0]]/itemlist[i-1][combo] > confidence):
                final = tuple(set(items)-set(combo))
                # print(itemlist[i-1], combo)
                if len(final) == 1:
                    final = final[0]
                    # print("here")
                associations.append("{} => {}".format(combo, final))
                # print(set(items))
    return associations
