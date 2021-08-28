def calculator(num1, sign, num2):
    if sign == "+":
        return num1 + num2
    elif sign == "-":
        return num1 - num2
    elif sign == "*":
        return num1 * num2
    elif sign == "/":
        return num1 / num2
    elif sign == "%":
        return num1 % num2
    elif sign == "**":
        return num1 ** num2
    elif sign == "//":
        return num1 // num2

a = int(input(" Enter First Number : "))
b = input(" Enter sign of operation : ")
c = int(input(" Enter Secound Number: "))

print("Your answer is : ", calculator(a, b, c))
    