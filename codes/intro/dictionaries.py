# key value pair ....
# index can be any data type
# dictionary is mutable
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict1 = {}
print(type(dict1))
file_counts = {"jpg":10,"txt":14,"csv":2,"py":23}
print(file_counts)
print(file_counts["csv"])
file_counts["cfg"] = 8
print(file_counts)
file_counts["csv"] = 98 # updation ....
print(file_counts)
del file_counts["cfg"]
print(file_counts)
for extention in file_counts:
    print(extention,end="-")
print()
for ext,amount in file_counts.items(): # items to get key value pair
    print("There are {} files with the extension -> .{}".format(amount,ext))
print(file_counts.keys()) # to get keys
print(file_counts.values()) # to get values