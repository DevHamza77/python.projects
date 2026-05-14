while True:
    n = int(input(" Whats your number ?"))
    if n > 0:
        break
# while true starts an infinite loop, and it wont break until the user enters a positive number
for _ in range(n):
    print("Meow")
    # the for loop will run n times, and it will print "Meow" each time