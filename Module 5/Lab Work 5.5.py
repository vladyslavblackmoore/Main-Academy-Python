my_list = [1, 2, 3, 4, 5, 7]


def func(my_list):
    for i in my_list:
        yield my_list.index(i) + 1, i


for i in func(my_list):
    print(i)
