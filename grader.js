const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// create a class called Grader
class Grader {
  constructor() {
    this.askName();
  }

  // ask for the student's name
  askName() {
    rl.question('What is your name? ', (answer) => {
      this.name = answer;
      this.askAssignment();
    });
  }

  // ask for the assignment name
  askAssignment() {
    rl.question('What is the name of the assignment? ', (answer) => {
      this.assignment = answer;
      this.askScore();
    });
  }

  // ask for the assignment score
  askScore() {
    rl.question('What is the score for the assignment? ', (answer) => {
      this.score = answer;

      // if score is not a number, return invalid score
      if (isNaN(this.score)) {
        console.log('Invalid. Please try again.');
        this.askScore();
      } else if (this.score > 100 || this.score < 0) {
        console.log('Invalid. Please try again.');
        this.askScore();
      } else {
        this.printGrade();
      }
    });
  }

  // calculate the grade
  calculateGrade() {
    // if score is between 0 and 100, return the letter grade
    if (this.score >= 90) {
      // return 'A';
      return '(A)';
    } else if (this.score >= 80) {
      // return 'B';
      return '(B)';
    } else if (this.score >= 70) {
      // return 'C';
      return '(C)';
    } else if (this.score >= 60) {
      // return 'D';
      return '(D)';
    } else {
      // return 'F';
      return '(F)';
    }
  }

  // print the student name, assignment name, and grade
  printGrade() {
    console.log(`${this.name}'s score on ${this.assignment} is ${this.score} ${this.calculateGrade()}`);
    rl.close();
  }
}

// create a new instance of the class
const newGrader = new Grader();
