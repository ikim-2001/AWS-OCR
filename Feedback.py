from Checker import *
# use Checker().isCorSErect to display the lines in which there is
class Problem(Checker):
    def __init__(self):
        Checker.__init__(self)
        print("\n")
        self.lines = self.text
        self.no_slash_n()
        self.lines = self.instantiate_lines(self.lines)
        # bad line refers to the line in which person fucked up
        self.bad_line = self.iterate_lines(self.lines)



    # gets rid of that \n
    def no_slash_n(self):
        for i in range(len(self.lines)):
            self.lines[i] = self.parse(self.lines[i].replace("\n", ""))[0].replace(" ", "")



    # replace these lines from being strings to -> Line() struct type
    def instantiate_lines(self, array):
        print("Showing student's work:")
        for i in range(len(array)):
            array[i] = Line(array[i])
            print(array[i].content)
        print("\n")
        return array


    # iterates through the array and checks which part is wrong
    def iterate_lines(self, array):
        for i in range(len(array)):
            # is wrong if the answer is off by the nearest thousandth
            if abs(eval(array[i].left_side.replace("var", self.true_output)) - eval(array[i].right_side.replace("var", self.true_output))) >= 0.01:
                print(f"Feedback: You fucked up between:\n"
                      f"Line {int(i)} : {array[i-1].content}\n"
                      f"Line {int(i+1)}: {array[i].content}")
                return array[i].content
 
 


class Line():
    def __init__(self, content):
        self.content = content
        self.left_side = self.content.split("=")[0]
        self.right_side = self.content.split("=")[-1]

