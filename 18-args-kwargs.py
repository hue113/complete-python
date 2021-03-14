
def super_func(*args):
    print(args)  # (1, 2, 3, 4, 5)
    return sum(args)


(super_func(1, 2, 3, 4, 5))  # 15


def super_func2(*args, **kwargs):
    print(args)  # (1, 2, 3, 4, 5)
    print(kwargs)  # {'num1': 5, 'num2': 10}
    total = 0
    for item in kwargs.values():
        total += item
    return sum(args) + total


super_func2(1, 2, 3, 4, 5, num1=5, num2=10)  # 30
