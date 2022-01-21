# create a class called grader
class Grader
    def initialize
        # get the name of the student
        puts "What is the student's name?"
        @name = gets.chomp
        #  get the name of the assignment
        puts "What is the assignment name?"
        @assignment = gets.chomp
        # get the score in numbers
        puts "What is the score?"
        @score = gets.chomp.to_i
        # call the display method
        display
    end

    # create a method called grade that returns the grade
    def grade
        # if the score if greater than 100 and less than 0 return invalid grade and exit the program
        if @score > 100 || @score < 0
            puts "Invalid score. Please try again."
            exit
        # if the score is greater than or equal to 90 return A
        elsif @score >= 90
            return "A"
        # if the score is greater than or equal to 80 return B
        elsif @score >= 80
            return "B"
        # if the score is greater than or equal to 70 return C
        elsif @score >= 70
            return "C"
        # if the score is greater than or equal to 60 return D
        elsif @score >= 60
            return "D"
        # if the score is less than 60 return F
        else
            return "F"
        end
    end

    # create a method called display that displays the student's name, assignment, and score
    def display
        # concatenate the name, assignment, and score
        puts "#{@name}'s score on #{@assignment} is #{@score} (#{grade})"
    end
end

# create a new instance of the class
student = Grader.new



