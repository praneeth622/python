from random import *

def gameplay(comp , user):
    if comp == user:
        return None

    elif comp == 'R':
        if user == 'S':
            return False
        if user == 'P':
            return True

    elif comp == 'P':
        if user == 'S':
            return True
        if user == 'R':
            return False

    elif comp == 'S':
        if user == 'R':
            return True
        if user == 'P':
            return False


print("Comp Turn : Rock{R}, Paper{P} or Scissors{S} ")
r = randint(1,3)
if r == 1:
    comp = 'R'
if r == 2:
    comp = 'P'
if r == 3:
    comp = 'S'

user =  input("Your Turn : Rock{R}, Paper{P} or Scissors{S} :  ")
a = gameplay(comp,user)

print(f'Computer choose {comp}')
print(f'You choose {user}')

if a == None:
    print(" Tie ")
elif a:
    print(" You Win the Game!!!, Congratulations")
else:
    print("You Lose, Better Luck Next Time ")

