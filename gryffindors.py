students = [
    {"name": "Harry Potter", "house": "Gryffindor"},
    {"name": "Hermione Granger", "house": "Gryffindor"},
    {"name": "Ron Weasley", "house": "Gryffindor"},
    {"name": "Malfoy", "house": "Slytherin"}
]

def is_gryffindor(student):
    return student["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)

for gryffindor in gryffindors:
    print(gryffindor["name"])

# A list has been given that contains dictionaries with information about students
# A function called is_gryffindor has been introduced that takes in the argument 'student'
# As indicated, its sole purpose is to return every student has the house 'Gryffindor'
# is_gryffindor function is used in the list 'students'
# filter function is also used that filters the name of every student in the house ' Gryffindor'
# The names are then stored in the variable ' gryffindors '
# for loop is used that will print every student in gryffindor from the variable ' gryffindors '