# set only contains unique value

my_set = set()
my_set.add(1)     # {1}
my_set.add(100)   # {1, 100}
my_set.add(100)   # {1, 100} --> no duplicates!

# ==========================================
new_list = [1, 2, 3, 3, 3, 4, 4, 5, 6, 1]
set(new_list)           # {1, 2, 3, 4, 5, 6}

# ==========================================
my_set.remove(100)      # {1} --> Raises KeyError if element not found
my_set.discard(100)     # {1} --> Doesn't raise an error if element not found
my_set.clear()          # {}
new_set = {1, 2, 3}.copy()    # {1,2,3}

# ==========================================
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)                 # {1,2,3,4,5}
set4 = set1.intersection(set2)          # {3}
set5 = set1.difference(set2)            # {1, 2}
set6 = set1.symmetric_difference(set2)  # {1, 2, 4, 5}
set1.issubset(set2)                     # False
set1.issuperset(set2)                   # False
set1.isdisjoint(set2)  # False -> return True if 2 sets have null intersection.

# ==========================================
# Frozenset
# hashable --> can be used as a key in a dictionary or as an element in a set.
< frozenset > = frozenset(< collection >) # noqa
