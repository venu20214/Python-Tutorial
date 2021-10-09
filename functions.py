"""
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.
"""

# Creating a Function
def my_function():
  print("Hello from a function")

# Calling a Function
def m_function():
  print("Hello from a function")

m_function()

# Arguments
def y_function(fname):
  print(fname + " Refsnes")

y_function("Emil")
y_function("Tobias")
y_function("Linus")

# Number of Arguments
def function(fname, lname):
  print(fname + " " + lname)

function("Emil", "Refsnes")

# Arbitrary Arguments, *args
def f1(*kids):
  print("The youngest child is " + kids[2])

f1("Emil", "Tobias", "Linus")

# Keyword Arguments
def children(child3, child2, child1):
  print("The youngest child is " + child3)

children(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs
def kwrg(**kid):
  print("His last name is " + kid["lname"])

kwrg(fname = "Tobias", lname = "Refsnes")

# Default Parameter Value
def dfv(country = "Norway"):
  print("I am from " + country)

dfv("Sweden")
dfv("India")
dfv("Brazil")

# Passing a List as an Argument
def lg(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

lg(fruits)

