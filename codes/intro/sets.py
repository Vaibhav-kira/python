# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.
# Duplicates Not Allowed
fruits = {"banana","apple","orange","kiwi"}
print(fruits)  # order cannot be prideicted
fruits = {"apple","apple"} # will only show one apple
print(fruits) 
fruits = {"banana","apple","orange","kiwi",15} # set can contatin deffrent datatypes
print("{} has a length {} ".format(fruits,len(fruits)))
fruits.add("melon")
print("{} has a length {} ".format(fruits,len(fruits)))
fruits2 = {"grapes","stawberry"}
fruits.update(fruits2)
print("{} has a length {} ".format(fruits,len(fruits)))
fruits.remove("apple") # if not present raises error 
# use pop insted
print("{} has a length {} ".format(fruits,len(fruits)))
# .union() 
