"""
WEEK 4 LAB SUBMISSION
Name: SANA ULLAH
ID: 42051
University: FUUAST Islamabad
Date: March 14, 2026
"""

# ====================================
# LAB 1: Student Record System
# ====================================

def add_student():
    """Add student records"""
    students = []
    total = int(input("How many students? "))
    
    for i in range(total):
        print(f"\nStudent {i+1}:")
        roll = input("Roll Number: ")
        name = input("Name: ")
        marks = input("Marks: ")
        students.append([roll, name, marks])
    
    return students

def show_students(students):
    """Show all students"""
    print("\nSTUDENT RECORDS")
    print("-"*20)
    for s in students:
        print(f"Roll: {s[0]}, Name: {s[1]}, Marks: {s[2]}")

# ====================================
# LAB 2: Git Commands
# ====================================

git_commands = """
Git Commands:
------------
git init
git add .
git commit -m "message"
git push origin main
git pull origin main
"""

# ====================================
# LAB 3: Error Handling
# ====================================

def divide_numbers(a, b):
    """Safe division"""
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"
    except:
        return "Error!"

# ====================================
# LAB 4: Calculator (Debugged)
# ====================================

def calculator():
    """Simple calculator"""
    print("\n1. Add")
    print("2. Subtract") 
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Choice (1-4): ")
    n1 = float(input("First number: "))
    n2 = float(input("Second number: "))
    
    if choice == '1':
        print(f"Result: {n1 + n2}")
    elif choice == '2':
        print(f"Result: {n1 - n2}")  # Fixed
    elif choice == '3':
        print(f"Result: {n1 * n2}")
    elif choice == '4':
        if n2 == 0:  # Fixed
            print("Error: Division by zero!")
        else:
            print(f"Result: {n1 / n2}")  # Fixed

# ====================================
# Main Program
# ====================================

def main():
    print("="*40)
    print("WEEK 4 SUBMISSION")
    print("="*40)
    print("Name: SANA ULLAH")
    print("ID: 42051")
    print("University: FUUAST Islamabad")
    
    while True:
        print("\n1. Lab 1 - Student Records")
        print("2. Lab 2 - Git Info")
        print("3. Lab 3 - Error Handling")
        print("4. Lab 4 - Calculator")
        print("5. Exit")
        
        ch = input("\nEnter choice: ")
        
        if ch == '1':
            s = add_student()
            show_students(s)
        elif ch == '2':
            print(git_commands)
        elif ch == '3':
            print("10/2 =", divide_numbers(10, 2))
            print("10/0 =", divide_numbers(10, 0))
        elif ch == '4':
            calculator()
        elif ch == '5':
            print("Bye!")
            break
        else:
            print("Invalid choice!")

# Run program
if __name__ == "__main__":
    main()
