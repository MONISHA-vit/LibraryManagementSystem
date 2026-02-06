# student_registration.py
# Initial existing code - Student Registration Module

students = []
def login(username, password):
    if username == "admin" and password == "1234":
        print("Login successful")
    else:
        print("Invalid credentials")

login("admin", "1234")

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


print("daily update test")

# Sample execution
add_student("Arun", 20, "BCA")
view_students()
