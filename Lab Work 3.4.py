'''Generate string with lowercase and uppercase alphabet plus numbers'''
str = 'Generate  3 string 1 with 2 Lowercase 4 and 5 Uppercase 6 alphabet 7 plus 8 numbers 9'
print(f'String: {str}')

'''Print 1st symbol of string'''
print(f'1st symbol: {str[0]}')

'''Print last symbol'''
print(f'Last symbol {str[len(str)-1]}')

'''Print 3rd from start and 3rd from the end'''
print(f'Symbol:\n3rd from start: {str[2]}\n3rd form the end: {str[-3]}')

'''Slice first 8 symbols'''
sliceStr = slice(8, len(str))
print(f'Slice first 8 symbol: {str[sliceStr]}')

'''Print only symbols with index, which divides on 3 without remaining'''
sliceStrStep = slice(0, len(str), 3)
print(f'Which divides on 3 without remaining: {str[sliceStrStep]}')

'''Print the symbol of the middle of the string text'''
middleValueStr = int(len(str)/2)
print(f'Symbol of the middle of the string text: {str[middleValueStr]}')

'''Reverse text using slice'''
sliceStrReverse = slice(-1, -len(str)-1, -1)
print(f'Reverse text: {str[sliceStrReverse]}')
