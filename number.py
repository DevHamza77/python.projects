while True:
    try:
        x = int(input("What's x ? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
        
print(f"x is {x}")

# while true creates an infinite loop that will end when user inputs a valid integer 
# this is because the user input a non number value causing function #6 to act 
# pass means to ignore the answer and repeat the question