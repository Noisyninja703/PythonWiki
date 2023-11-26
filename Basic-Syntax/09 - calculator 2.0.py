def calc():
    num1 = input("Enter a number : ")
    num2 = input("Enter another number : ")
    op = input("Enter an operator (+ | - | * | /) : ")

# check if input is valid then proceed
    if (num1.isnumeric and num2.isnumeric):
        num1 = float(num1)
        num2 = float(num2)

        if op == '+':
            answer = num1 + num2
        elif op == '-':
            answer = num1 - num2
        elif op == '*':
            answer = num1 * num2
        elif op == '/':
            answer = num1 / num2
        else:
            print("Invalid Operator")
            #restart
            calc()
    else:
        print("Please Enter a Number")
        #restart
        calc()

    print("Answer is " + str(answer))

calc()