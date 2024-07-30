class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def update_GPA(self):
        total_credits = sum(course.credits for course in self.courses_registered)
        if total_credits == 0:
            self.GPA = 0.0
        else:
            total_grade_points = sum(course.credits * course.grade for course in self.courses_registered)
            self.GPA = total_grade_points / total_credits

class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits
        self.grade = 0.0
