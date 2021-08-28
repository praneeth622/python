

print(" Welcome to python Calculator \n             Done By Praneeth")
i = 1
while i >=1:
    if i >=1 :
        a = int(input("Enter First Number : "))
        b = int(input("Enter Secound Number : "))
        print("Choose any one of the following")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multipication")
        print("4. Division")
        pns = int(input("Choose Any one option : "))
        if pns == 1:
            print("Your value is : ", a + b)
        elif pns == 2:
            print("Your value is : ", a - b)
        elif pns == 3:
            print("Your value is : ", a * b)
        elif pns == 4:
            print("Your value is : ", a / b)
        else :
            print("Wrong option,  Try Again")
    p = str(input("To continue = (press any key), exit = q :"))
    if p == 'q':
        print('Exiting...')
        break
    print("Continue...")
    i = i+1 # Done own refrence scrach.py line 494

