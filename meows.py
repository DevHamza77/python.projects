def meow(n: int):
    for _ in range(n):
        print("Meow")

number:int = int(input("Number of meows: "))
meow(number)

# a function called meow has been introduced that take in argument 'n' which has to be an integer
# for _ in range creates a loop that wont stop until it has printed the no. of meows told