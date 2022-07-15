import itertools
hi = "2*(4*var-+2)+2*x-+2*(1*var-+var)"
og = []
hi = hi.split("*(")
for i in hi:
    og.append(i.split("-+"))
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
print(output)

# spiting terms consists of +, +-, *(, )

# import itertools
# a = [['a','b'], ['c']]
# print(list(itertools.chain.from_iterable(a)))