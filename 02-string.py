print(type('Hellloooooo'))  # str

# both ' or " works
print('Hellloooooo')
print("Hellloooooo")

# long string with '''
print('''Hellloooooo
      Hue
      !!!''')

# Escape Sequence
weather = "It\'s \"kind of\" sunny"
print(weather)

'I\'m thirsty'
"I'm thirsty"
"\n"  # new line
"\t"  # adds a tab

# Formatted String
print("Hello {}, your balance: {}.".format("Cindy", 50))
print("Hello {0}, your balance: {1}.".format("Cindy", 50))
print("Hello {name}, your balance: {amount}.".format(name="Cindy", amount=50))
print("Hello {0}, your balance: {amount}.".format("Cindy", amount=50))


# String Indexes
# [start:stop:stepover]
# negative index = start at the end, starting -1
'Hey you!'[4]  # y
name = 'Andrei Neagoie'
name[4]       # e
name[:]       # Andrei Neagoie
name[1:]      # ndrei Neagoie
name[:1]      # A
name[-1]      # e
name[::1]     # Andrei Neagoie
name[::-1]    # eiogaeN ierdnA
name[0:10:2]  # Ade e
# : is called slicing and has the format [ start : end : step ]

# String Concatenation
'Hi there ' + 'Timmy'  # 'Hi there Timmy'
'*'*10  # **********

# Immutability
a = 'aaaa'
a = 'aaa'
# a[0] = 'b'  # ERROR: IMMUTABLE
print(a)
