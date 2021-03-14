my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_list2 = [(1, 2), (3, 4), (5, 6)]
my_dict = {'a': 1, 'b': 2, 'c': 3}

for num in my_list:
    print(num)    # 1, 2, 3

for num in my_tuple:
    print(num)    # 1, 2, 3

for num in my_list2:
    print(num)    # (1,2), (3,4), (5,6)

for num in '123':
    print(num)    # 1, 2, 3

for k, v in my_dict.items():   # Dictionary Unpacking
    print(k)      # 'a', 'b', 'c'
    print(v)      # 1, 2, 3

# while < condition that evaluates to boolean >: # noqa
#     #  action
#     if < condition that evaluates to boolean >: # noqa
#         break     # break out of while loop
#     if < condition that evaluates to boolean >: # noqa
#         continue  # continue to the next line in the block

# =======================================================
# ITERABLE: list, dictionary, tuple, set, string
# for item in (1, 2, 3, 4, 5):
#     for x in ['a', 'b', 'c']:
#         print(item, x)

user = {
  'name': 'Hue',
  'age': 100,
  'can_swim': 'no'
}

for item in user.items():
    print(item)
for k, v in user.items():
    print(k)
    print(v)
for item in user:  # name, age, can_swim
    print(item)
for item in user.values():  # Hue, 100, no
    print(item)
