list1 = ["Aalu", "Hariom", "apple", "Santosh", "Harindra", "cherry", "Apple", "banana"]
# newList = []

# for x in list1:
#     if "A" in x:
#         newList.append(x)

# newList = [x for x in list1 if "A" in x]

# newList = [x for x in list1 if x != "Apple"]

# newList = [x for x in list1]

# newList = [x for x in range(5)]

# newList = [x for x in range(5) if x < 3]

# newList = [x.upper() for x in list1]

# newList = ["Python" for x in list1]

# newList = [x.lower() for x in list1]

# newList = ["Python".upper() for x in list1]

newList = [x if x != "Apple" else "Pyhon" for x in list1]

print(newList)
print(list1)
