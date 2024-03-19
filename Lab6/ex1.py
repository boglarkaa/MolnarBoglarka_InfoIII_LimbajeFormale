import re

format = re.compile(r"(1+00*1)+(1+00*1)(0+10*1)*(0+10*1)")

input = input("Enter string: ")
if not format.match(input):
    print("Incorrect input")
else:
    print("Correct input")

# correct example :
# 1001100101010101
# incorrect example:
# 10011001
