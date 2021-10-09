# Set
# Sets are used to store multiple items in a single variable.
# A set is a collection which is both unordered and unindexed

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# Get the Length of a Set
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

# type()
myset = {"apple", "banana", "cherry"}
print(type(myset))

# The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

