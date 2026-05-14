students =[
    {"name": "Harry Potter", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Hermione Granger", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Ron Weasley", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco Malfoy", "house": "Slytherin", "patronus": "None"},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=" - ")
    # square brackets represent a list whereas curl brackets represent a dictionary
    # In this case, where each student is a dictionary
    # in the last function, we are accessing the value of the key "name", "house", and "patronus" for each student 
    