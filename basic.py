'''
print ("Hello World!")
prit = 90;
print ("prit value is : ", prit)
# is use for comment 
#let "a" be varable and it has value of 78
a = 78; 
'''
##for running code we use print (a) no "" is not there if u use it it will print letter a not a=78
# print (a)
# for multiple line comment we can use ## or ''' at starting and ''' at ending
'''This 
is
 multiline
comment'''
'''datatypes 
numbers ex int-2,1,3,.. float-10.5,45.4... complex 4g,5s5...
sequence
boolean
set 
dictionary'''
# numbers datatypes 
'''a = 10;
b = 10.5;
c = 7j;

print (a)
print (b)
print (c)

print (type(a))
print (type(b))
print (type(c))
remove ' to run code 
'''
#Sequence data type -str, tuple, list 
'''a = "Hyderabad";
b = ("Praneeth", "Pravalika", "Padma", "Srinivas Rao")
c =  ["kedar", "sai kruthi"]

print (a) 
print (b) 
print (c)

print (type(a))
print (type(b))
print (type(c))
'''
#boolean just True or False
''')
T should capital in True'''
# set {}
'''b = {"Praneeth", "Pravalika", "Padma", "Srinivas Rao"}
print (b)
print (type(b))
'''
#dictionary data type
'''dict = {'brand': 'honda', 'model': 'city', 'colour': 'black'}
print ("Car Brand", dict['brand'])
print ("Car model", dict['model'])
print ("Car colour", dict['colour'])
'''
#Rules for making varirables in python
'''
1 Dont use space while making variables (my name = "Praneeth")
2 dont use special symboles like @#4567890! etc whiles making variables (n@ame = praneeth)
3 dont use number as first letter of your variable (8list ="list")
4 Invalid (my name = "";, n@me = "";)
5 valid (my_name ="";, nam3 ='';)
'''
#Invalid Type 
'''
my name = Praneeth
n@me = Praneeth
3shoule = some thing
'''
# valid type
'''
name = "praneeth";
myname3 = "praneeth";
my_name = "praneethrocks";

print (name)
print (myname3)
print (my_name)
'''
# Typecasting
#changing int to float 
''' a = 5.55;
print (type(a))
print (a)

x = int(5.55);
print (type(x))
print (x)

y = str(5.55);
print (type(y))
print (y)

b = int("Praneeth");
print (type(b))
print (b)
'''
# We get error because int will take only numbers but above one is in letters

 #Taking input from the user
'''
ipt = input("Enter a number")
print ("you enterd number is : ", ipt)
print (type(ipt))
'''
# to avoid entring letters in ipt we use following command in 2nd line 
'''
ipt = input("Enter a number : ")
ipt = int()
print ("you enterd number is : ", ipt)
print (type(ipt))
'''
# We can saparate by any symbol
'''
print(1,2,3,4,5, sep=' @ ')
# output 1 @ 2 @ 3 @ 4 @ 5    only for numbers
'''
'''
print('Answer is : {country} & {capital}' .format(capital = 'New delhi', country = 'India'))
'''
# Operators in Python

# Arithmetic operators (+,-,*,/,%,//,**)
'''
x = 5
y = 4

print('The Addition is : ', x + y)
print('The Sub is : ', x - y)
print('The Multi is : ', x * y)
print('The Division is : ', x / y)
print('The Exponation is : ', x % y)
print('The  Floor Division is : ', x ** y)
'''
# Assignment operator ( +=, -=, *=, /=, **=, =)
'''
x = 5

x += 3   # x = x + 3 lhs < rhs x = rhs
print(x)
x -= 3   # x = x - 3 lhs > rhs X = lhs
print(x)
x *= 3   # x = x * 3 lhs < rhs x = rhs
print(x)
x /= 3   # x = x / 3 lhs > rhs X = lhs
print(x)
x **= 3  # x = x **3  5 < 125 x = 125
print(x)
x  = 3   # Lhs = rhs  x = 5
print(x) 
'''
# Comparison  values (==, <, >, <=, >=, != )
'''
x = 5;
y = 3;
print('Comparison == is : ', x == y)
print('Comparison  > is : ', x > y)
print('Comparison  < is : ', x < y)
print('Comparison >= is : ', x >= y)
print('Comparison <= is : ', x <= y)
print('Comparison != is : ', x != y)
'''
# logical operator ( and, or , not) 
'''
x = 5;
y = 3;
print(x == 5 and y == 3) # both statements x , y should be correct
print(x == 5 or y == 3)  # one statement have to be correct
print(not(x == 5 and y == 5)) # any one statement should incorrect
# out put is true true true for all 3 
'''
# bitwise operators ( ^, |, &, ~, <<, >>)

