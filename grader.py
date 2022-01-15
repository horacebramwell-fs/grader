import sys

class Grader:
    def __init__(self):
        self.student_name = input("What is the student's name? : ")
        self.assignment_name = input("What is the assignment name? : ")
        self.grade = float(input("What is their grade in numbers? : "))
        self.get_grade()

    def get_grade(self):
        if (type(self.grade) != float):
            print("Invalid grade. Please try again.")
            self.__init__()
        elif (self.grade < 0 or self.grade > 100):
            print("Invalid grade. Please try again.")
            self.__init__()
        else:
            self.grade = self.grade
            self.calculate_letter_grade()
    
    def calculate_letter_grade(self):
        if (self.grade >= 90):
            self.letter_grade = "A"
        elif (self.grade >= 80):
            self.letter_grade = "B"
        elif (self.grade >= 70):
            self.letter_grade = "C"
        elif (self.grade >= 60):
            self.letter_grade = "D"
        else:
            self.letter_grade = "F"
        self.print_grade()

    def print_grade(self):
        print("{0}'s grade in {1} is {2} ({3})".format(self.student_name, self.assignment_name, self.grade, self.letter_grade))


grader = Grader()
