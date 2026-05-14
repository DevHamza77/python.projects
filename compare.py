x = int(input("What's x? "))
y = int(input("What's y? "))
# above code requires the user to input a number and converts it to an integer using int() function
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
# above code compares x and y using if statements and prints the appropriate message
# or can also be used e.g. if x < y or x > y print (" x is not equal to y ")
# if x != y print (" x is not equal to y ") is the most concise way