# We should learn binary numbers to decimal numbers for it exucute the below one ( for internet not explaied )
'''def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

# decimal number
dec = 34 # change the value as you wish 

convertToBinary(dec)
print()'''
# Some binary numbers 
# 1 - 1, 2 - 10, 3 - 11, 4 - 100, 5 - 101, 6 - 110, 7 - 111, 8 - 1000, 9 -1001, 
# 10 - 1010, 11 - 1011 , 12 - 1100, 13 - 1101, 14 - 1110, 15 - 1111
'''
x = 7 # 7 in binary 0111
y = 2 # 2 in binary 0010
print('Bitwise for XOR :', x ^ y) # 0111 ^ 0010 = 0101 0*0=0 1*0=1 1*1=0 1*0=1
print('Bitwise for OR :', x | y)  # 0111 | 0010 = 0111 0*0-0 1*0=1 1*1=1 1*0=1
print('Bitwise for AND :', x & y) # 0111 & 0010 = 0010 0*0=0 1*0=0 1*1=1 1*0=0
print('Bitwise for NOT :', (~(x)))# 0111 - 1000 -8 
print('Bitwise for LS :', x << 2) # 7 * 2 = 14  14 *2 = 28
print('Bitwise for RS :', x >> 2) # 7 / 2 = 3.5 only 1st digit 3 /2 = 1.5 1st digit = 1
'''
# Membership operators ( in , not in )
'''
# input
# ex - 1 
x = ["India" , "Russia"]
print("India" in x)
# Output = True

# ex -2
# Input 
print('India' not in x) 
# Output False

# ex - 3 
print('nepal' not in x)
# Output True
'''
# Identity operators ( is , is not )
'''
x = ['Praneeth', 'Pravalika'] 
y = ['Praneeth', 'Pravalika'] # x = y because boh vales are similar but not same 9 root value is different
z = x # now x root value = z

print(x is y) # output - False x not equal to y but they are similar
print(x is z) # output - True because both root vale are similar
print(x == y) # Output - True both are similar but not same sa mentioned ( == means similar )
print(x == z) # Output - True both are same and similar
# still have dought ! run the down one 
print( x is not y) # output is True becaue x is not equal to y but similar
'''

# If-else 
'''
age = int(input(" Please enter Your age : "))

if age > 1 and age < 18:
    print("You not are Eligible")
elif age >= 18 and age <=99:
    print("Your are Eligible")
else:
    print("your age is max ")   
'''
# ex - 2
'''
print('Capital of India')
print('1. Delhi   2.Mumbai  3.Hyderabad  4.Vizag')
Answer = int(input("Your answer is : "))
if Answer == 1:
    print("Your Answer is correct ")
else :
    print( "Better Luck Next Time")
'''
# Loop statement (v For more go to line n0 308 )
'''
age = int(input("Enter your age : "))

if age > 1 and age < 18:
    print(" your are not Eligible")
elif age >= 18:
    print("You are Eligible ") 
    if age < 18 :
        print("Your are Minor ") 
    else :
        print("You are Major")
else:
    print("you are too old")
'''
# switch case statement
'''
def day1():
    return "Monday"
def day2():
    return "Tuesday"
def day3():
    return "Wesnesday"
def day4():
    return "Thursday"
def day5():
    return "Friday"
def day6():
    return "Saturday"
def day7():
    return "Sunday"
def default():
    return " Incorrect day "


switcher = {
    1: day1,
    2: day2,
    3: day3,
    4: day4,
    5: day5,
    6: day6,
    7: day7
   }
def switch(Dayweek):
    return switcher.get(Dayweek, default) ()

inp=int(input("Enter Day Number : "))
print(switch(inp))
'''

