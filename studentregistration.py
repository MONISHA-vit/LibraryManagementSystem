# student_registration.py
# Initial existing code - Student Registration Module

students = []

def add_student(name, age, course):
    student = {
        "name": name,
        "age": age,
        "course": course
    }
    students.append(student)
    print("Student added successfully")

def view_students():
    if len(students) == 0:
        print("No students registered")
    else:
        print("Registered Students:")
        for s in students:
            print(s["name"], "-", s["course"])

students = []

def add_student(name, age):
    student = {"name": name, "age": age}
    students.append(student)
    print("Student added successfully")

def view_students():
    for s in students:
        print(s)

print("daily update test")

# Sample execution
add_student("Arun", 20, "BCA")
view_students()
