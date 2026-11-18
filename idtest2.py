import random

# A list of alphanumeric characters for base-36 encoding (0-9, a-z)
BASE36_CHARS = "0123456789abcdefghijklmnopqrstuvwxyz"

def encode_b36(num: int) -> str:
    """Converts an integer to a base-36 string."""
    if num == 0:
        return "0"
    res = []
    while num > 0:
        res.append(BASE36_CHARS[num % 36])
        num //= 36
    return "".join(reversed(res))

def decode_b36(s: str) -> int:
    """Converts a base-36 string back to an integer."""
    return int(s, 36)

def genID():
    op = random.randint(0, 3)
    # Numbers up to 3 digits (0 to 999)
    num1 = random.randint(0, 999)
    num2 = random.randint(0, 999)

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
        result = round(num1 / num2, 2) if num2 != 0 else 0

    # Encode components into a safe, hyphen-separated short ID string
    id_str = f"{op}-{encode_b36(num1)}-{encode_b36(num2)}"
    problem = f"{num1} {op2} {num2} = {result}"
    
    print(f"problem: {problem}")
    print(f"id: {id_str}")

def checkID(id_str: str):
    try:
        # Split the alphanumeric blocks back into their pieces
        parts = id_str.strip().split("-")
        if len(parts) != 3:
            print("Invalid ID format. Must be format: op-num1-num2")
            return

        op_code = int(parts[0])
        num1 = decode_b36(parts[1])
        num2 = decode_b36(parts[2])

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
            result = round(num1 / num2, 2) if num2 != 0 else 0
        else:
            print("Invalid operator code in ID")
            return

        problem = f"{num1} {op2} {num2} = {result}"
        print(f"id: {id_str}")
        print(f"problem: {problem}")
        
    except (ValueError, IndexError):
        print("Invalid ID content")

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