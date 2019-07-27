def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count

# one way to test this is to use the print() function (but this is not an automated test!)
print(count_upper_case("Hello World"))

# we automate the test by using the assert keyword
assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("&%##¤€$@") == 0, "Special characters"

# if the assert keyword throws an error, then the program stops so we can throw in a print at the end!
print("All tests passed!")
