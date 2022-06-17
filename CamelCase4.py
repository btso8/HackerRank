# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
inputData = [l.rstrip('\n\r') for l in sys.stdin.readlines()]
for line in inputData:
    word = ""
    upper = False
    if line[0] == "S":
        for val in line[4:]:
            if val.isupper():
                word += " " + val.lower()
            elif val.isalpha():
                word += val
    elif line[0] == "C" and line[2] == "M":
        for val in line[4:]:
            if val == " ":
                upper = True
            elif upper == True:
                word += val.upper()
                upper = False
            else:
                word += val
        word += "()"
    elif line[0] == "C" and line[2] == "C":
        firstVal = True
        for val in line[4:]:
            if val == " ":
                upper = True
            elif firstVal == True:
                word += val.upper()
                firstVal = False
            elif upper == True:
                word += val.upper()
                upper = False
            else:
                word += val
    elif line[0] == "C" and line[2] == "V":
        for val in line[4:]:
            if val == " ":
                upper = True
            elif upper == True:
                word += val.upper()
                upper = False
            else:
                word += val
    print(word.lstrip().rstrip())
