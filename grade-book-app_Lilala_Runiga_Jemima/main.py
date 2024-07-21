#!/usr/bin/python3

# Create the Student Class include documentation
class Student:
    def __init__(self, email, names, courses_registered, GPA):
        self.email = email
        self.names = names
        self.courses_registered = courses_registered
        self.GPA = GPA


# Create the Coursers class include documentattion
class Courses:
    def __init__(name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits

# Create the grade book class
def main():
    gradebook = GradeBook()
    While True
    display_menu()
    

    # Define the add_student method
    def add_student(self):
        email = input("Enter student's email: ")
        names = input("Enter student's name: ")
        new_student = Student(email, names)
        self.student_list.append(new_student)
    

    # Define the add_course() method
    def add_course(self):
        name = input("Enter course name: ")
        trimester = input("Enter course trimester: ")
        credits = int(input("Enter course credits: "))
        new_course = Course(name, trimester, credits)
        self.course_list.append(new_course)
    
    
    # Define the register_student_for_course() method
    def register_student_for_course(self):
        try:
            student_email = input("Enter student's email: ")
            course_name = input("Enter course name: ")

            student = next((s for s in self.student_list if s.email == student_email), None)
            course = next((c for c in self.course_list if c.name == course_name), None)

            if student is None:
                raise ValueError("Student not found")
            if course is None:
                raise ValueError("Course not found")

            student.register_for_course(course)
            print(f"Student {student.names} has been registered for course {course.name}")

        except ValueError as e:
            print(e)
    

    # Define the calculate_GPA() method


# Define the calculate_ranking() method

# Define the search_by_grade() method

# Define the generate_transcript() method create the main program

# Create instances of the Student and Course classes

# Create an example of the Grade Book class

# Display a menu of actions for the user to choose from
def display_menu():
    print(" Gradebook Application")
    print("\nMenu:")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Register Student for Course")
    print("4. Calculate Ranking")
    print("5. Search by Grade")
    print("6. Generate Transcript")
    print("7. Exit")

# Implement the chosen action using the Grade Book class methods

# Display the results of the selected action

#Main loop of The application
def main():
    gradebook = GradeBook()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student(gradebook)
        elif choice == '2':
            add_course(gradebook)
        elif choice == '3':
            register_student_for_course(gradebook)
        elif choice == '4':
            calculate_ranking(gradebook)
        elif choice == '5':
            search_by_grade(gradebook)
        elif choice == '6':
            generate_transcript(gradebook)
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

