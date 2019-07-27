# assert is a Python keyword! 
"""

"""

x = 2
y = 1

# we use the assert keyword to see if statement return true and if it does the program should execute as normal, otherwise we get an assertionError.

#! assert x < y, "x should be less than y"

# make the assertionError look nicer we do this:

assert x < y, "{0} should be less than {1}".format(x,y)

print(x + y)
