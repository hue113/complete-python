# loop, but also get index
for i, char in enumerate((1, 2, 3, 4, 5)):
    print(i, char)
    
# find index of value in a list
for i, char in enumerate(list(range(100))):
    if char == 40:
        print(f'index of 40 is: {i}')
