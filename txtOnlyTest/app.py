import modes
import bankFuncs

def main():
    bankFuncs.createBank()

    running = True
    while running:
        print("\n(1) Answer Checker")
        print("(2) Number Guesser")
        print("(3) Memory Bank")
        print("(4) Exit")

        try:
            choice = int(input("Select Option: "))
        except ValueError:
            print("\nInvalid Choice")
        else:
            if choice == 1:
                modes.ansChecker()
            elif choice == 2:
                modes.numGuesser()
            elif choice == 3:
                memBank()
            elif choice == 4:
                running = False
                print("\nExiting...")
            else:
                print("\nInvalid Choice")

def memBank():
    bankMenu = True
    while bankMenu:
        print("\n(1) Add Problem")
        print("(2) Remove Problem")
        print("(3) View Bank")
        print("(4) Practice Problems")
        print("(5) Close Menu")

        try:
            choice = int(input("Select Option: "))
        except ValueError:
            print("\nInvalid Choice")
        else:
            if choice == 1:
                id = input("Enter Problem ID: ")
                bankFuncs.bankAdd(id)
            elif choice == 2:
                num = input("Enter Problem Number: ")
                bankFuncs.bankRemove(num)
            elif choice == 3:
                print(bankFuncs.loadBank())
            elif choice == 4:
                modes.memBank(bankFuncs.loadBank())
            elif choice == 5:
                bankMenu = False
                print("\nExiting...")
            else:
                print("\nInvalid Choice")
        

if __name__ == "__main__":
    main()