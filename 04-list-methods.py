# https://www.w3schools.com/python/python_ref_list.asp

basket = [1, 2, 3, 4, 5]

# ADD: append, insert, extend
none_list = basket.append(100)
new_list = basket
print(basket)     # [1, 2, 3, 4, 5, 100]
print(none_list)  # none
print(new_list)   # [1, 2, 3, 4, 5, 100]

# ==========================================
# REMOVE: pop, remove
# pop     -> remove & return the 'pop' element
# remove  -> remove & NOT return anything

# ==========================================
# index

# ==========================================
# basket.sort()   -> sort original list
# sorted(basket)  -> sort & return new list

# ==========================================
# COPY: copy, [:]
# basket.copy()   -> copy & return a new list
# basket[:]       -> copy & return a new list

# ==========================================
# REVERSE: reverse, [::-1]
# basket.reverse()
# basket[::-1]

# ==========================================
print(range(1, 10))         # range(1, 10)
print(list(range(1, 10)))   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10)))      # way to generate a list quickly

# ==========================================
# join('')
new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'Hue'])
print(new_sentence)

# ==========================================
# LIST UNPACKING
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)      # 1
print(b)      # 2
print(c)      # 3
print(other)  # [4, 5, 6, 7, 8]
print(d)      # 9
