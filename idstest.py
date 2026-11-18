import random


def genID():
    op = random.randint(0, 3)
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)

    if op == 0:
        op2 = "+"
        result = num1 + num2
    elif op == 1:
        op2 = "-"
        result = num1 - num2
    elif op == 2:
        op2 = "*"
        result = num1 * num2
    elif op == 3:
        op2 = "/"
        result = num1 / num2 if num2 != 0 else 0

    id_str = f"{op}{num1}{num2}"
    problem = f"{num1} {op2} {num2} = {result}"
    print(f"problem: {problem}")
    print(f"id: {id_str}")


def checkID(id_str: str):
    if len(id_str) < 3:
        print("Invalid ID format")
        return

    op_code = int(id_str[0])
    num1 = int(id_str[1])
    num2 = int(id_str[2])

    if op_code == 0:
        op2 = "+"
        result = num1 + num2
    elif op_code == 1:
        op2 = "-"
        result = num1 - num2
    elif op_code == 2:
        op2 = "*"
        result = num1 * num2
    elif op_code == 3:
        op2 = "/"
        result = num1 / num2 if num2 != 0 else 0

    problem = f"{num1} {op2} {num2} = {result}"
    print(f"id: {id_str}")
    print(f"problem: {problem}")


def main():
    running = True
    while running:
        print("\n1. generate random")
        print("2. check id")
        print("3. exit")
        try:
            choice = int(input("select option: "))
            if choice == 1:
                genID()
            elif choice == 2:
                c2 = input("enter id: ")
                checkID(c2)
            elif choice == 3:
                running = False
            else:
                print("invalid")
        except ValueError:
            print("invalid")


if __name__ == "__main__":
    main()
