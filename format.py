import re 

name = input("What's your name? ").strip()
matches = re.search(r"^(.+),(.+)$", name)
                    
if matches:
   name= matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")

# A library called 're' has been imported that allows us access to all its functions 
#Programmer asks the user for his name and stores it in the variable 'name' and strips whitespace