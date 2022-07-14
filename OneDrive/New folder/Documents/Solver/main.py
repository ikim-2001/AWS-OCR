import numpy as np

class Problem():


    def __init__(self):
        # initialize the problem, output, and correct fields
        # problem is an array of line by line of parsed
        # OCR output
        f = open('problem.txt', "r")
        self.text = f.readlines()
        self.problem = self.text[0]
        self.problem_left = self.problem.split("=")[0].split('+')
        self.problem_right = self.problem.split("=")[-1].split('+')
        self.output = self.text[-1]
        self.isCorrect = None
        self.unique_id = [{"vars": 0, "cons": 0},
                          {"vars": 0, "cons": 0}]
        self.variable = "X"
        # for i in range(len(self.problem)):
        #     if self.problem[i].isalpha():
        #         self.variable = self.problem[i]
        # clean out the '\n' in the end
        for j in range(len(self.problem_left)):
            self.problem_left[j] = self.problem_left[j].replace(" ", "")

        for i in range(len(self.problem_right)):
            if "\n" in (self.problem_right[i]):
                self.problem_right[i] = self.problem_right[i][:-1]
            self.problem_right[i] = self.problem_right[i].replace(" ", "")
        print("Start with: " + self.problem)
        print("Left hand: " + str(self.problem_left))
        print("Right hand: " + str(self.problem_right))



    def returnSolution(self):
        # for this, split function will be extremely helpful
        # AX = B
        # X = B / A
        case1_id = [{"vars": 1, "cons": 0},
                    {"vars": 0, "cons": 1}]

        # Case 2:
        # AX + B = C + D
        # AX = (C+D)-B
        # X = ((C+D)-B)/A
        case2_id = [{'vars': 1, 'cons': 1},
                    {'vars': 0, 'cons': 2}]


        # this function will call the findCase functions
        # and return a boolean given if the findCase's output
        # matches the last line of f.readlines()'s last few characters
        self.unique_id = self.countParams()
        print(self.unique_id)
        if self.unique_id == case1_id:
            # eventually change to move around terms (not yet)
            return int(self.problem_right[0])/int(self.problem_left[0][0])
        print(case2_id)
        print(self.countParams())

        if self.unique_id == case2_id:
            print("case")
            return (int(self.problem_right[0])+int(self.problem_right[1])-int(self.problem_left[1]))/int(self.problem_left[0][0])

    def countParams(self):
        # initialize a whole bunch of dictionaries in which we have
        # each case being represented by an array of two dictionaries
        # where each dictionary counts the number of variables and constants

        # iterate thru left
        for term in self.problem_left:
            for char in term:
                if char == self.variable:
                    self.unique_id[0]["vars"] += 1
            if term.isnumeric():
                self.unique_id[0]["cons"] += 1

        for term in self.problem_right:
            for char in term:
                if char == self.variable:
                    self.unique_id[1]["vars"] += 1
            if term.isnumeric():
                self.unique_id[1]["cons"] += 1
        return self.unique_id


print(Problem().returnSolution())