# ask user for their name , name is a variable that will store the user's input
name=input("what is your name ? ")

# remove any leading or trailing whitespace from the name, strip stands for removing any whitespace 
name = name.strip()

# capitalize the first letter of the name, title stands for capitalizing the first letter  
name = name.title()

# code can minimized to one line by adding .strip and .title to the input(1st here) function
# user's first and second name can be splitted by first, last = name.split(" ")
# print(f" Hello, {first}") would be used for it

# say hello to the user, print stands for displaying the message to the user, f stands for formatted string which allows us to include the variable name in the message
print(f"Hello, {name}!")
