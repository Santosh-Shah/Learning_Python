# python list
#  items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# thislist = ["Santosh", "Hariom", "cherry"]
# print(thislist)

# duplicate
# thislist = ["Hariom", "Santosh", "Hariom", "cherry"]
# print(thislist)

# find length of list
# thisList = ["Hariom", "Santosh", "Hariom", "cherry"]
# print(len(thisList))

# list items can be of any data types
# list1 = ["Hariom", "Santosh", "Hariom", "cherry"]
# list2 = [True, True, False, False]
# list3 = [1, 5, "Apples", True, 4.25, 'c']
# print("list1 length and datas: ", len(list1), " ", list1)
# print("list2 length and datas: ", len(list2), " ", list2)
# print("list3 length and datas: ", len(list3), " ", list3)


# it will show the type of lists: whether it is tuples, list, set or dictionary
# print(type(list3))

# we can also create list constructor as well
# list4 = list(("Ram", "Sita", "Laxman"))
# print(list4)


# list1 = ["Hariom", "Santosh", "Harindra", "cherry", "apple", "banana"]
# print(list1[1])
# print(list1[-1])   # run in reverse order

# both below show error "list index out of range"
# print(list1[-6])
# print(list1[6])

# it will print index 2, 3, 4 not 5 index's data
# print(list1[2:5])

# it will print from index's 0 data < index's 5 data
# print(list1[:5])

# it will print from index's 2 data = last index's  data
# print(list1[2:])

# remember -1 means last index
# it will print -5's index to < -1's index(-1 is not included)
# print(list1[-5:-1])


# remember apple and Apple has different meaning
# check data exits or not using -in- keyword
# list1 = ["Hariom", "Santosh", "Harindra", "cherry", "apple", "banana"]
# if "apple" in list1:
#     print("Apple exits")
# else:
#     print("Apple not exits")
