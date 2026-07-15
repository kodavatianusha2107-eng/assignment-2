students = {}


def add_student():
    roll_no = input("Enter Roll Number: ")

    if roll_no in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks: "))

    students[roll_no] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully!")


def display_students():
    if not students:
        print("No students found!")
        return

    print("\n--- Student Details ---")

    for roll_no, details in students.items():
        print("Roll Number:", roll_no)
        print("Name:", details["name"])
        print("Marks:", details["marks"])
        print("----------------------")


def search_student():
    roll_no = input("Enter Roll Number to search: ")

    if roll_no in students:
        print("Roll Number:", roll_no)
        print("Name:", students[roll_no]["name"])
        print("Marks:", students[roll_no]["marks"])
    else:
        print("Student not found!")


def update_marks():
    roll_no = input("Enter Roll Number: ")

    if roll_no in students:
        new_marks = float(input("Enter New Marks: "))
        students[roll_no]["marks"] = new_marks
        print("Marks updated successfully!")
    else:
        print("Student not found!")


def delete_student():
    roll_no = input("Enter Roll Number to delete: ")

    if roll_no in students:
        del students[roll_no]
        print("Student deleted successfully!")
    else:
        print("Student not found!")


def find_topper():
    if not students:
        print("No students found!")
        return

    topper = max(students, key=lambda roll: students[roll]["marks"])

    print("\n--- Topper ---")
    print("Roll Number:", topper)
    print("Name:", students[topper]["name"])
    print("Marks:", students[topper]["marks"])


def find_average_marks():
    if not students:
        print("No students found!")
        return

    total = sum(student["marks"] for student in students.values())
    average = total / len(students)

    print("Average Marks:", average)


def count_students():
    print("Total Students:", len(students))


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Find Topper")
    print("7. Find Average Marks")
    print("8. Count Students")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_marks()

    elif choice == 5:
        delete_student()

    elif choice == 6:
        find_topper()

    elif choice == 7:
        find_average_marks()

    elif choice == 8:
        count_students()

    elif choice == 9:
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")
