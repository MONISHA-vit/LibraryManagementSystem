# student_registration.py
# Initial existing code - Student Registration Module

students = []
def login(username, password):
    if username == "admin" and password == "1234":
        print("Login successful")
    else:
        print("Invalid credentials")
        
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

print("Main and Login feature merged")

print("daily update1 test")
print("LOGIN VERSION")


# Sample execution
add_student("Arun", 20, "BCA")
view_students()
