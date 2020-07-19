import string

'''Generate list with lowercase and uppercase alphabet plus numbers'''
myList = list(string.ascii_letters + string.digits)
print(f'My list: {myList}')
'''Print 1st symbol of list'''
print(f'1st symbol of list: {myList[0]}')

'''Print last symbol'''
print(f'Last symbol: {myList[-1]}')

'''Print 3rd from start and 3rd from the end'''
print(f"3rd from start: {myList[2]}\n3rd from the end: {myList[-3]}")

'''Slice first 10 symbols'''
print(f'Slice first 10: {myList[10:]}')

'''Print only symbols with index, which divides on 2 without remaining'''
print(f'Which divides on 2 without remaining: {myList[::2]}')

'''Print only integer values from list'''
print('Only integer values:', end=' ')
for i in myList:
    if i.isdigit():
        print(i, end=' ')

'''Reverse list using slice'''
print(f'\nReverse list: {myList[-1: -len(myList)-1: -1]}')

'''Convert base list into string'''
myString = ' '.join(myList)
print(f'Convert base list into string: {myString}')
