
import re
test = False



def prepInput(path):
    lines = open(path, 'r').readlines()
    return lines



def one(path: str):
    result = 0
    for line in prepInput(path):
        matches = re.findall(r"(mul\(\d{1,3},\d{1,3}\))",line)
        for match in matches:
            a,b = match.strip("mul(").strip(")").split(",")
            result += int(a)*int(b)
    print(result)

def two(path: str):
    result = 0
    enabled = True
    for line in prepInput(path):
        matches = re.findall(r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))",line)
        for match in matches:
            if match[1]:
                enabled = True
            elif match[2]:
                enabled = False
            elif match[0] and enabled:
                #print(match)
                a,b = match[0].strip("mul(").strip(")").split(",")
                result += int(a)*int(b)
    print(result)

def main():
    current = __file__.strip('.py')
    if test:
        one(current+"a.txt")
    else:
        print("Calling Toby")
        one(current+"b.txt")
        two(current+"b.txt")
        print("Calling Freya")
        one(current+"c.txt")
        two(current+"c.txt")
main()