# Loops in python ( While , For, Nested )

# while loop
'''
a = 1
while a < 11: # upto 10
    print(a) # we are youing print a because loop satrts from 2 if we add print a it will 1 on top
    a += 1 # a = a=1 > let a=1 > a = 1+1 = 2
'''
# for loop 
'''
num = int(input(" Enter a number for table : "))
for a in range(1 ,11): # it will also work like above one value lie 1-11 i.e. 1 -10 will get print
    print( num , 'x' , a , "=" ,num*a) 
# Output is 5 x 1 = 5 , 5 x 2 = 10 ... work like multiplication table
'''
# range (sub topic)
'''
print(range(10)) # range(0,10)
print(list(range(1,10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,10,3))) # start at 1 and ends at 10 common difference is 3
# Output [1, 4, 7]
'''

# Nested loop
'''
colour = ["red", "blue","green"]
company = ["Dell" ,"Lenovo", "HP" ]
for x in colour:
    for y in company:
        print(x , y)
'''

# break and continue statement
'''
# continue statement 

for var in "word": # let var is in word but we dont know what is var 
    if var == "d": # now we will give some value to var i.e. is d
        continue   # now var is there in word i.e. d inn word , so now continue 
    print(var)     # now print var i.e. complet word except var i.e. d
                   # now we will add just ending statement
                   # OUTPUT is - w o r and 
print("ending")
'''

# break statement
'''

for var in "Word": # same as above 
    if var == "r": # same as above 
        break      # now statemant will break when it reached r
    print(var)

print("this statement is not needed") # OUTPUT - w o and last statement

'''
# list and tuples in python 

# list in python
'''
mylist = ["Laptop", "keyboard", "Mouse"]
#print(mylist)
#print(type(mylist))
#print(mylist[2]) # Output is Mouse, the pattern 0 1 2 3 4.. 
#print(len(mylist))# ans = 3 len = length =3
#print(len(mylist[0])) # ans = 6 laptop has 6 chartrs
'''
# Changing or replacing terms 
'''
mylist[0] = "Mointor"
print(mylist) # Output = ['Mointor', 'keyboard', 'Mouse']
'''
# Replacing multiple terms
'''
mylist[0] = ["Monitor", 'Laptop']
print(mylist) # Output = [['Monitor', 'Laptop'], 'keyboard', 'Mouse']
'''
# To add Terms
'''
mylist.append("Display")
print(mylist) # Output ['Laptop', 'keyboard', 'Mouse', 'Display']
# or
mylist.insert(0,"keys") # Output ['keys', 'Laptop', 'keyboard', 'Mouse', 'Display']
print(mylist) # it will add term "keys" at 0
'''

# arranging in Alphabetical order
'''
mylist.sort()
print(mylist) # output ['Display', 'Laptop', 'Mouse', 'keyboard', 'keys']
'''
# Removing terms
'''
print(mylist) # output ['Laptop', 'keyboard', 'Mouse']
mylist.remove("Laptop")
print(mylist) # ouput ['keyboard', 'Mouse']
# or 
mylist.pop(1)
print(mylist) 3 output ['keyboard']
'''

# Combining 2 lists
'''
yourlist = [ "Dell", "Lenovo", "HP"] # we need atleast 2 already my list so now we crete another
combine = mylist + yourlist # we can keep any term in place of combine 
print(combine) # output ['Laptop', 'keyboard', 'Mouse', 'Dell', 'Lenovo', 'HP']
'''

