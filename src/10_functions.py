# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False


# Read a number from the keyboard
num = input("Enter a number: ")

num = int(num)


# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def number(int):
    if int % 2 == 0:
        print("Even!")
    else:
        print("Odd!")


number(num)