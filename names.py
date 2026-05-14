names = []
with open ("names.txt") as file:
    for line in file:
        names.append(line.strip())

for name in sorted(names):
    print(f"Hello, {name}!")

# names is a variable assigned to an empty list
# with open ( names.txt) opens the file and named as a variable file
# for line in file iterates through each line in the file
# names.append(line.strip()) adds the line to the names list after stripping whitespace
# for name in sorted(names) iterates through the sorted names list
# print(f"Hello, {name}!") prints a greeting for each name in the sorted names