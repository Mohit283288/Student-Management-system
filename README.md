# Student Management System

# 1. Project Title

**Student Management System**

# 2. Project Overview

The **Student Management System** is a Python-based console application designed to manage student academic information in a simple and organized way.

The system allows the user to add student details, view all students, search for a particular student, update information, delete student records, manage attendance, calculate academic results, and generate a complete student report.

The project demonstrates practical use of Python programming concepts such as:

* Variables
* Data types
* Lists
* Dictionaries
* Functions
* Loops
* Conditional statements
* User input
* Searching
* Updating and deleting data
* Mathematical calculations

The project does not use CSV files, databases, or external Python libraries. Student information is stored temporarily using a Python list of dictionaries.

# 3. Problem Statement

Managing student information manually can be time-consuming and may make it difficult to quickly find academic records.

The purpose of this project is to provide a simple computerized system that can manage student details, marks, attendance, and results through a menu-driven Python application.

# 4. Objectives

The main objectives of the project are:

* To create a simple student management system using Python.
* To store student information using Python data structures.
* To provide options for adding, viewing, searching, updating, and deleting students.
* To record and display attendance.
* To calculate total marks and percentage.
* To assign grades according to percentage.
* To generate a complete student report.
* To demonstrate practical implementation of Python programming concepts.

# 5. Scope of the Project

The project is intended for basic academic record management.

The system can manage:

* Student roll number
* Student name
* Python marks
* Maths marks
* Science marks
* Attendance percentage
* Total marks
* Percentage
* Grade
* Complete student report

The project is suitable for a small-scale classroom or academic demonstration.

# 6. Features

# 6.1 Add Student

The user can add a new student by entering:

* Roll number
* Student name
* Python marks
* Maths marks
* Science marks
* Attendance percentage

The system also checks whether the roll number already exists.

# 6.2 View All Students

The system displays the details of all students stored in the program.

It displays:

* Roll number
* Name
* Python marks
* Maths marks
* Science marks
* Attendance

# 6.3 Search Student

The user can enter a roll number to search for a particular student.

If the student exists, the system displays the student's stored information.

# 6.4 Update Student

The user can update existing student information.

The following information can be updated:

* Name
* Python marks
* Maths marks
* Science marks
* Attendance

The user can leave a field blank if they do not want to change that value.

# 6.5 Delete Student

The user can delete a student record by entering the student's roll number.

# 6.6 Record Attendance

The system allows the user to update the attendance percentage of a particular student.

# 6.7 View Attendance

The attendance section displays the roll number, student name, and attendance percentage of all students.

# 6.8 Calculate Result

The system calculates the total marks and percentage.

```text
Total = Python + Maths + Science
Percentage = Total Marks / 3
```

The system then assigns a grade based on the percentage.

# 6.9 Complete Student Report

The complete report displays:

* Student name
* Roll number
* Python marks
* Maths marks
* Science marks
* Total marks
* Percentage
* Grade
* Attendance percentage

# 7. Grading System

| Percentage  | Grade |
| ----------- | ----- |
| 90 or above | A+    |
| 80–89       | A     |
| 70–79       | B     |
| 60–69       | C     |
| 50–59       | D     |
| Below 50    | F     |

# 8. Technologies and Tools Used

# Programming Language

**Python 3**

# Python Concepts Used

* Lists
* Dictionaries
* Functions
* `if-elif-else`
* `for` loops
* `while` loops
* `input()`
* `print()`
* Arithmetic operations
* Searching
* Updating records
* Deleting records

# Data Storage

The project uses a Python list containing dictionaries to temporarily store student records.

The main logic now uses shorter local variable names such as `r`, `n`, `s`, `A`, `p`, `G`, and `C`, while the dictionary keys remain descriptive for clarity.

Example:

```python
students = []

r = int(input("Enter roll number: "))
n = input("Enter student name: ")
A = float(input("Enter attendance percentage: "))

s = {
    "roll": r,
    "name": n,
    "python": 85,
    "maths": 78,
    "science": 90,
    "attendance": A
}

students.append(s)
```

# External Libraries

No external Python libraries are required.

# 9. Project File

```text
Student-Management-System/
│
├── python.py
└── README.md
```

# 10. System Workflow

```text
Start
  ↓
Display Main Menu
  ↓
Select Operation
  ↓
Add / View / Search / Update / Delete
  ↓
Attendance Management
  ↓
Calculate Result
  ↓
Generate Student Report
  ↓
Display Output
  ↓
Return to Main Menu
  ↓
Exit
```

# 11. Requirements

To run this project, the following are required:

* Python 3.x
* Any Python IDE or code editor
* Command Prompt or Terminal

No database or external library is required.

# 12. Installation

# Step 1: Install Python

Install Python 3.x on your computer.

# Step 2: Download the Project

Download or clone the project from the GitHub repository.

```bash
git clone <your-github-repository-link>
```

# Step 3: Open the Project

Open the project folder using:

* VS Code
* PyCharm
* IDLE
* Any other Python-compatible editor

# 13. How to Run the Project

Open the terminal in the project folder.

Run:

```bash
python python.py
```

If your system uses `python3`, run:

```bash
python3 python.py
```

After running the program, the following menu will appear:

```text
STUDENT MANAGEMENT SYSTEM

1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Record Attendance
7. View Attendance
8. Calculate Result
9. Complete Student Report
10. Exit
```

Enter the number corresponding to the operation you want to perform.

# 14. Error Handling

The program handles common invalid operations by displaying appropriate messages.

Examples include:

* Duplicate roll number
* Student not found
* Invalid menu choice
* Empty student list
* Searching for a non-existing student

The program checks whether a student exists before performing operations such as searching, updating, deleting, recording attendance, and calculating results.

# 15. Limitations

* Student data is stored only temporarily in memory.
* Data is lost when the program is closed.
* The project does not currently use a database.
* The application is console-based.
* The current implementation is designed for basic student record management.

# 16. Future Enhancements

The project can be improved in the future by adding:

* A graphical user interface
* Permanent data storage
* Database connectivity
* Login and authentication
* More subjects
* Multiple attendance records
* Student performance charts
* Exportable reports
* Teacher and administrator accounts

# 17. Conclusion

The **Student Management System** is a simple Python project that demonstrates how programming concepts can be applied to solve a practical academic problem.

The system provides student record management, attendance management, result calculation, and report generation through a menu-driven interface.

The project demonstrates the use of Python data structures, functions, loops, conditional statements, searching, updating, deleting, and calculations in a practical application.

# 18. References

* Python Documentation: https://docs.python.org/
* VITyarthi – Build Your Own Project Guidelines
