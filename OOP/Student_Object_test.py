from Class_Test import Student

students = []

for i in range(5):
    students.append(Student(input("ID:\n"),input("Name:\n"),input("Course:\n"),input("Mark:\n")))
    print(students[i].return_attributes())

    if students[i].setMark():
        students[i].printGrade()
