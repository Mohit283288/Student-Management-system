# ==========================================
# STUDENT MANAGEMENT SYSTEM
# Python Only - Simple Project
# ==========================================

students = []



# 1. ADD STUDENT
def add_student():
    print("\n--- ADD STUDENT ---")

    roll = int(input("Enter roll number: "))

    # Check duplicate roll number
    for student in students:
        if student["roll"] == roll:
            print("Roll number already exists!")
            return

    name = input("Enter student name: ")

    python_marks = float(input("Enter Python marks: "))
    maths_marks = float(input("Enter Maths marks: "))
    science_marks = float(input("Enter Science marks: "))

    attendance = float(input("Enter attendance percentage: "))

    student = {
        "roll": roll,
        "name": name,
        "python": python_marks,
        "maths": maths_marks,
        "science": science_marks,
        "attendance": attendance
    }

    students.append(student)

    print("Student added successfully!")


# 2. VIEW ALL STUDENTS
def view_students():
    print("\n ALL STUDENTS")

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print(" ")
        print("Roll No :", student["roll"])
        print("Name    :", student["name"])
        print("Python  :", student["python"])
        print("Maths   :", student["maths"])
        print("Science :", student["science"])
        print("Attendance :", student["attendance"], "%")



# 3. SEARCH STUDENT

def search_student():
    print("\nSEARCH STUDENT")

    roll = int(input("Enter roll number: "))

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found!")
            print("Roll No  :", student["roll"])
            print("Name     :", student["name"])
            print("Python   :", student["python"])
            print("Maths    :", student["maths"])
            print("Science  :", student["science"])
            print("Attendance :", student["attendance"], "%")
            return

    print("Student not found.")


# 4. UPDATE STUDENT
def update_student():
    print("\nUPDATE STUDENT")

    roll = int(input("Enter roll number: "))

    for student in students:
        if student["roll"] == roll:

            print("Leave blank if you don't want to change a value.")

            name = input("Enter new name: ")

            if name != "":
                student["name"] = name

            marks = input("Enter new Python marks: ")
            if marks != "":
                student["python"] = float(marks)

            marks = input("Enter new Maths marks: ")
            if marks != "":
                student["maths"] = float(marks)

            marks = input("Enter new Science marks: ")
            if marks != "":
                student["science"] = float(marks)

            attendance = input("Enter new attendance: ")
            if attendance != "":
                student["attendance"] = float(attendance)

            print("Student updated successfully!")
            return

    print("Student not found.")


# 5. DELETE STUDENT
def delete_student():
    print("\n--- DELETE STUDENT ---")

    roll = int(input("Enter roll number: "))

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


# 6. RECORD ATTENDANCE
def record_attendance():
    print("\nRECORD ATTENDANCE")

    roll = int(input("Enter roll number: "))

    for student in students:
        if student["roll"] == roll:

            attendance = float(
                input("Enter attendance percentage: ")
            )

            student["attendance"] = attendance

            print("Attendance updated successfully!")
            return

    print("Student not found.")


# 7. VIEW ATTENDANCE
def view_attendance():
    print("\nATTENDANCE")

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print(
            student["roll"],
            "-",
            student["name"],
            "-",
            student["attendance"],
            "%"
        )


# 8. CALCULATE RESULT

def calculate_result():
    print("\n STUDENT RESULT")

    roll = int(input("Enter roll number: "))

    for student in students:
        if student["roll"] == roll:

            total = (
                student["python"]
                + student["maths"]
                + student["science"]
            )

            percentage = total / 3

            if percentage >= 90:
                grade = "A+"
            elif percentage >= 80:
                grade = "A"
            elif percentage >= 70:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 50:
                grade = "D"
            else:
                grade = "F"

            print("\nRESULT ")
            print("Name       :", student["name"])
            print("Roll No    :", student["roll"])
            print("Total      :", total)
            print("Percentage :", round(percentage, 2), "%")
            print("Grade      :", grade)

            return

    print("Student not found.")


# 9. COMPLETE STUDENT REPORT
def student_report():
    print("\n COMPLETE STUDENT REPORT")

    roll = int(input("Enter roll number: "))

    for student in students:
        if student["roll"] == roll:

            total = (
                student["python"]
                + student["maths"]
                + student["science"]
            )

            percentage = total / 3

            if percentage >= 90:
                grade = "A+"
            elif percentage >= 80:
                grade = "A"
            elif percentage >= 70:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 50:
                grade = "D"
            else:
                grade = "F"

            print("\n")
            print("       STUDENT REPORT")
            print("")
            print("Name       :", student["name"])
            print("Roll No    :", student["roll"])
            print("")
            print("Python     :", student["python"])
            print("Maths      :", student["maths"])
            print("Science    :", student["science"])
            print("")
            print("Total      :", total)
            print("Percentage :", round(percentage, 2), "%")
            print("Grade      :", grade)
            print("Attendance :", student["attendance"], "%")
            print("")

            return

    print("Student not found.")


# MAIN MENU

while True:

    print("\n")
    print("")
    print("       STUDENT MANAGEMENT SYSTEM")
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

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        record_attendance()

    elif choice == "7":
        view_attendance()

    elif choice == "8":
        calculate_result()

    elif choice == "9":
        student_report()

    elif choice == "10":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")