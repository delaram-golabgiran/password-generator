while True:
    try:
        a = int(input("Type your first number: "))
    except ValueError:
        print("Invalid Input. Try again.")
        continue

    try:
        b = int(input("Type your second number: "))
    except ValueError:
        print("Invalid Input. Try again.")
        continue


    oper = input("Choose a math operation (+, -, *, /, %, //): ")
    if oper == '+':
        print(" a + b = ", a+b)
    elif oper == '-':
        print(" a - b = ", a-b)
    elif oper == '*':
        print(" a * b = ", a*b)
    elif oper == '/':
        print("a / b = ", a/b)
    elif oper == '%':
        print("a % b = ", a%b)
    elif oper == '//':
        print("a // b = ", a//b)
    else:
        print('operator is not supported')
