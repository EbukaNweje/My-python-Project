# list is a collection type in which values which are mutable(can b changed),
# it is given by [],they are ordered and allows duplicate valyes
#they are ordered in the sense that they are indexed unlike others e,g 1st index
items = ["chair", "table", "comb", "pen", "torchlight"]
pay = ["lie", "pink", "yel"]

# print(type(items))
# print(len(this list))

#adding an item to a list
# items.insert(3, "book")
# print(items)

#to add an item to end of list
# items.append("man")
# print(items)

#deleting an item from a list;del,remove,pop
# del items[4]
# print(items)

# items.remove("chair")
# print(items)

# items.pop(4)
# print(items)

#to get value at indicated index
# print(items[3])

#to get a range from where to start and end
# print(items[1:4])

# to get the value in front to the index indicates
# print(items[:4])

#to get from the indicated index to the end
# print(items[3:])

#to change item at indicated index
# items[2] = "apple"
# print(items)

#to change range of value
# items[2:5] = ["mare", "pine", "tin"]
# print(items)

#replacing of selectedvrange of index with other values
# items[1:3] = ["pine", "tick", "pay", "tin"]
# print(items)

#to add elements of one list to another
#extend allows one to add to any type of collection;be it tuple,set or dictionary
# pay.extend(items)
# print(pay)

#to empty a list
# items.clear()
# print(items)

#to print all items in list accordingly
# for y in items:
#     print(y)

#to sort items alphabetically
# items.sort()
# print(items)

#to combine 2 or more lists
# mmm = items + pay
# print(mmm)