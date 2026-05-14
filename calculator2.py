def main():
    x = int(input("What's x? "))
    print( "x squared is", square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()

# def main () means that a function called main has been made
# The programmer prompts the user to assign a value to 'x' which will be stored in the variable "x"
# A function called square has been intoduced that has the argument as "n"
# This function's sole purpose is to return the value of 'n' after multiplying it with itself
# The function on line 3 is interpreted at last because it did'nt have a value at first
# At last, main() is called