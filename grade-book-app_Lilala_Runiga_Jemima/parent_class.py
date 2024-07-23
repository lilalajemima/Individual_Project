class Student:
    def __init__(self, email, names, courses_registered=None, GPA=0.0):
        self.email = email
        self.names = names
        self.courses_registered = courses_registered if courses_registered else []
        self.GPA = GPA


class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits
