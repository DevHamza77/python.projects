def main():
    x = int(input("Enter a number: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
# def main() creates a function called main
def is_even(n):
    return True if n % 2 == 0 else False

# def is_even (n) creates a function that answers true if the number is divisible by 2
# if the condition is met it prints even 
# if the number is not divible by 2, it returns false and odd is printed