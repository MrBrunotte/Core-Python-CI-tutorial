# helper function to stop us from repeating ourselves, returns true or false depending whether the numbr is even or not
def is_even(number):
    return number % 2 == 0

def even_number_of_evens(numbers):
    """
    Comment out this and use Pythonic code or idiomatic Python!

    #removed checked for empty because evens == 0 covers that!
    evens = 0
    for n in numbers:
        if is_even(n):
            evens += 1
    
    if evens == 0:
        return False #! return false because the remainder of 2 / 0 is 0 (Modula 2 % 0 = 0)
    else:
        return is_even(evens)
    """
#Pythonic code or idiomatic Python!
    evens = sum([1 for n in numbers if is_even(n)])
    return False if evens == 0 else is_even(evens)

# Our set of test cases
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

# If all the test cases pass, print some successful info to the console to let
# the developer know
print("All tests passed!")
