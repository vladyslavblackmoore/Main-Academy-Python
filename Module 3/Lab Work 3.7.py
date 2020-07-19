'''Generate two sets with not unique numbers and few symbols'''
mySet1 = set('3322privet')
mySet2 = set('4488773322pokast')

'''Print 1st set'''
print(f'1st set: {mySet1}')

'''Create tuple from intersection of first and second set'''
myTupleIntersection = tuple(mySet2.intersection(mySet1))
print(f'Intersection of first and second set: {myTupleIntersection}')

'''Create tuple from difference first and second set'''
myTupleDifference = tuple(mySet2.difference(mySet1))
print(f'Difference first and second set: {myTupleDifference}')

'''Slice first 3 symbols from first tuple'''
print(f'Slice first 3 symbols from first tuple: {myTupleIntersection[3:]}')

'''Print only symbols with numbers from second set'''
print(f'Only symbols with numbers from second set:', end=' ')
for i in mySet2:
    if i.isdigit():
        print(i, end=' ')

'''Reverse tuple using slice'''
print(f'\nOriginal Tuple: {myTupleDifference}')
print(f'Reverse: {myTupleDifference[-1:-len(myTupleDifference)-1: -1]}')

'''Convert both tuples into list'''
myList = list(mySet2) + list(mySet1)
print(f'Both tuples into list: {myList}')
