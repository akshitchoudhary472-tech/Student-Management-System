

import json
import os

DATA_FILE = "data/students.json"


def load_students():
    """Load student records from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read the student data file.")
        return []


def save_students(students):
    """Save student records to the JSON file."""
    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def calculate_grade(marks):
    """Return a grade based on marks out of 100."""
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


def add_student(students):
    print("\n--- Add Student ---")
    roll = input("Enter roll number: ").strip()

    if not roll:
        print("Roll number cannot be empty.")
        return

    if any(s["roll"] == roll for s in students):
        print("A student with this roll number already exists.")
        return

    name = input("Enter student name: ").strip()
    course = input("Enter course: ").strip()

    if not name or not course:
        print("Name and course cannot be empty.")
        return

    try:
        marks = float(input("Enter marks (0-100): "))
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Please enter a valid number for marks.")
        return

    student = {
        "roll": roll,
        "name": name,
        "course": course,
        "marks": marks
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!")


def view_students(students):
    print("\n--- Student Records ---")

    if not students:
        print("No student records found.")
        return

    print(f"{'Roll No.':<12}{'Name':<22}{'Course':<18}"
          f"{'Marks':<10}{'Grade'}")
    print("-" * 72)

    for student in students:
        grade = calculate_grade(student["marks"])
        print(
            f"{student['roll']:<12}"
            f"{student['name']:<22}"
            f"{student['course']:<18}"
            f"{student['marks']:<10.1f}"
            f"{grade}"
        )


def search_student(students):
    print("\n--- Search Student ---")
    roll = input("Enter roll number to search: ").strip()

    for student in students:
        if student["roll"] == roll:
            print("\nStudent found:")
            print("Roll Number:", student["roll"])
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])
            print("Grade:", calculate_grade(student["marks"]))
            return

    print("Student not found.")


def update_student(students):
    print("\n--- Update Student ---")
    roll = input("Enter roll number to update: ").strip()

    for student in students:
        if student["roll"] == roll:
            print("Leave a field blank to keep its current value.")

            name = input(f"Name [{student['name']}]: ").strip()
            course = input(f"Course [{student['course']}]: ").strip()
            marks_input = input(
                f"Marks [{student['marks']}]: "
            ).strip()

            if name:
                student["name"] = name

            if course:
                student["course"] = course

            if marks_input:
                try:
                    marks = float(marks_input)
                    if not 0 <= marks <= 100:
                        print("Marks must be between 0 and 100.")
                        return
                    student["marks"] = marks
                except ValueError:
                    print("Invalid marks. No changes saved.")
                    return

            save_students(students)
            print("Student record updated successfully!")
            return

    print("Student not found.")


def delete_student(students):
    print("\n--- Delete Student ---")
    roll = input("Enter roll number to delete: ").strip()

    for student in students:
        if student["roll"] == roll:
            confirm = input(
                f"Delete {student['name']}? (y/n): "
            ).strip().lower()

            if confirm == "y":
                students.remove(student)
                save_students(students)
                print("Student deleted successfully!")
            else:
                print("Deletion cancelled.")
            return

    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n==============================")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()