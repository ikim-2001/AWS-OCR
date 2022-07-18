from Checker import *
from Feedback import *
import itertools
import string

class Rules(Problem):
    def __init__(self):
        Problem.__init__(self)
        if self.bad_line:
            self.bad_left = self.bad_line.split("=")[0]
            self.bad_right = self.bad_line.split("=")[-1]
            self.bad_left_terms = self.classify_terms(self.get_terms(self.bad_left), "left")
            self.bad_right_terms = self.classify_terms(self.get_terms(self.bad_right), "right")
            # initialize arrays of Term elements for left and right sides
            self.left_array = self.hash(self.bad_left, self.bad_left_terms)
            self.left_hashed, self.bad_left_terms = self.left_array[0], self.left_array[1]
            self.right_array = self.hash(self.bad_right, self.bad_right_terms)
            self.right_hashed, self.bad_right_terms = self.right_array[0], self.right_array[1]
            self.plug_neg_one()
            # print('\n')
            # print(self.bad_left)
            # print(self.left_hashed)
            # print('\n')
            # print(self.bad_right)
            # print(self.right_hashed)
            print('\n')



    # atrocious syntax right now but will update eventually
    def get_terms(self, str):
        hi = str
        og = []
        hi = hi.split("*(")
        for i in hi:
            og.append(i.split("+"))
        lst = []
        for i in og:
            lst.append(i)
        lst = list(itertools.chain.from_iterable(lst))
        og2 = []

        for i in lst:
            og2.append(i.split(')'))
        new = list(itertools.chain.from_iterable(og2))
        og3 = []
        for i in new:
            og3.append(i.split("+"))
        new = list(itertools.chain.from_iterable(og3))
        output = []
        for i in new:
            if i != "":
                output.append(i)
        return output

    def classify_terms(self, array, side):
        output = []
        for i in range(len(array)):
            output.append(Term(array[i], side))
        return output

    # assign each term to a unique class
    # takes in the string for the bad line's respective side and array of terms (with ID's uninitialized)
    # returns both the new_str with terms replaced as IDs, as well as the term classes encoded with IDs
    def hash(self, sides_string, terms):
        alphabet = string.ascii_uppercase[::-1]
        for i in range(len(terms)):
            terms[i].ID = alphabet[i]
            # print(f"Replacing {terms[i].content} with {terms[i].ID}\n")
            sides_string = sides_string.replace(terms[i].content, terms[i].ID, 1) # one indicates to only replace first occurence
        return [sides_string, terms]

    def plug_neg_one(self):
        # replace every a, b, c, d, etc. with actual values
        left_count, right_count = 0, 0
        while left_count < len(self.bad_left_terms):
            left_str, right_str = self.left_hashed, self.right_hashed
            print(f"Count {left_count}: {left_str} = {right_str}")

            # for each iteration, run a for loop that replaces each unique term ID with its original contents
            # if i (in for loop counter) == left_count, the pointer for the specific array's index, that means to
            # negate that content's value and call solve to see if it's vaid
            for i in range(len(self.bad_left_terms)):
                if i == left_count:
                    # replaces letter with the negative of correponding content field of that term
                    left_str = left_str.replace(self.bad_left_terms[i].ID, "-1*"+self.bad_left_terms[i].content)
                else:
                    left_str =  left_str.replace(self.bad_left_terms[i].ID, self.bad_left_terms[i].content)
            for j in range(len(self.bad_right_terms)):
                right_str = right_str.replace(self.bad_right_terms[j].ID, self.bad_right_terms[j].content)
            # call the compare left right function to see if adding a -1 made a difference
            print(f"{left_str} = {right_str}")
            if self.is_equal(left_str, right_str) and len(self.bad_left_terms) > 1:
                print(f"Sign error with: {self.bad_left_terms[left_count].content}")
                print("Should have been: " "-" + self.bad_left_terms[left_count].content)
                return
            else:
                print(f"Multiply by -1 on either side for right answer")
            left_count += 1
        while right_count < len(self.bad_right_terms):
            left_str, right_str = self.left_hashed, self.right_hashed
            print(f"Count {right_count}: {left_str} = {right_str}")
            # for each iteration, run a for loop that replaces each unique term ID with its original contents
            # if i (in for loop counter) == left_count, the pointer for the specific array's index, that means to
            # negate that content's value and call solve to see if it's vaid
            for i in range(len(self.bad_right_terms)):
                if i == right_count:
                    # replaces letter with the negative of correponding content field of that term
                    right_str = right_str.replace(self.bad_right_terms[i].ID, "-1*"+self.bad_right_terms[i].content)
                else:
                    right_str =  right_str.replace(self.bad_right_terms[i].ID, self.bad_right_terms[i].content)
            for j in range(len(self.bad_left_terms)):
                left_str = left_str.replace(self.bad_left_terms[j].ID, self.bad_left_terms[j].content)
            # call the compare left right function to see if adding a -1 made a difference
            print(f"{left_str} = {right_str}")
            if self.is_equal(left_str, right_str) and len(self.bad_left_terms) > 1:
                print(f"Sign error with: {self.bad_right_terms[right_count].content}")
                print("Should have been: " "-" + self.bad_right_terms[right_count].content)
                return
            else:
                print(f"Multiply by -1 on either side for right answer")
            right_count += 1


    def is_equal(self, left, right): # returns boolean True if abs(left-right) < 0.001
        print("is_equal is called\n")
        left = left.replace("var", self.true_output)
        right = right.replace("var", self.true_output)
        return abs(eval(left)+eval(right)) < 0.01





class Term():
    # two parameters that we can pass in (side, content)
    def __init__(self, content, side):
        self.content = content
        self.side = side
        # the ID is initialied as none but will be replaced with its unique val later
        self.ID = None


Rules()