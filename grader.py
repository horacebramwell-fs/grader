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
        #if grade is greater than 100 or less than 0 then it is invalid 
        if (self.grade > 100) or (self.grade < 0):
            return "Invalid Grade" + self.__init__()
        #if grade is between 0 and 100 then it is valid
        elif (self.grade >= 0) and (self.grade <= 100):
            if (self.grade >= 90):
                return "A"
            elif (self.grade >= 80):
                return "B"
            elif (self.grade >= 70):
                return "C"
            elif (self.grade >= 60):
                return "D"
            else:
                return "F"

    def print_grade(self):
        print("{0}'s grade in {1} is {2} ({3})".format(self.student_name, self.assignment_name, self.grade, self.calculate_letter_grade()))


grader = Grader()
grader.print_grade()