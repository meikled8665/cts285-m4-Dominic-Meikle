import random

def genID():
    op = random.randint(0, 3)
    num1 = hex(random.randint(0, 99))
    num2 = hex(random.randint(0, 99))

    num1 = str(f"{num1[2:]}")
    num2 = str(f"{num2[2:]}")

    id = f"{op}{len(num1)}{num1}{len(num2)}{num2}"

    return id
    

def loadProb(id):
    strID = str(id)

    opCode = int(strID[0])

    len1 = int(strID[1])
    num1H = strID[2 : 2 + len1]

    len2I = 2 + len1
    len2 = int(strID[len2I])
    num2H = strID[len2I + 1 : len2I + 1 + len2]

    num1 = int(num1H, 16)
    num2 = int(num2H, 16)
    

    operators = {0: "+", 1: "-", 2: "*", 3: "/"}
    if opCode in operators:
        op = operators[opCode]
        return f"{num1} {op} {num2}"
    else:
        print(f"\nUnable To Load {id}: Invalid ID")
        return None

def solveProb(prob):
    operators = {"+", "-", "*", "/"}

    for i in operators:
        if i in prob:
            index = prob.index(i)
            num1 = int(prob[:index])
            num2 = int(prob[index + 1:])

            if i == "+":
                ans = num1 + num2
            elif i == "-":
                ans = num1 - num2
            elif i == "*":
                ans = num1 * num2
            elif i == "/":
                if num2 == 0:
                    ans = "UNDEFINED"
                else:
                    ans = num1 / num2
            else:
                print("Could Not Solve: Invalid Operator")
                return None

    return ans
