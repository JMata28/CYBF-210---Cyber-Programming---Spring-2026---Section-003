#Code obtained from: https://www.w3schools.com/python/python_sets.asp

#Creating a set
# thisset = {"apple", "banana", "cherry"}
# print(thisset) 

# Using the set() constructor to make a set:
# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)

# #Duplicate values will be ignored
# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)

#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
# thisset = {"apple", "banana", "cherry", True, 1, 2}
# print(thisset)

#Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:
# thisset = {"apple", "banana", "cherry", False, True, 0}
# print(thisset)

#Sets are useful to remove duplicates from other data structures like lists
# a = [ "house", "beach", "lake", "pool", "house"]
# b = set(a)
# print(b)