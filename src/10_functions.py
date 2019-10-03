# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
is_even(num)

    
# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def is_even_string(n):
    if n % 2 == 0:
        print("Even!")
    else:
        print("Odd")
is_even_string(num)