print("Calculator")

while True:

    print("Define your operation (+,-,*,/): ", end="")
    Function = input()

    if Function in ("+", "-", "*", "/"):
        if Function == "+":
            x1 = float(input("Enter first number: "))
            x2 = float(input("Enter second number: "))
            print(x1+x2)
        elif Function == "-":
            x1 = float(input("Enter first number: "))
            x2 = float(input("Enter second number: "))
            print(x1-x2)
        elif Function == "*":
            x1 = float(input("Enter first number: "))
            x2 = float(input("Enter second number: "))
            print(x1*x2)
        elif Function == "/":
            x1 = float(input("Enter first number: "))
            x2 = float(input("Enter second number: "))
            print(x1/x2)

        nxt_calc = input("Would you want another calculation? (y/n): ")
        if nxt_calc == "n":
            break
    else:
        print("Invalid")
