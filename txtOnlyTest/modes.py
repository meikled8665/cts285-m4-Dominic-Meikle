import random
import problems
import threading
import time

def ansChecker():
    probID = problems.genID()
    prob = problems.loadProb(probID)
    ans = problems.solveProb(prob)
    attC = 0
    userAns = ""

    print("Solve:")

    while userAns != ans and attC <= 2:
        try:
            userAns = int(input(f"{prob} = "))
            if userAns != ans:
                        attC += 1
        except ValueError:
            print("Invalid Input")

    if attC < 3:
        print(f"Correct\n Answer Was: {ans}")
    else:
        print(f"Max Attempts Reached\nCorrect Answer Was: {ans}")

    print(f"Problem ID: {probID}")

def numGuesser():
    num = random.randint(1, 100)
    h1 = 100
    h2 = 0
    guess = ""

    while h1 >= num:
        h1 = random.randint(1, 100)
    while h2 <= num:
        h2 = random.randint(1, 100)

    while guess != num:
        print(f"Number is between {h1} and {h2}")
        try:
            guess = int(input("Enter your guess: "))
            if guess != num:
                nH1 = random.randint(h1, num - 1)
                h1 = nH1

                nH2 = random.randint(num + 1, h2)
                h2 = nH2
        except ValueError:
            print("Invalid")

    print(f"\nCorrect, The Number Was {num}")

def memBank(bank):
    correct = 0
    sTime = time.perf_counter()
    for i in bank:
        prob = i[1]
        ans = problems.solveProb(prob)

        print(f"{i[0]} / {len(bank)}\nSolve:")
        userAns = input(f"{prob} = ").strip()
        try:
            if ans == "UNDEFINED":
                isCorrect = userAns.upper() == ans
            elif isinstance(ans, int):
                isCorrect = int(userAns) == ans
            else:
                isCorrect = float(userAns) == ans
        except ValueError:
            print("Invalid Input")
            isCorrect = False

        if isCorrect:
            correct += 1
    eTime = time.perf_counter() - sTime
    print(f"\nTotal Answered: {len(bank)}\nCorrect: {correct}\nTime: {eTime:.0f}")