def add_student():
    name = input("Enter student name")
    skills = input("Enter skills (comma seprated): ")
    contact = input("Enter contact info: ")
    with open("data.txt", "a") as file: file.write(name + "|" + skills + "|" + contact + "\n")
    print("Student added Successfully ✅")
def search_student():
    skill = input("Enter skill to search").lower()
    found = False
    try:
        with open("data.txt","r") as file:
            for line in file:
                if skill in line.lower():
                    print(line.strip())
                    found = True
        if not found:
            print("No students found with this skill ❌")
    except FileNotFoundError:
        print("No Data file Found yet ❌")
def view_student():
    try:
        with open("data.txt", "r") as file:
            print("\n--- All Students---")
            for i, line in enumerate(file, start=1):
                print(f"{i}, {line.strip()}")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No Students found ❌")
def show_menu():
    print("\n--- student skill finder---")
    print("1. Add Student")
    print("2. search by skill")
    print("3. View All Students")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter Your Choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        view_student()
    elif choice == "4":
        print("Goodbye 👋")
        break
    else:
        print("invalid choice")