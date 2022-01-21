import sys

class Grader:
    def __init__(self):
        self.student_name = input("What is the student's name? : ")
        self.assignment_name = input("What is the assignment name? : ")
        self.score = float(input("What is the score for the assignment? : "))
        self.check_score()

    def check_score(self):
    # if score is greater than 100 or less than 0 then it is invalid
        if (self.score > 100) or (self.score < 0):
            print("Invalid score. Please try again.")
            self.score = float(input("What is the score for the assignment? : "))
            self.check_score()   
        else:
            self.print_grade()
        
    def get_grade(self):
        if (self.score >= 90):
            return "A"
        elif (self.score >= 80):
            return "B"
        elif (self.score >= 70):
            return "C"
        elif (self.score>= 60):
            return "D"
        else:
            return "F"

    def print_grade(self):
        print("{0}'s score on {1} is {2} ({3})".format(self.student_name, self.assignment_name, self.score, self.get_grade()))


grader = Grader()