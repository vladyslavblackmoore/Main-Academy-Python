def list_intersection(list1, list2):
    list3 = []
    for list1 in list2:
        list3.append(list1)


my_list_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list_1 = [0, 2, 4, 6, 8]
print(list_intersection(my_list_2, my_list_1))
