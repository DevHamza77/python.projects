students = [ "Harry Potter", "Hermione Granger", "Ron Weasley" ]

gryffindors = [{"name":student, "house":"Gryffindor"} for student in students]
print(gryffindors)

#[' Harry', ' Hermione', ' Ron']
# gryffindors = { student: "Gryffindor" for student in students }
# print(gryffindors)