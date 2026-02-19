print("Student Grade Manager")

students = {}

while True:
    print("\n1. Add student")
    print("2. View students")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        students[name] = grade
        print("Student added!")

    elif choice == "2":
        if len(students) == 0:
            print("No students yet.")
        else:
            print("\nStudent List:")
            for name, grade in students.items():
                print(name, ":", grade)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
