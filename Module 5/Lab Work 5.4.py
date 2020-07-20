foo = [1, 2, 3, 4, 5]


# def isOdd(x):
#     return x % 2 == 1
#
#
# for f in foo:
#     if isOdd(f):
#         odd_foo.append(f)
#         print(odd_foo)


odd_foo = [i for i in foo if i % 2 == 1]
print(odd_foo)


odd_foo = list(filter(lambda i: (i % 2 == 1), foo))
print(odd_foo)
