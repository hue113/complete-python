# https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
# LIST SLICING:
my_list = ['a', 'b', 'c']
print(my_list[1])    # b
print(my_list[-2])   # b
print(my_list[1:3])  # b c
my_list[0] = 'z'     # z b c
print(my_list)


qtm_list = ['q', 'u', 'a', 'n', 't', 'r', 'i',
            'm', 'a', 'n', 'g', '.', 'c', 'o', 'm']
print(qtm_list[1:5])   # ['u', 'a', 'n', 't']
print(qtm_list[:-8])   # ['q', 'u', 'a', 'n', 't', 'r', 'i']
print(qtm_list[9:])    # ['n', 'g', '.', 'c', 'o', 'm']

# List are mutable
my_list2 = [1, 2, 3]
bonus = my_list2 + [5]   # 1 2 3 5 -> mutable
my_list[0] = 'z'        # z 2 3   -> mutable
print(my_list2)
print(bonus)


# Note: copy a list
my_list3 = [1, 2, 3]
my_list4 = my_list3  # copy, refer to same reference point
my_list4[0] = 'z'
print(my_list3)   # z 2 3
print(my_list4)   # also: z 2 3

# copy, but not same reference point -> list5 change, list3 not change
my_list5 = my_list3[:]

# list nested in list
ln_list = ["Happy", [1, 3, 5, 9]]
print(ln_list[0][1])  # a
