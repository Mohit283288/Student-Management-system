
# STUDENT MANAGEMENT SYSTEM

students = []

# 1. ADD STUDENT
def add_student():
    print("\n ADD STUDENT")

    r = int(input("Enter roll number: "))

    # Check duplicate roll number
    for s in students:
        if s["roll"] == r:
            print("Roll number already exists!")
            return

    n = input("Enter student name: ")

    python_marks = float(input("Enter Python marks: "))
    maths_marks = float(input("Enter Maths marks: "))
    science_marks = float(input("Enter Science marks: "))

    A = float(input("Enter attendance percentage: "))

    s = {
        "roll": r,
        "name": n,
        "python": python_marks,
        "maths": maths_marks,
        "science": science_marks,
        "attendance": A
    }

    students.append(s)

    print("Student added successfully!")


# 2. VIEW ALL STUDENTS
def view_students():
    print("\n ALL STUDENTS")

    if len(students) == 0:
        print("No students found.")
        return

    for s in students:
        print(" ")
        print("Roll No :", s["roll"])
        print("Name    :", s["name"])
        print("Python  :", s["python"])
        print("Maths   :", s["maths"])
        print("Science :", s["science"])
        print("Attendance :", s["attendance"], "%")


# 3. SEARCH STUDENT

def search_student():
    print("\nSEARCH STUDENT")

    r = int(input("Enter roll number: "))

    for s in students:
        if s["roll"] == r:
            print("\nStudent Found!")
            print("Roll No  :", s["roll"])
            print("Name     :", s["name"])
            print("Python   :", s["python"])
            print("Maths    :", s["maths"])
            print("Science  :", s["science"])
            print("Attendance :", s["attendance"], "%")
            return

    print("Student not found.")


# 4. UPDATE STUDENT
def update_student():
    print("\nUPDATE STUDENT")

    r = int(input("Enter roll number: "))

    for s in students:
        if s["roll"] == r:

            print("Leave blank if you don't want to change a value.")

            n = input("Enter new name: ")

            if n != "":
                s["name"] = n

            marks = input("Enter new Python marks: ")
            if marks != "":
                s["python"] = float(marks)

            marks = input("Enter new Maths marks: ")
            if marks != "":
                s["maths"] = float(marks)

            marks = input("Enter new Science marks: ")
            if marks != "":
                s["science"] = float(marks)

            A = input("Enter new attendance: ")
            if A != "":
                s["attendance"] = float(A)

            print("Student updated successfully!")
            return

    print("Student not found.")


# 5. DELETE STUDENT
def delete_student():
    print("\nDELETE STUDENT")

    r = int(input("Enter roll number: "))

    for s in students:
        if s["roll"] == r:
            students.remove(s)
            print("Student deleted successfully!")
            return

    print("Student not found.")


# 6. RECORD ATTENDANCE
def record_attendance():
    print("\nRECORD ATTENDANCE")

    r = int(input("Enter roll number: "))

    for s in students:
        if s["roll"] == r:

            A = float(
                input("Enter attendance percentage: ")
            )

            s["attendance"] = A

            print("Attendance updated successfully!")
            return

    print("Student not found.")


# 7. VIEW ATTENDANCE
def view_attendance():
    print("\nATTENDANCE")

    if len(students) == 0:
        print("No students found.")
        return

    for s in students:
        print(
            s["roll"],
            "-",
            s["name"],
            "-",
            s["attendance"],
            "%"
        )


# 8. CALCULATE RESULT

def calculate_result():
    print("\n STUDENT RESULT")

    r = int(input("Enter roll number: "))

    for s in students:
        if s["roll"] == r:

            total = (
                s["python"]
                + s["maths"]
                + s["science"]
            )

            p = total / 3

            if p >= 90:
                G = "A+"
            elif p >= 80:
                G = "A"
            elif p >= 70:
                G = "B"
            elif p >= 60:
                G = "C"
            elif p >= 50:
                G = "D"
            else:
                G = "F"

            print("\nRESULT ")
            print("Name       :", s["name"])
            print("Roll No    :", s["roll"])
            print("Total      :", total)
            print("Percentage :", round(p, 2), "%")
            print("Grade      :", G)

            return

    print("Student not found.")


# 9. COMPLETE STUDENT REPORT
def student_report():
    print("\n COMPLETE STUDENT REPORT")

    r = int(input("Enter roll number: "))

    for s in students:
        if s["roll"] == r:

            total = (
                s["python"]
                + s["maths"]
                + s["science"]
            )

            p = total / 3

            if p >= 90:
                G = "A+"
            elif p >= 80:
                G = "A"
            elif p >= 70:
                G = "B"
            elif p >= 60:
                G = "C"
            elif p >= 50:
                G = "D"
            else:
                G = "F"

            print("\n")
            print("       STUDENT REPORT")
            print("")
            print("Name       :", s["name"])
            print("Roll No    :", s["roll"])
            print("")
            print("Python     :", s["python"])
            print("Maths      :", s["maths"])
            print("Science    :", s["science"])
            print("")
            print("Total      :", total)
            print("Percentage :", round(p, 2), "%")
            print("Grade      :", G)
            print("Attendance :", s["attendance"], "%")
            print("")

            return

    print("Student not found.")


# MAIN MENU

while True:

    print("\n")
    print("")
    print("STUDENT MANAGEMENT SYSTEM")
    print("")

    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Record Attendance")
    print("7. View Attendance")
    print("8. Calculate Result")
    print("9. Complete Student Report")
    print("10. Exit")

    C = input("Enter your choice: ")

    if C == "1":
        add_student()

    elif C == "2":
        view_students()

    elif C == "3":
        search_student()

    elif C == "4":
        update_student()

    elif C == "5":
        delete_student()

    elif C == "6":
        record_attendance()

    elif C == "7":
        view_attendance()

    elif C == "8":
        calculate_result()

    elif C == "9":
        student_report()

    elif C == "10":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")