# Tupels in python
'''
mytuple = ("Laptop", "Keyboard", "Mouse", "Camera")
print(mytuple)
#print(type(mytuple))  
#print(mytuple[3])
mylist = list(mytuple) # same as list but u should change tiple to list by line 416, 417
mylist.insert(0, "wire")
print(mylist)
newtuple = tuple(mylist)
print(mylist)
mylist.remove("wire")
print(mylist)
# all are same as list but we should excucute line 416,417
'''
# finding repeted words
'''
# ex 1
var = (1,2,3,4,5,6,7,8,9)
x =var.count(3) # Output = 1 3 has repeted 1 time
print(x) # will tell how many times 3 has repeted 
'''
# ex -2
'''
xyz = (1,2,2,3,4,4,5,4,6,7,8,3,4)
y = xyz.count(4)
print(y)# Outut = 4 has repeted 4 times
'''
# set in python
'''
set1 = {1,2,3,4,5,6,7}
print(type(set1)) #output = class 'set' 
# adding 2 sets
set2 = {2,3,4,9,5,8}# set 1 is already there
set1.update(set2)
print(set1) # Output {1, 2, 3, 4, 5, 6, 7, 8, 9}

# removing terms in sets

set1.remove(1)
print(set1) # output {2, 3, 4, 5, 6, 7, 8, 9}

#removing ALL terms in set

set1.clear()
print(set1) # Output set()

'''
#Set union
'''
set1 = { 1, 2, 3, 8}
set2 = { 10, 20, 30, 80}
set3 = set1.union(set2)
print(set3) # output {1, 2, 3, 8, 10, 80, 20, 30}
'''
# intersection in sets
'''
set1 = { 1, 2, 3, 8}
set2 = { 1, 2, 30, 80}
set3 = set1.intersection(set2)
print(set3) #Output {1, 2}
'''
# Dictionary (DICt) in python
'''
mydict = {
    "Brand": "Lenovo",
    "Model": "G50-70",
    "Year": 2014,
    "TurboSpeed": "2.6G"   
}
'''
'''
print(mydict) # output {'Brand': 'Lenovo', 'Model': 'G50-70', 'Year': 2014, 'TurboSpeed': '2.6G'}
print(mydict["Brand"]) # Output Lenovo
# or 
x  = mydict.get("Brand")
print(x) # Output Lenovo
'''
# changing terms in dict
'''
mydict["Year"] = 2013
print(mydict["Year"]) # output = 2013
'''
# Adding terms 
'''
mydict["Colour"] = "Black"
print(mydict)
'''
# to temove terms
'''
mydict.pop("Colour")
print(mydict) # output {'Brand': 'Lenovo', 'Model': 'G50-70', 'Year': 2013, 'TurboSpeed': '2.6G'}
'''
# Rename of dict 
'''
thisdic = dict(mydict)
print(thisdic)
'''
# numbers in python
'''
a = 5
b = 4.5
c = int(b)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))

# min and max 
# min
print("min (102, 103, 104, 105) : ", min(102, 103, 104, 105))
# output =min (102, 103, 104, 105) :  102
# max
print("max (102, 103, 104, 105) : ", max(102, 103, 104, 105)) 
# output max (102, 103, 104, 105) :  105
'''
# Strings
'''
a = "Praneeth "
b = "Devarasetty"
c = a+b
print(c) # output = Praneeth Devarasetty
print(len(a)) # ans = 9
print(a[5]) # ans 5
print(c.lower()) # Output praneeth devarasetty
print(c.upper()) # Output PRANEETH DEVARASETTY
print(a.replace("P", "E")) # Output Eraneeth

name = "Praneeth"
txt = "my name {}"
name = input("")
print(txt.format(name))
# Output = input praneeth 
# my name is praneeth
'''
'''
txt = "We are Indian\'s and\\ we have Proud \"Quote\" to be an Indian"
print(txt) # output = We are Indian's and\ we have Proud "Quote" to be an Indian 

txt = "We are Indian\'s and \n we have Proud \"Quote\" to be an Indian"
print(txt)
# We are Indian's and
# we have Proud "Quote" to be an Indian 
# at place of \n it will come to another line
'''
# Funtion in python

