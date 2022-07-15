from sympy import symbols, solve, Eq


class Checker():
    def __init__(self):
        # initialize the problem, output, and correct fields
        # problem is an array of line by line of parsed
        # OCR output
        print("SUBMISSION\n")
        f = open('problems/problem1.txt', "r")
        self.text = f.readlines()
        self.problem = self.text[0].replace(" ", "")
        self.isCorrect = None
        # fixed for now heh
        self.variable = self.findvar()
        self.student_prob_ans = self.parse(self.problem)
        self.problem = self.student_prob_ans[0]
        self.student_output = self.student_prob_ans[-1]
        self.problem_left = self.problem.split("=")[0]
        self.problem_right = self.newlinesgone(self.problem.split("=")[-1])
        self.true_output = self.solve()
        self.isCorrect = self.verify()

    # returns new self.problem where coeffs are separated to
    # vars with a * (will do parenthessis later)

    def findvar(self):
        for char in self.text[0]:
            if char.isalpha():
                return char

    def newlinesgone(self, str):
        new_right = ""
        for i in range(len(str)):
            if str[i] == "\n":
                break
            new_right += str[i]
        return new_right

    # returns an array with the parsed problem as first element
    # and parsed answer as second element
    def parse(self, str):
        # print(f"Parsing: {str}")
        output = []
        new_str = ""
        # parse the problem
        # for coefficients and variables
        for i in range(len(str)):
            if str[i] == self.variable:
                # if there is a coefficient in front of variable
                if i > 0 and str[i - 1].isnumeric():
                    new_str += f"*var"
                else:
                    new_str += "var"
            elif str[i] == "(":
                # if there is a variable or number before '('
                if i > 0 and (str[i-1].isnumeric() or str[i-1].isalpha()):
                    new_str += "*("
                else:
                    new_str += "("
            elif str[i] == ")":
                # the ")" is not the last char and there is a number or variable after the str
                if i < len(str)-1:
                    if (str[i+1].isnumeric() or str[i+1].isalpha()):
                        new_str += ")*"
                    else:
                        new_str += ")"
                else:
                    new_str += ")"
            elif str[i] == "-":
                # changes the 2-x -> 2+-x; -2 -> +-2
                if i < len(str) - 1:
                    # edge case: -(2x+3) =
                    if str[i+1] == "(":
                        new_str += "-1*"
                    else:
                        new_str += "+-"
                else:
                    new_str += "+-"
            else:
                new_str += str[i]

        # parse the anwer
        answer = self.text[-1].split("=")[-1].strip()
        # print(f"Parsed expression: {new_str}")
        return [new_str, answer]

    def solve(self):
        # print(f"Solving: {self.problem}")
        var = symbols(self.variable)
        lhs = eval(self.problem_left)
        rhs = eval(self.problem_right)
        answer = str(solve(Eq(lhs, rhs), var)[0])
        return answer

    def verify(self):
        print(f"Student's Answer: {self.student_output}\n"
              f"Correct Answer: {self.solve()}")
        if self.true_output == self.student_output:
            print("Student is correct! :)")
            return True
        print("Student is incorrect! :(")
        return False