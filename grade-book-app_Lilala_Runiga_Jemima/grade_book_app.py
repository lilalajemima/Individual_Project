#!/usr/bin/python3

from parent_class import *

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self):
        email = input("Enter student's email: ")
        names = input("Enter student's name: ")
        new_student = Student(email, names)
        self.student_list.append(new_student)
        print(f"Student {names} with email {email} has been added !")

    def add_course(self):
        name = input("Enter course name: ")
        trimester = input("Enter course trimester: ")
        credits = int(input("Enter course credits: "))
        new_course = Course(name, trimester, credits)
        self.course_list.append(new_course)
        print(f"Course {name} for trimester {trimester} with {credits} credits has been added !")

    def register_student_for_course(self):
        try:
            student_email = input("Enter student's email: ")
            course_name = input("Enter course name: ")

            student = next(
                (s for s in self.student_list if s.email == student_email), None)
            course = next(
                (c for c in self.course_list if c.name == course_name), None)

            if student is None:
                raise ValueError("Student not found")
            if course is None:
                raise ValueError("Course not found")

            student.courses_registered.append(course)
            print(
                f"Student {student.names} has been registered for course {course.name}")

        except ValueError as e:
            print(e)

    def calculate_GPA(self):
        for student in self.student_list:
            # GPA calculation logic here
            print(f"Student {student.names} has a GPA of {student.GPA:.2f}")

    def calculate_ranking(self):
        sorted_students = sorted(self.student_list, key=lambda s: s.GPA, reverse=True)
        for i, student in enumerate(sorted_students, 1):
            print(f"Rank {i}: {student.names} with GPA {student.GPA:.2f}")

    def search_by_grade(self):
        grade_threshold = float(input("Enter the GPA threshold to search by: "))
        for student in self.student_list:
            if student.GPA >= grade_threshold:
                print(f"Student {student.names} with GPA {student.GPA:.2f}")

    def generate_transcript(self):
        student_email = input("Enter student's email: ")
        student = next((s for s in self.student_list if s.email == student_email), None)

        if student:
            print(f"\nTranscript for {student.names}:")
            for course in student.courses_registered:
                print(f"Course: {course.name}, Credits: {course.credits}")
            print(f"GPA: {student.GPA:.2f}\n")
        else:
            print("Student not found.")
    
    def list_all_students(self):
        if not self.student_list:
            print("No students recorded.")
        else:
            print("List of all students:")
            for student in self.student_list:
                print(f"Name: {student.names}, Email: {student.email}")

    def list_all_courses(self):
        if not self.course_list:
            print("No courses recorded.")
        else:
            print("List of all courses:")
            for course in self.course_list:
                print(f"Name: {course.name}, Trimester: {course.trimester}, Credits: {course.credits}")

            
def display_menu():
    print("----------------------------------------------Gradebook Application--------------------------------------------------")
    print("\nMenu:")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Register Student for Course")
    print("4. Calculate Ranking")
    print("5. Search by Grade")
    print("6. Generate Student Transcript")
    print("7. List All Students")
    print("8. List All Courses")
    print("9. Exit the Application")

def main():
    gradebook = GradeBook()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            gradebook.add_student()
        elif choice == '2':
            gradebook.add_course()
        elif choice == '3':
            gradebook.register_student_for_course()
        elif choice == '4':
            gradebook.calculate_ranking()
        elif choice == '5':
            gradebook.search_by_grade()
        elif choice == '6':
            gradebook.generate_transcript()
        elif choice == '7':
            gradebook.list_all_students()
        elif choice == '8':
            gradebook.list_all_courses()
        elif choice == '9':
            print("Closing the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