# Simple funtion 
'''
def pra(x, y): # pra is just varable 
    return x+y

print(pra(4, 5)) # to execute top funtion we type same varable 
'''
# ex 2 
'''
def my_nation(country):
    print("I am from ", country) # we can write return or print, + can use in place of ","
my_nation("India") # we can add print also but there is no difference 
# output I am from India
'''

# Ex 3 
'''
def stu_details(name, age, city):
    print(" Student name {0}\n His age {1}\n He is from {2}".format(name, age, city))


 stu_details("praneeth", 17, "Hyderabad") 
# output Student name praneeth
# His age 17
# He is from Hyderabad
'''
# or
'''
def stu_details(name, age, city):
    print(" Student name {0}\n His age {1}\n He is from {2}".format(name, age, city))
# same as above
a = str(input("Enter Your name : "))
b = int(input("Enter your age : "))
c = int(input("Enter your Mobile Number : "))


stu_details(a, b, c)
# output Enter Your name : Praneeth
#Enter your age : 17
#Enter your Mobile Number : 9030919634
#Student name Praneeth
#His age 17
#He is from 9030919634
# to make top stu_details and bottom stu_details = name = a ....
'''
# recursion in python ex 2 scratch.py line 1350
'''
# Making factorial table another one is in scratch.py lne 1249
def factorial(x):

    if x == 1: # x =1 then 1 only ( we are writing condition)
        return 1
    else: # if x is not equal to 1 then it go to retrun 
        return( x * factorial(x-1)) # it will repert untill inp = x-1
# factoriaal x - 1 means it will go to top def factorial... and continue
inp = int(input(" Enter factorial number : ",))
print("The Factoral of ", inp, "is", factorial(inp) )
# output Enter factorial number : 7
# The Factoral of  7 is 5040
'''
# user defined modules
'''
import mod # mod.py is a file already created now we are importing

a = mod.laptop["Brand"]
print(a) # output Lenovo
'''


# predefined modules ( already install in system)
'''
import platform

print("system : ", platform.system())
print("Platform : ", platform.platform())
print("Processor : ", platform.processor())
# output system :  Windows
# Platform :  Windows-10-10.0.18363-SP0
# Processor :  Intel64 Family 6 Model 69 Stepping 1, GenuineIntel
'''
# import subprocess ex 2
'''
import subprocess

subprocess.Popen('C:\\Windows\\System32\\Calc.exe')
# calculator opended
'''
# Ex 3 playing songs

# download a file and keep in python folder ( in praneth folder - pythonfiles - python)
'''
import playsound

filename = 'alan.mp3.mp3'
playsound.playsound(filename)

# OUTPUT song is playing 
# top stop the music close and open virtul studo code
'''
# EX 4 EMOJIS 
'''
import emojis

print(emojis.encode(":smile:"))
# output not working 

'''
# File handiling in python
'''
# Creating file using python

file = open('trail.txt', 'w') # by this comand file will get created in python folder
file.write("this is trail file") # by this commond mentioned text will added in to it
file.close() # by this commound file get close
# output file created
''' 
'''
# read files 
file = open('trail.txt', 'r')
print(file.read())
# output - this is trail file
'''
# Object oriented pograming ( OOPS )
# Class and object in python oops 
# in oops class and obj are there 
# ex if we take car lights, tyres , seat .... are obj and total caris class  
'''
class person: # person is class ( person is variable) and name age .. are obj
    def __init__(self, name, age, city): # we are adding name age city as obj but NOT SELF 
        self.name = name # self is not variable it is constant
        self.age = age
        self.city = city

xyz = person("praneeth", 17, "hyderabad") # we already given a value
# xyz is variable and it can customizable
print("The person name is : " + xyz.name) 
print("The person age is : ", xyz.age)
print("The person city is : " + xyz.city)
'''

#if user give value
'''
class person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

a = str(input("Enter your Name : "))
b = int(input("Enter your Age : "))
c = str(input("Enter your City  :"))

abc = person(a,b,c)
print("The person name is : " + xyz.name) 
print("The person age is : ", xyz.age)
print("The person city is : " + xyz.city)
'''




