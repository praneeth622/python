# python from scrach
# Therory
'''
Python is a both compile and interpet language it use both
Python has it own Virtual Machine Bulit-In
Python imlementaion is here is Cpython
There are many implementations like Cpython, PyPy, Ironpython, Jython
Cpython From c language 
Jython from java
Ironpython from .net 
In general all use Cpython

'''
#Basic
'''
print("Praneeth laptop") # output Praneeth laptop
print(5 *"praneeth") # output praneethpraneethpraneethpraneethpraneeth
#print('Praneeth's laptop") # output error (Solution Next line)
#print("praneeth's laptop") # error 
#print('praneeth's"laptop') # error
# solution 
print('Praneeth\'s "laptop"') # It Works !!!
print('C:\docs\next') #Output C:\docs and ext on next line # error
# solution
print(r'C:\docs\next') # It works !! 'r' means raw it print statement raw
'''
# Using variables
'''
x = 5
y = 6
print(x + y) # output = 5
print(x + 10) # Output = 15 
'''
# Srings
'''

name = 'Youtube '
#print(name) # output youtube
#print(name[1]) # Output = o [Youtube - 0123456]
print(name[0:4]) # Output = yout # itstart at 0 and ends at 4
print(name[1:]) # Output = outube # it starts at 1 and complet the sentance
'''

# changing the name
'''
print('my' + name[0:]) # Output = myyoutube
print(len("Praneeth")) # output = 8
'''
# lists in python
'''
nums =[1,2,3,4]
print(nums[2]) # Output = 3
print(nums[4:]) # output 3
num = [3,5,7]
mal = (nums, num)
print(mal) # output ([1, 2, 3, 4], [3, 5, 7])
'''
# Editing
'''
# adding
hi = [1,2,3,4,5]
hi.insert(1,15)
print(hi) # Output [1, 15, 2, 3, 4, 5]
hi.append(15)
print(hi) # [1, 15, 2, 3, 4, 5, 15]

# Removing

#hi.pop(15) # [1, 2, 3, 4, 5]
print(hi)
del hi [2:]
print(hi) # [1, 15]
print(min(hi)) # 1
print(max(hi)) # 15
print(sum(hi)) # 16
print(hi.sort()) # none
'''
# tuples () only
'''
tup = (1,2,3,3,56,4)
print(tup.count(3)) # 2
'''
'''
# sets
s= {5,3,65,98,1}
# for more about sets go to basic.py for additional information
'''
# Dictonary
'''
data = {1:'Praneeth', 2:'Sujeeth'}
print(data[1]) # Praneeth=output
#or
data.get(1) # Praneeth
print(data.get(3,'Not Found')) # Not found
keys = ['Praneeth', 'Sujeeth', 'Surya']
values = ['skinny', 'fat', 'Fit' ]
total = dict(zip(keys, values))
print(total) # {'Praneeth': 'skinny', 'Sujeeth': 'fat', 'Surya': 'Fit'}
print(total['Praneeth']) # skinny
# TO add data to dictonary
total['Vignesh'] = 'short'
print(total) # {'Praneeth': 'skinny', 'Sujeeth': 'fat', 'Surya': 'Fit', 'Vignesh': 'short'}
# to delete
del total ['Vignesh']
print(total) # {'Praneeth': 'skinny', 'Sujeeth': 'fat', 'Surya': 'Fit'}
'''
# licts in Dict , Dict in Dict
'''
prog = {'Nsl' : 'Suger', 'Tata' : ['Tea', 'Steel'], 'Google' : {'Android' : 'Mobile', 'Youtube' : 'Allinone'}} 
print(prog) #  ''   ''   ''     ''' ''''' ....
print(prog['Tata']) # ['Tea', 'Steel']
print(prog['Google']) # {'Android': 'Mobile', 'Youtube': 'Allinone'}
print(prog['Tata'][1]) # Steel
print(prog['Google']['Android']) # mobile
'''
# More Varables
'''
# Every varable in python have some id/Addr, Let's Try !!
num = 5 
print(id(num)) # 1641545755056
num = 'Praneeth'
print(id(num)) # 1912018199792
'''
# ID
'''
a = 10 
k = a
print(id(a)) # 2016140683856
print(id(k)) # 2016140683856
print(id(10))# 2016140683856
# Conclusion if a = k = 10 then id(a) = id(k) = id(10)
'''
# range (sub topic)
'''
print(range(10)) # range(0,10)
print(list(range(1,10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,10,3))) # start at 1 and ends at 10 common difference is 3
# Output [1, 4, 7]
'''
# Keys and values
'''
d = {'Praneeth' : 'Samsung','nagendher' : 'Realme', 'Pavan' : 'Vivo'}
print(d.keys()) # dict_keys(['Praneeth', 'nagendher', 'Pavan'])
print(d.values()) # dict_values(['Samsung', 'Realme', 'Vivo'])
print(d['Pavan']) # Vivo
print(d.get('Praneeth')) # Samsung
'''
# Arithmetic Operaters (+ - * / ** // ...)
'''
x = 2 
y = 3
print(x+y) # 5
print(x-y) # -1
print(x*y) # 6
print(x/y) # 0.6666666666666666
print(x**y) # 8
print(x//y) # 0
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
a,b = 5,6
print(a, b) # 5 6
'''
# Unary operators
'''
a = 2 
print(a) # 2
a=-a
print(a) # -2
'''
# Relational Operators
'''
n =7 
m =6 
print(n < m) # False
print(n > m) # True
print(n == m) # Flase
n = 6
print(n == m) # True
print(n >= m) # True
print(n <= m) # True
print(n != m) # False # != means not equal to
'''
# Logical Operators
'''
# And
a = 5
b = 3
print(a>8 and b<6) 
# false = true * false = false 
print(a < 9 and b <6 )
# True = True * true 
print(a >2 and b > 2 )
# true = flase * false 
'''
# Or
'''
a = 5
b = 3
print(a>9 or b < 7 )
#True = false * True = true
print(a<9 or b>7)
#True = true * flase = true
print(a >2 and b > 2 )
# true =true * true
print(a >11 or b > 11)
# False = false * false = false
'''
# not
'''
x = True
print(not x)
# false
'''
# Binary, Hexa, octa
'''
print(bin(52)) # 0b110100  b = binary
print(0b110100) # 52
print(oct(25)) # 0o31 o = octa
print(hex(25)) # 0x19 x = hexa
print(0xf) # 15 
'''
# Swapping 
'''
a = 5    # Output is  6 and 6 we are lossing value of a so use down ex
b = 6

a = b
b = a 

print(a)
print(b)

# ex 1

a = 5 
b = 6
         # Output = 6  5 or we can use formula # next example 
temp = a
a = b
b = temp

print(a)
print(b)

# ex 3 

a = 5 
b = 6
            # output = 6 5 
b = a + b   # 11
a = a - b   # 5 
b = a - b   # 6
            # or we can use ^ sign only in the place of both + - 
print(a)
print(b)

# ex 4

a = 5 
b = 6
          # Output= 6 5
a,b = b,a # it is use only for single not multi line

print(a)
print(b)
'''
# Bitwise Operators
#Complement ~
# And &
# Or |
#  XOR ^
# Left Swift <<
# Right Swift >>

# Complement ~
'''
print(~12) # - 13 
'''
'''
# 12 binary  is 00001100
# in genaral 13 is 00001101
# to convert 13 to - 13 we use 2 complement =>
# convert 13 to 13's complement reverse => 11110010 + 1 => 11110011  ( +1 becouse 2 = 1+1 => reverse + 1)
# 11110010 is 1's complement and when er add + 1 to it it will become 2's complement
# 2's complement is - sign so -13 = 12 complement
# 12 =>   00001100 12 's complement is reverse of 12
# 11110011 = 12's complement = -13 complement= 11110011
# https://youtu.be/PyfKCvHALj8?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&t=83
'''
# And & 
'''
# in and both should true to get true

print(12&13) # 12 REASON down
'''
'''
# 12 === 00001100
# 13 === 00001101 both should 1 then 1 or else it is 0 in AND 
# compare --------
# ans ===00001100 =12 ( last digit should be 0 line 302)
# Reason  line 302
'''
# OR
'''
print(12|13) # 13
# 12 === 00001100
# 13 === 00001101 (In OR ) any one should 1 then it is 1 or else it is 0 
# compare --------
# ans ===00001101 =13
'''
# XOR (^) ( if both num are different then ans is 1 or else it is 0)
'''
print(12^13) # Output = 1
# 12 ==== 00001100
# 13 ==== 00001101
# compare --------
# ans === 00000001 ( both are same it is 1 or else ot s 0)  
print(25^30) # Output is 7
# 25 ==== 11001
# 30 ==== 11110
# ans = 00111 = 7
'''
# Left shift (<<)
'''
print(10<<2) # output is 2
# 10 === 1010.000..... 
# when 2 is there then shift decimal point 2 to right side
# then ans == 101000 = 40
'''
# Right shift(>>)
'''
print(10>>2)
# # 10 === 1010.000..... 
# when 2 is there then shift decimal point 2 to left side = 10.10 = 10
# then ans == 10= 2
'''
# Important math functions in python
'''
# first import math funtion by 'import Math'

import math
x = math.sqrt(25) 
print(x) # 5.0

# Floor and ceil
# let be       ------- ceil  ---3      
#                 ---2.1-3.0 (floor)                         
#                    then ans = 2                    
#                                  ---2.1-3.0(ceil) ans = 3 
#             --------Floor  ---2
print(math.floor(2.9)) # 2 # floor give least
print(math.ceil(2.9)) # 3 # ceil gives highest
# Power and Square
print(3**2) # 9, ** =9
print(math.pow(3,2)) # 9.0 
print(math.pi) # 3.141592653589793
print(math.e) # 2.718281828459045
# IF U R LASY TO TYPE MATH !!! THEN,
# SET import math as m or any other letter
# or u even import limited functions by 
# from math import pow,sqrt .....
'''
# User input in python

# to control how many digts to print
'''
chr= input('enter a chr')
print(chr[1]) # input = qwery # output= q
'''
# If, Else, elif, nested if
# elif is use when if is correct it will not check elif if is not staisfied then it will check elif
# else = is wrong then it will check or it will not check 
# nested if = if under if


# If & elif example
'''
n = int(input("Enter your age : "))

if n >=0 and n<= 17 :
    print("Your are Minor")
elif n >= 18 :
    print("your are Major")
else :
    print("valid Age")
'''
# Nested if
'''
age = int(input("Enter your age : "))
if age >= 13 and age <= 22 :
    print('Your are eligible for exam')
    if age >= 13 and age <=15 : # it is nested if
        print("Your exam fee is 600")
    else:
        print('Your exam fee is 1200')

print("All The Best for your exam !!!")
'''
# Loop ( While )
'''
i = 1
j = 1
while i<=5:
    print('Praneeth')
    while j<= 4 :
        print('great')
        j=j+1
    
    i = i+1
'''
# ex 2 
'''
i = 1

while i<=5:
    print('Praneeth', end = ' ')
    j = 1 # here j is is under i so it will print side to  
    while j<= 4 :
        print('great', end = ' ')
        j=j+1
    
    i = i+1
    print() # whe we add print() then it starts printinging from next line
# hw 2.py hw 1.py for home work
'''

# Loop ( For )
'''
# ex 1
x = 'praneeth', 10, 10.3
for i in x:
    print(i)
# praneeth
# 10
# 10.3
'''
# ex 3
'''
for i in ["Praneeth", 10]:
    print(i)
# praneeth
# 10
'''
# Ex 4
'''
x= "PRANEETH"
for i in x:
    print(i) # PRANEETH vertically
'''
# ex 4
'''
for i in range(10):
    print(i) # 0-9 vertically
'''
# ex 5
'''
for i in range(2,10,2): # 2 is starting, 10 is ending, 2 is common difference
    print(i) # 2 4 6 8 vertically
'''
# ex 6
'''
for i in range(20,10,-2): # 20 starting 10 is ending -2 is common diff - to go back
    print(i) # 20 18 16 14 12 
'''
# ex 7 ***** print only 5 mulipules
'''
for i in range(1,21):
    if i%5  == 0:
        print(i) # 5 15 20
'''
# ex 8 not to print multipules of 5
''' 
for i in range(1,21):
    if i%5!=0:
        print(i)# 1- 20 except 5 10 15 20
'''
# ex 9 hw 3
'''
for i in range(1,51):
    if (i**(.5) == int(i**(.5))):
            print(i) # 1 4 9 16 25 36 49 
'''
 # Break, Continue and pass statement

 # Break
'''
x = int(input("How Man candy Do You want : "))
av = 5 # Candy will stop after printing 5 candy
i = 1
while i <= x:
    if i == av: # when i = avalivble (av) then it display out of stock 
        print( "Out Of Stock")
        break
    print('Candy')
    i = i+1
print("Thank you for placing Order ")
# candy (5 times Verticullary ) then out of stock, thank yoy for placing Order
'''
# Continue # print all 1 -100 except divisible by 3 5 
'''
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        continue
    print (i)
''' # 1-100 except divi by 3 5 
# Pass 

# Dont print odd numbers
'''
for i in range(1,101):
    if i%2!=0: # except divisible by ignore it (!=)
        pass # if no code is there then we use pass
    else: # if else is not there it will print odd numbers
        print(i)
'''     
# EX #3 hw 2 
'''
for i in range(1,101):
    if i%2 !=0 and i%3 !=0 and i%5 !=0 and i%7 !=0 :
        pass
    
        print(i) # prime numbers
'''
# ex 4 hw 4 ( line 604 )
'''
a = int(input("Enter an number : "))

for j in range(2, int(a/2) + 1):  
            # If the given number is divisible or not  
            if (a % j) == 0:  
                print(a, "is not a prime number")  
                break
            else:
                print(a, "is a prime number")
'''
# Printing prattens in python

#
# #
# # #
# # # #
'''
for i in range(4):
    for j in range(i+1): # i starts from 0 if we not ive + 1 first line will empty
        print("#", end = ' ')
    print() # Done
'''
# # # #
# # #
# #
#
'''
for i in range(4):
    for j in range(4-i): # 4- i because it will decrese 
        print("#", end = " ")
    print() # Done :-)
'''
# For - Else
# Ex - 1
'''
x = [10,11,12,13,14] 
for y in x :

    if y % 5 ==0:
        print(y) # 10
'''
# Ex 2
'''
x = [10,11,12,13,15]
for y in x :
    if y % 5 ==0:
        print(y) # 10,11 ( till heer)
        # if u need only 1 not too means just add break 
        break # 10 only
'''
# ex 3
'''
x = [16,11,12,13,14] # if not foud we make funtion "not found"

for y in x : 
    if y % 5 == 0:
        print(y)
        break
    else: 
        print("NotFound") # NotFound 5 times vertically
'''
# Ex 4
'''
x = [16,11,12,13,14] # if not foud we make funtion "not found"

for y in x : 
    if y % 5 == 0:
        print(y)
        break
else: 
    print("NotFound") # NotFound
# we use for -else in same loop and not in if loop
# if we use else in if loop it will print 5 times
'''
# Prime Number in python (line 528)
'''
num = int(input("Enter A Number : "))
for i in range(2,num):
    if num % i == 0:
        print("Not Prime")
        break # If it is not used it will print many times
else: 
    print("Prime")
'''
# Array
'''  ***NOTES***
unsigend = it will consider only + sign
sign = it will take both + -
Type code    C Type     Python Type    Minimum size in bytes
     
'b'         signed char         int            1
'B'         unsigned char        "             1
'u'         wchar_t       Unicode character    2 
'h'        signed short          "             2
'H'       unsigned short         "             "
'i'        signed int            "             2
'l'        signed long           "             4
'I'       unsigned int           "             "
'L'       unsigned long          "             4
'q'      signed long long        "             8
'Q'     unsigned long long       "             8
'f'          float               float         4
'd'          double              float         8
'''
# Importing array 

# 1 import array
# usage is array.array(...)
# 2 import array as arr or ..
# arr.array(..)
# OR
# from _typeshed import Self
from array import *  # * means all

''' 
# Usage just array(....)
vals = array('i',[5,2,3,6,4]) # is type is 1 
print(vals)
# array('i', [5, 2, 3, 6, 4])
# it will not take float(8.5..)
# it will not accept - sign
# for that un should chang type 
print(vals.buffer_info())
# (2208903207536, 5) first num is add, secound is size 5 digt, 4 digt
print(vals.typecode) # i
'''
# we can use append and insert to add
# we can use reverse to reverse
# we can use remove to remove
'''
# to print in order
for i in range(5):
    print(vals[i]) # all values vertically
'''
# if we dont know leanth but we need every value in in vertically
'''
vals = array('i',[5,-8,9,5,4])
for i in range(len(vals)):
    print(vals[i]) # all valuse vertically
# or
for e in vals:
    print(e)
# same output 
'''
# coping array 
'''
vals = array('i',[5,8,9,5,4])
newarr = array(vals.typecode, (a for a in vals))
# it means type c = use vals typcode = i, for value just copy each letter from vals and copy it to newarr
for e in newarr:
    print(e) # only valuse vertically
'''
# doing squres of above vales
'''
vals = array('i',[5,8,9,5,4])
newarr = array( vals.typecode, (a*a for a in vals))
# it will print each value of vals and multiply with it and it wil paste
for e in newarr:
    print(e)
 # only squres of value vertically
'''
# doing same with while loop insted of for loop
'''
vals = array('i',[5,8,9,5,4])
newarr = array( vals.typecode, (a*a for a in vals))
i = 0
while i<len(newarr):
    print(newarr[i])
    i = i+1 # al squre values in vertically
'''
# Array values from from user 

# Ex 1  ask user to enter or add value in array
'''
dev = array('i',[]) # let the array be empty

n = int(input(" Enter the Length of array : "))
# now we should add letters in array
for i in range(n):
    x = int(input(" Enter the value : "))
    dev.append(x)
print("You enter array is : ", dev)
'''
# Ex 2 check weather user given value is in array
'''
dev = array('i',[]) # let the array be empty

n = int(input(" Enter the Length of array : "))
# now we should add letters in array
for i in range(n):
    x = int(input(" Enter the value : "))
    dev.append(x)
print("You enter array is : ", dev) # just copy paste top program

val = int(input(" Enter the value you want to check : "))
k = 0

for e in dev:# we use e because we already use i 
    if e == val:
        print(k)
    k = k+1 

print(dev.index(val))
# input = 5  1 2 3 4 5 
# output = 3 3 # 1st 3 is loop and 2nd 3 is due to print(dev.index(val))
'''
# we can use is single and multi dimensional
# to use multi dimensional we have to download NUMPY tool
# numpy download by = pip3 install numpy
# multi dimensional array used in ex matrix etc...
# numpy (multi dimensional)
# importing of numpy is same as import array ( line 636)
from numpy import *

# ex 1
'''
arr = array('i',[1,2,3,4,5])
print(arr) # Error beczuse we should not specify type code
'''
# ex 2 
'''
arr = array([1,2,3,4,5])
print(arr) # [1 2 3 4 5] 
'''
# Different ways creating array in numpy 
# array()
# linspace()
# logspace()
# arange()
# zeros()
# ones() 

# array
'''
arr = ([1,2,3,4,5.0], int) # in place of int we an use float ...

print(arr)# [1, 2, 3, 4, 5.0]
'''
# linspace 
#ex 1
'''
arr = linspace(0,15,20) # starts from 0 end at 15 it divides 20 equal parts 
print(arr)
# [ 0.          0.78947368  1.57894737  2.36842105  3.15789474  3.94736842
#  4.73684211  5.52631579  6.31578947  7.10526316  7.89473684  8.68421053
#  9.47368421 10.26315789 11.05263158 11.84210526 12.63157895 13.42105263
# 14.21052632 15.     ]
'''
# ex 2
'''
dev = linspace(0,20,10)
print(dev)
# [ 0.          2.22222222  4.44444444  6.66666667  8.88888889 11.11111111
# 13.33333333 15.55555556 17.77777778 20.        ]
'''
# ex 3
'''
deva = linspace(1,25) # it default divide 50 parts
print(deva)
# [ 1.          1.48979592  1.97959184  2.46938776  2.95918367  3.44897959
#  3.93877551  4.42857143  4.91836735  5.40816327  5.89795918  6.3877551
#  6.87755102  7.36734694  7.85714286  8.34693878  8.83673469  9.32653061
#  9.81632653 10.30612245 10.79591837 11.28571429 11.7755102  12.26530612
# 12.75510204 13.24489796 13.73469388 14.2244898  14.71428571 15.20408163
# 15.69387755 16.18367347 16.67346939 17.16326531 17.65306122 18.14285714
# 18.63265306 19.12244898 19.6122449  20.10204082 20.59183673 21.08163265
# 21.57142857 22.06122449 22.55102041 23.04081633 23.53061224 24.02040816
# 24.51020408 25.        ]
'''
# arange (/a range/)
'''
arr = arange(1,15,2) #starts at 1 end at 15, it will print after 2 steps
# it will print 1 and print 3 5 7
print(arr) # [ 1  3  5  7  9 11 13]
'''
# logspace
# Ex 1
'''
# logspace contain 3 or 5 values ( we are taking 3 - start,end,parts)
# start: It represents the starting value of the interval in the base.
# stop:It represents the stopping value of the interval in the base.
# num:The number of values between the range.
# endpoint:It is a boolean type value. ...
# base:It represents the base of the log space.
arr = logspace(1,5,5) 
print(arr) # [1.e+01 1.e+02 1.e+03 1.e+04 1.e+05] for calrity got line 817

# it take log 1 or easily take 10 to poewr or 10**
# 10**1 = 10 or 1.e+01 
# ends at 10**5 or 1.e+05
# divides 5 parts
# TO GET ACCURATE VALUE TYPE "print('%.2f' %arr[index num])"
print('%.2f' %arr[0]) # 10
print('%.2f' %arr[1]) # 100
print('%.2f' %arr[2]) # 1000
print('%.2f' %arr[3]) # 10000
print('%.2f' %arr[4]) # 100000
'''
# Ex 2
'''
dev = logspace(5,78,8)
# start at 5 i.e. 10**5 =100000
# ends at 78 i.e. 10**78 = 
print(dev)# [1.00000000e+05 2.68269580e+15 7.19685673e+25 1.93069773e+36
# 5.17947468e+46 1.38949549e+57 3.72759372e+67 1.00000000e+78]

print('%.2f' %dev[0]) # 100000.00
print('%.2f' %dev[1]) # 2682695795279727.50
print('%.2f' %dev[2]) # 71968567300115284252164096.00
print('%.2f' %dev[3]) # 1930697728883245745701259503137193984.00
print('%.2f' %dev[4]) # 51794746792312235958236180840144950459816214528.00
print('%.2f' %dev[5]) # 1389495494373147430779328728969267709764684200590190837760.00
print('%.2f' %dev[6]) # 37275937203149226287136062689097023685326282582807869158706896699392.00
print('%.2f' %dev[7]) # 1000000000000000008493621433689702976148869924598760615894999102702796905906176.00
# it get devided into 8 parts
'''
# zeros 
'''
arr =zeros(6)
print(arr) # [0. 0. 0. 0. 0. 0.]
'''
# ones

# Ex 1
'''
arr = ones(5)
print(arr) # [1. 1. 1. 1. 1.]
'''
# ex 2 
'''
dev = ones(7,int) # also applicable to zeros 
print(dev) # [1 1 1 1 1 1 1]
'''
# Adding 2 arrays 
# ex 1
'''
arr = array([1,2,3,4,5])
arr1 = arr + 5
print(arr1) # [ 6  7  8  9 10] it will add + 5 to all nums
'''
# ex 2 
'''
arr1 = ([5,6,7,8,9])
arr2 = ([1,2,3,4,5])
arr3 = arr1 + arr2
print(arr3) # [5, 6, 7, 8, 9, 1, 2, 3, 4, 5]
'''
# we can even perform funtions with array
'''
arr1 = ([5,6,7,8,9])
print(sin(arr1)) # [-0.95892427 -0.2794155   0.6569866   0.98935825  0.41211849]
print(cos(arr1)) # [ 0.28366219  0.96017029  0.75390225 -0.14550003 -0.91113026]
print(log(arr1)) # [1.60943791 1.79175947 1.94591015 2.07944154 2.19722458]
print(sqrt(arr1))# [2.23606798 2.44948974 2.64575131 2.82842712 3.        ]
# sqrt(squre root)
print(sum(arr1)) # 35
print(max(arr1)) # 9
'''
# copying array
# we have 2 types of copye it is shadow copy and deep copy ( line 897 917 ) 
# Ex 1
'''
arr1 = ([5,6,7,8,9])
arr2 = arr1
print(arr1) # [5, 6, 7, 8, 9]
print(arr2) # [5, 6, 7, 8, 9]
print(id(arr1)) # 1972073377536
print(id(arr2)) # 1972073377536 
# both have same id it is called aliasing
'''
# Ex  2 (Shadow Copy)
'''
arr1 = array([1,2,5,7,9,4])
arr2 = arr1.view() # view make a different array at different location 
print(arr1) # [1 2 5 7 9 4]
print(arr2) # [1 2 5 7 9 4]

print(id(arr1)) # 1682646657328
print(id(arr2)) # 1682646657232
# now we can see different id even we have same array
# we have some problem in this view option
# if we change the value of arr1 automatically arr2 value will be changed 
arr1[0] = 7
print(arr1) # [7 2 5 7 9 4]
print(arr2) # [7 2 5 7 9 4]
# IF WE CHANGE ONE ANOTHER ONE IS ALSO CHANGED
# IT WILL GIVE SHADOW COPY **********
# SHADOW COPY MEANS if 1 is change 2 will also change automatically
'''
# Ex 2 Deep copy 
'''
arr1 = array([1,2,5,7,9,4])
arr2 = arr1.copy() # it is deep copy
arr1[0]=6

print(arr1) # [6 2 5 7 9 4]
print(arr2) # [1 2 5 7 9 4]

print(id(arr1)) # 1722683124112
print(id(arr2)) # 1722683124016

# Now if we change arr1 it will nopt effect arr2
# also id of both will be different 
'''
# Working with Multi Dimentional array or Matrix
'''
arr1 = array([
    [1,2,3],
    [4,5,6]
])
print(arr1)
# [[1 2 3]
#  [4 5 6]]
print(arr1.dtype) # int32, dtype we can know what type of data we ae working with
print(arr1.ndim)  # 2, ndim give u how many dimention you are working with here 2 dimension
print(arr1.shape) # (2, 3), it will give no.of rows and coloums
print(arr1.size)  # 6 = 3*3, it will give size of entire block 3*3=6 3 colu *3 colu 
'''
# Converting 2D array to 1D array
'''
arr1 = array([
    [1,2,3],
    [4,5,6]
])
arr2 = arr1.flatten()
print(arr2) # [1 2 3 4 5 6] 
'''
# converting single dimensional to multi dimensional
'''
arr1 = array([
    [1,2,3,6,7,9],
    [4,5,6,5,4,8]
])
arr2 = arr1.flatten()
arr3 = arr2.reshape(3,4) # 3 rows and 4 colo
print(arr3)
#[[1 2 3 6]
# [7 9 4 5]
# [6 5 4 8]]
'''
# making multiple arrays
'''
arr1 = array([
    [1,2,3,6,7,9],
    [4,5,6,5,4,8]
])
arr2 = arr1.flatten()
arr3 = arr2.reshape(2,2,3) 
# it will make 2 arrays , 2 rows and 3 colu
print(arr3)
#[[[1 2 3]
#  [6 7 9]]

#[[4 5 6]
#  [5 4 8]]]
'''
# Matrix
'''
m = matrix('1 2 3; 4 5 6; 7 8 9') # ;=make new row 
print(m)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print(diagonal(m)) #[1 5 9]
print(m.min()) # 1 it will print min in total matrix
print(m.max()) # 9 it will print max in total matrix
'''
# + - * / of matrix 
'''
m = matrix('1 2 3; 6 5 4; 7 8 9')
m1 = matrix('7 8 9; 3 3 0; 3 2 3')
'''
# Addition
'''
m = matrix('1 2 3; 6 5 4; 7 8 9')
m1 = matrix('7 8 9; 3 3 0; 3 2 3')
m2 = m +m1
print(m2)

# [[ 8 10 12]
# [ 9  8  4]
# [10 10 12]]
'''
# multiplication
'''
m = matrix('1 2 3; 6 5 4; 7 8 9')
m1 = matrix('7 8 9; 3 3 0; 3 2 3')
m2 = m * m1
print(m2)
#[[ 22  20  18]
# [ 69  71  66]
# [100  98  90]]
# all are same just change sign at line no 1009
'''
# Funtions in Python
# Ex 1
'''
def routine(): # routine is just variable we can keep any thing
    print(" Hello, Sir")
    print("what can i do for u")
routine()
#Hello, Sir
#What can i do for u
# ***USES***
# untill we not specify variable (routine in aboue case) it will not print 
# it will keep in mind the value of variable
# if we typing large program we cant write specify the value of variable every time it will be easier
# we can allocate job of every function
# it makes our tasks easier
'''
# Ex 2
'''
def add(x,y):
    c = x+y
    return c # return = it just store in c

result = add(2,6)
# it will add the value and sore in c 
# c = result as mentioned in line no 1042
print(result) # 8
# the value of add(2,6) is stored in result
''' 
# Ex 3 
'''
def add_sub(x,y): # let us keep the name of function as add_sub
    c = x+y
    d = x-y
    return c,d
result1, result2 =add_sub(1,7)
print(result1, result2) # 8, -6
'''
# Function Arguments in python
# Pass by Value - Pass by Reference 
'''
def qwerty(x):
    x = 8
    print('x - ',x) # 8
a= 10
qwerty(a)
print('a - ',a)# 10
# here we can say that 'a' is not affecting by 'x'
# ***PASSBYVALUE*** - if we call function by passing variable or value, it will pass as a value but not change variable
# In above one we can say it just pass the vlue but not the address or change the varable
# ***PASSBYREFRENCE*** - it will change address or change the value of variable
#      ****IN PYTHON WE DONT HAVE PASSBYVALUE OR PASSBYREFERENCE****
'''
# Ex 2
'''
# Let us check the id of 3 (before namig the value x(1075), after x(1077) and id of a(1082))

def qwerty(x):
    print(id(x)) # 1408744581712
    x = 8
    print(id(x)) # 1408744581712
    print('x - ',x) # 8
a= 10
print(id(a)) # 1408744581648
qwerty(a)
print('a - ',a)
print(id(a)) # 1408744581712
# we can see that id of a is different after effecting with x id of a is changed to id of x 
# but id(x) = id(a) but x!=a 
# the reason is integer and strings are immutable(cant changed)
'''
# Types of arguments
'''
# These are 2 types - Actual Arguments , Formal Arguments
def add(x,y): # It is Formal Arguments
    c = x+y
    print(c)

add(5,6) # This is Actual Arguments
# Actual Arguments are 4 Types they are 
# 1 Position 
# 2 Keyword
# 3 Default
# 4 variable length 
'''
# Position 
'''
def list(name,age):
    print(name)
    print(age)

list('Praneeth',18)
# position should be same   
# both arguments should be same in funtion and user input/fun.call & fun.def
'''
# keyword
'''
def list(name,age):
    print(name)
    print(age)

list(age=18, name="Praneeth")
# if we don't know the order then we will then we can use keyword argument
# position not requried
# intiaisation done based on keywords
'''
# Default
'''
def list(name,age = 18):
    print(name)
    print(age)

list("Praneeth")
# If user Dont specify then age then it will take 18(as u specify) as default
def list(name,age):
    print(name)
    print(age)

list('Praneeth',17)
# if we specify the age it will overwrite the age
'''
# variable length
''''
def branch(*courses):
    for i in courses:
        print(i)

branch("MBA","MCA","B-TECH")

# it accept any no.of aruguments 
# It will done by placing * before to the argument of f.definetion
'''
# Ex 2
'''
# If we dont shure about  what user give in data then
def details(name,**data): # 88data reprsents the multiple with keywords
    print(name) # Praneeth
    print(data) # {'age': 28, 'city': 'Hyderabad'}

details('Praneeth', age=28, city='Hyderabad')
'''
# Global and local scope
# Global Keyword in python
'''
# Ex 1
a =10
def something():
    a = 15
    print(a) # 15

something()
print(a) # 10
# Here we can see first a has value 15 and secound has 10 
# First a is GLOBAL
# secound a is LOCAL
# global a will not  effect the local a
# we cant use the local a ('a' or any other variable) outside(global)
'''
# Ex 2 what if we dont specify local variable
'''
a= 15
def thing():
    print(a) # 15
thing()
print(a) # 15
# we can use global variable as local variable if we not specify local varable 
'''
# Ex 3 how to change global variable in local variable
'''
a= 15
def thing():
    global a
    a = 10
    print(a) # 10
thing()
print(a) # 10
# now we change global = local
'''
# Ex 3 accessing Both Global and local at a time
'''
a =10
print(id(a)) # 2388072884816
def access():
    a = 15
    x = globals()['a']
    print(a) # 15
    print(id(a)) # 2388072884976
    print(x) # 10
    print(id(x)) # 2388072884816
print(a) # 10
access()
# we can conclude that
# global a = x by using globals arguments
# now we use a in global and local a 2 ways by copying global a as x 
'''   
# Ex 4 Changing gobal variable by not effing local variable
'''
a =10
print(a) # 10
def access():
    a = 15
    x = globals()['a']
    print(a) # 15
    print(x) # 10
    globals()['a'] = 15 # we have changed global variable 10 to 15 by using globlas arugument

access()
print(a) # 15
'''
# Pass list in python
'''
# Ex 1 finding no.of even and odd numbers

def find(list):
    even = 0
    odd = 0

    for i in list:
        if i%2 == 0:
            even +=1 # +=1 because we should increment the numbers
        else:
            odd +=1
    return even,odd
list = [12,23,56,4,8,45,621,474,78]

even, odd = find(list)
print(even) # 6
print(odd) # 3
# or (Conclusion)
print("No.of Even No is : {} and No.of Odd No.is : {}" .format(even,odd))
# No.of Even No is : 6 and No.of Odd No.is : 3
# .format will add the value at flower brackets
'''
# Printing FIBONACCI Numbers
'''
def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2,n): # in range it will print -1 so 2 = it print 1
        c = a + b
        a = b
        b = c
        print(c)


fib(15)
# first 15 fibb numbers printed
# But there is problem when we give 1 (fib(1)) then it will print 2 numbers insted of 1 
# to solve it will add if function
'''
# Ex 2 
'''
def fib(n):
    a = 0
    b =1

    
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)


    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(c)

# fib(1) # 0
# or taking no.of values from user
n = int(input("Enter no of fibnocci numbers do u want : "))
fib(n) # it works !!!
'''
# Factorial ex 2 in basic.py line 610 and scratch.py line 1350
'''
def fact(n):

    f = 1

    for i in range(1,n+1): 
        f = f * i 

    return f
p =(int(input("Enter Factorial Number : ")))
result = fact(p)
print(result)
'''
# Recursion - A function calling it self in multiple times
'''
def repert():
    print("Hellow World")
    repert()# i am using same inside it to rpert multiple times

repert()

# it will print multiple times and final it et error for printing multiples times
# But How many Times ???....
# let find
'''
# Ex 2 Knowning how many times does it repert
'''
i = 0
def find():
    global i # We use it because we are using global i in local
    i +=1 
    print("Hello World", i)
    find()
find()  

# It has print 1000 lines(996 + 4 error)
# If we need to set certain no.of loops more than 1000 then 
'''
# Ex 3 set loop limit
'''
import sys

sys.setrecursionlimit(2000)
i = 0
def find():
    global i # We use it because we are using global i in local
    i +=1 
    print("Hello World", i)
    find()
find()  # Hello World 1996 = 4 error
'''
# Recurtion in Factorial
'''
def fact(n):

    if n == 0:
        return 1
    
    return n * fact(n-1)

n = int(input("Enter Factorial Number : "))
result=fact(n)
print(result)
'''
# Lambda ( Anonymous Functions )

# Ex 1

# we can use functions without name by using lambda
'''
f = lambda a : a*a
result = f(5)
print(result) # 25
'''
# Ex 2 for multiple letters
'''
f = lambda a,b : a*b
result = f(5,9)
print(result) # 45
'''
# Function in Lambda
# 1.Filter
# 2.Map
# 3.Reduce

# Filter
'''
# Task to filter EVEN numbers from list

nums= [2,5,3,4,86,7,2,6]
result= list(filter(lambda n : n%2==0 , nums)) # we use lambda as temp, anourumus
print(result) # [2, 4, 86, 2, 6] for odd write (lambda n : n%2 ,nums)
'''
# Map
'''
# Now we will make *2 OF EVEN VALUES
nums = [2,5,3,4,86,7,2,6]
result = list(filter(lambda n : n%2==0, nums))
double= list(map(lambda n : n*2 , result))
print(double) # [4, 8, 172, 4, 12]
'''
# Reduce
'''
# we should all even numbers genarated above 
# for reduce we should import reduce from functools
from functools import reduce

def add_all(a,b):
    return a + b

nums = [2,5,3,4,86,7,2,6]

result= list(filter(lambda n : n%2==0, nums))
double = list(map(lambda n : n*2, result))
sum = reduce(add_all,result)
print(sum) # 100
'''
# Decorators
'''
# x,y are function, if we want to use x in y then we use decorators
# Task - let a, b are  2 numbers and we should divide both but,
# larger number should numerator, smaller number should denomenator

def divi(a,b):
    print(a/b)

def short_divi(func):
    def inner(a,b):
        if a<b :
            a,b = b,a
        return func(a,b)
    return inner

divi1=short_divi(divi)
divi1(2,4) # 2.0
'''
# Modules
'''
from cal import *
c= multi(13,5)
print(c) # 11 
# we import cal.py (another file created by us)
# no we call use cal.py function here
'''
# Special Variable "__name__"

# ****NOTES****
# if we print __name__ it will print __main__
# Ex 1
'''
print(__name__) # __main__
# if we import __name__ it will print module where it has imported
# we are keeping main in trail.py line 40
'''
# Ex 2
'''
import trail # trail
print("name in scratch.py", __name__) # name in scratch.py __main__
# we can see that __name in trail.py print its module name called trail (line 1452)
'''
# Ex 3 Some tasks with __name__
'''
# Task - import trail.py write a funtion, print it when trail.py is first file
# or when trail.py is imported created function should not print

import trail # Nothing has printed even there is a function in trail.py
'''
# Object Oriented Programing
'''
# here 2 things class ,object
# Class - blueprint then object may Buliding
# in Class it has Attributes and Methods
# attributes means variables, Behavior means Methods[Functions]
class computer:
    
    def config(self):
        print("i5, 8gb, 466gb")

com1 = computer()
print(type(com1)) # <class '__main__.computer'>

computer.config(com1) # i5, 8gb, 466gb
# here config function change its behavier based on object
# now we are giving some function to config called com1 
# com1 is parameter or arugument
# now when we will pass config it will call com1 as aruument and get self
# self is the object which we are passing
# Another way we can do is 

com1.config() # i5, 8gb, 466gb
# Now we are using bject it self to call the function
# Behind the scene config will take comp1 as parameter, and t will pass that in self
# Mostly we can see 2nd type of syntax 
'''
# Special Method "__inti__"
'''
class computer:
    def __init__(self) :
        print("Statement 1")
    
    def config(self):
        print("i5, 8gb, 466gb")

com1 = computer() # Statement 1
com2 = computer() # Statement 1

com1.config()# i5, 8gb, 466gb
com2.config()# i5, 8gb, 466gb

# It will print 2 times becaues for every object it will called 2 times
# It is called OBJECT CREATION
'''
# Ex 2 2 computersn with different specs
'''
class computer:
    def __init__(self,cpu,ram) :
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print("Config is : ", self.cpu, self.ram)# cpu is not local variable it is object so we used self

com1 = computer("i5",16) 
com2 = computer("Ryzen 3", 8) 
# line 1514 we given 3 but here only 2 because accully by default we are passing comp1
com1.config()# Config is :  i5 16
com2.config()# Config is :  Ryzen 3 8
# line 1514 we given 3 but here only 2 because accully 3 parameters 1 obj 2 cpu 3 ram
'''
# Constructor, Self and Comparing Objects

# Ex 1 Constructor
'''
class computer():
    pass

c1 = computer()
c2 = computer()
print(id(c1)) # 140717590420696
print(id(c2)) # 140717590420696
# size of id depends up on variable 
# size allocated by Constructor
# here Constructor is computer
'''
# Ex 2 Defineing variable
'''
class computer():

    def __init__(self):
        self.name = 'Praneeth'
        self.age = 17

c1 = computer()
c2 = computer()

print(c1.name) # Praneeth
print(c2.name) # Praneeth
'''
# Ex 3 updating the values
'''
class computer():

    def __init__(self):
        self.name = 'Praneeth'
        self.age = 17

c1 = computer()
c2 = computer()

c1.name = "Pravalika"
c1.age = 18
print(c1.name) # Pravalika
print(c2.name) # Praneeth

print(c1.age) # 18
print(c2.age) # 17
'''
# Ex 3 using self and updating again
'''
class computer():

    def __init__(self):
        self.name = 'Praneeth'
        self.age = 17
    
    def update(self):
        self.name = 'Pravalika'
        self.age = 18


c1 = computer()
c2 = computer()

c1.update() # it will update c1 that is importance of self

print(c1.name) # Pravalika
print(c2.name) # Praneeth

print(c1.age) # 18
print(c2.age) # 17
# c1 = 1wst function and c2 2nd function
# https://youtu.be/ic6wdPxcHc0?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&t=315
'''
# Ex 4 comparing
'''
class computer():

    def __init__(self):
        self.name = 'Praneeth'
        self.age = 17
    def compare(self,other): # in place of other we can use c2
        if self.age == other.age:
            return True
        else:
            return False
# compare has 2 parameters who is calling it, whom to compare) 
c1 = computer()
c1.age = 30
c2 = computer()

if c1.compare(c2):
    print("they are same")
else:
    print("they are different")
# They are different
'''
# Types of variable 

# 1 instance variable
# 2 Class or static variable

# instance variable  
'''
# it is inside function ( Applicable to only c1 or c2 other wise we have to specify)
class car():


    def __init__(self):
        self.milage =18
        self.brand = 'i10'

c1 = car()
c2 = car()

# values of c1 and c2 are same
# Now we are changing / giving new values to c1
# c2 values are mentioned above 
c1.milage = 17
c1.brand= 'i20'

# Now we are printing teh values of both c1 and c2
print(c1.milage, c1.brand)# 17 i20
print(c2.milage, c2.brand )# 18 i10
'''
# Class or static variable
'''
# it is outside variable ( Applicable to both c1, c2 ...)

class car():

    wheels = 4 

    def __init__(self):
        self.milage = 20
        self.brand = 'alto'
c1 = car()
c2 = car()

c1.milage = 10
c1.brand = 'BMW'

print(c1.brand, c2.milage, c1.wheels) # BMW 20 4
print(c2.brand, c2.milage, c2.wheels) # alto 20 4

# ********NOTES*********
# The reason behind here is namespace
# namespace = namespace is aarea where u create and store object/variable
# 2 types of namespace - 1 class and 2 initance namespace
# self.milage, self.brand are stored in instance name space
# wheels are stored in class namespace 

# to change class namespace 

car.wheels= 5
print(c1.brand, c2.milage, c1.wheels) # BMW 20 5
print(c2.brand, c2.milage, c2.wheels) # alto 20 5
# when we change the class i.e. car it will affect all the objects
'''
# Types of Methods

# instance method
# class method
# static method ( in variables class and ctatic are same ) 

# Instance Method
'''
class student():

    school = 'ISRO'

    def __init__(self,m1,m2,m3):
        self.m1 =m1
        self.m2 =m2
        self.m3 = m3

# Here m1 m2 m3 are instance variable 
s1 = student(45,56,57)
s2 = student(42,75,62)
print(s1.m1,s1.m2,s1.m3) # 45 56 57
print(s2.m1,s2.m2,s2.m3) # 42 75 62
'''
# Ex 2 knowing avg
'''
# class student():

    school = 'ISRO'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

s1 = student(45,56,57)
s2 = student(42,75,62)

print(s1.avg()) # 52.666666666666664
print(s2.avg()) # 59.666666666666664
'''
# In instance there are Accessor and Mutator method
# Ex 3 Accessor and Mutator method
'''
class student():

    school = 'ISRO'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self): # Accessor
        return self.m1

    def set_m1(self,value):# Mutator
        self.m1 = value

s1 = student(45,56,57)
s2 = student(42,75,62)
# we can use get_m1 and set_m1 by 
print(s1.get_m1())# 45
print(s1.set_m1(15)) # its done
print(s1.get_m1()) # 15 
'''
# Class Method
'''
# as m1,m2,m3 are instance variable 
# school is class variable
# to work with class variable we have to use class variable  

class student():

    school = 'ISRO'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod # we should use decoraters(@classmethod) to use class method 
    def info(cls):
        return cls.school

s1 = student(45,56,57)
s2 = student(42,75,62)
# print(s1.info()) but it will print 1 if we have more than 1 it will not work
# for more than 1 we use 
print(student.info())# for using we should add @classmethod (decoraters) at line 1774
# if we have to use class method we should pass decoraters
# Outuput ISRO
'''
# static Method
'''
# When if u dont do with class or instance, do some thing new then we can use staric variable
# it can used as static instead of class,instance
class student():

    school = 'ISRO'

    def __init__(self,m1,m2,m3):
        self.m1 =m1
        self.m2 =m2
        self.m3 =m3
# now we are not using avg
    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def info():
        print('This is staticmethod statement')

s1 = student(45,56,57)
s2 = student(42,75,62)

student.info() # This is staticmethod statement
'''
# Class in class ( Inner class )
'''
class student():

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()
# I want to get all information about student with function show
    def show(self):
        print(self.name,self.rollno)
# Student need laptop and mentor want to know that configuation so creatig new class 
    class laptop:
        def __init__ (self):
            self.brand = 'hp'
            self.cpu = 'i5'
            self.ram = 8
# to create a obj laptop we shoud create inside the outerclass line 1821

s1 = student('Praneeth',23)
s2 = student('Pavan',22)

s1.show()
# to use laptop we should call it has
# print(s1.lap.brand) # hp
lap1 = s1.lap
lap2 = s2.lap
'''
# Ex 2 creating obj (laptop) directly outside
'''
# we can create obj innerclass inside the outer class
class student():

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap= self.laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class laptop:
        def __init__ (self):
            self.brand = 'hp'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = student('Praneeth',23)
s2 = student('Pavan',22)

s1.show()
#Praneeth 23
#hp i5 8 
'''
# Inheritance Getting fuction of previous class to preasent class
'''
#2 types single and multilevel inheritence

class A():
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")
class B(A): # if we keep A in B(A) then is parent and is child or super class and sub class
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")

class C(B): # c = 1,2,3,4,5 # C is multilevel inheritance
    def feature5():
        print("feature 5 is working")
a1 = A()

a1.feature1() # feature 1 is working
a1.feature2() # feature 2 is working

b1 =B()
b1.feature2() # feature 2 is working
b1.feature1() # feature 1 is working
b1.feature3() # feature 4 is working
b1.feature4() # feature 4 is working
# we can use all a features in b
# in C we can access A B features
# sub class can access the all featuers and super class cant ex c can access a , but a cna access c
'''
# Ex 3 Multiple Inheritence
'''
# if A, B are 2 class dont have inheritance
# then c want features of A B then  

class A():
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")
class B(): # B dont have any inheritance with A
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")

class C(A,B): # Now we can use features of both A B 
    def feature5():
        print("feature 5 is working")

a1 = A()

a1.feature1()
a1.feature2()

b1 = B()
b1.feature3()
b1.feature4()
c1 = C()
# we can use feature of 1,2,3,4,5
'''
# Constructor in Inheritance
# Ex 1
'''
class A():
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")

class B(A):
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")

a1 = A() # in A init
'''
# Ex 2 Problem
'''
class A():
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")

class B(A):
    def __init__(self):
        print("in B init")
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")

# Now A and B has same model(function) Whinch one it will print ? 
a1 = B()
# Ans = B
# if we create a object in sub class first it will search in sub clas and then it will search in super class
# But we need both what to do 
''' 
# Ex 3 
'''
class A():
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")

class B(A):
    def __init__(self):
        super().__init__() # super = super class now it can access all features of super class
        print("in B init")
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")

a1 = B()
# Ans = A ,B 
'''
# Ex 4 what if C has same object which one it will print ??
'''
class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working")

class B:
    def __init__(self):
        super().__init__()
        print("in B init")

    def feature3(self):
        print("feature 3 is working")

    def feature4(self):
        print("feature 4 is working")

class C(A,B): 
    def __init__(self):
        print("in B init")

    def feature5(self):
        print("Feature 5 working")

c1 = C() # it will print "in A init"
# when there are 2 then IT WILL PRINT FROM LEFT SIDE (line 2021) ACCORDING TO MRO
# MRO - method reslution order 
# Acording to it it will consider from left to right i.e. a, b 
'''
# Ex 5
'''
class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B:
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class C(A,B):
    def feature5(self):
        print("Feature 5 working")


a1 = A()

a1.feature1()
a1.feature2()

b1 = B()

c1 = C()
# Feature 1 working
# Feature 2 working
'''
# Polymorphism
'''
The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types.
or one thig in multiple forms - poly= many , morphism - forms
Types are 
Duck typing
Operator overloading 
Method overloading
Method overriding.
'''
# Duck Typing 
'''
# if some bird swims , walks, sounds like duck then it is duck 
# same if a variable 
class Pycharm:

    def execute(self):
        print("Compiling")
        print("Running")



class Laptop:

    def code(self,ide):
        ide.execute()

ide = Pycharm() # if we change ide to pyxham it will print Compiling, Running

lap1 = Laptop()
lap1.code(ide)
# Compiling
# Running
'''
# Ex 2 
'''
class Pycharm:

    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:

    def code(self,ide):
        ide.execute()

ide = MyEditor() # if we change ide to pycham it will print Compiling, Running

lap1 = Laptop()
lap1.code(ide)
# Spell Check
# Convention Check
# Compiling
# Running
# Ide behaves like duck we can change ide to pycham and myeditor we have that flexibility
'''
#2 Oparator overloading

# if we take 5+6 then 5,6 are operands and + is operator
# Ex 1 
'''
a = 5 
b  = 6 
print(a+b)#11
print(int.__add__(a,b)) # 11
# same works wih sub, multi,divi
# when we  use + = __add__,- = __sub__,*= __multi__ ....
# Thesr are called Magic operators  
'''
# Ex 2 Defining new method
'''
class student:

    def __init__(self,m1,m2):
        self.m1 =m1 
        self.m2 = m2
    
s1 = student(78,57)
s2 = student(87,77)

s3 = s1 + s2
print(s3) # error because we didn't define value of +
'''
# Ex 2 creating + operator
'''
class student:

    def __init__(self,m1,m2):
        self.m1 =m1 
        self.m2 = m2

    def __add__(self,other): # student.__add__(m1,m2)
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)
        return s3
    
s1 = student(78,57)
s2 = student(87,77)

s3 = s1 + s2 # -> student.__add__(m1,m2)
# student.__add__(78,57)
# student.__add__(87,77) 
print(s3.m1) #165
'''
# Ex 3 finding largest number
'''
class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)

        return  s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format( self.m1,self.m2)# by usig flower brackets we can use print(s1) or else we should write line 2220


s1 = Student(58,69)
s2 = Student(69,65)

s3 = s1 + s2

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")


print(s1.__str__())# we cant get str insted er get adder so we should define function 3 in line 2203

print(s2)
'''
# Method overloading

# if we have class with 2 meyhods with different parameters then it is called method overloading
# Ex 1 
'''
class student:

    def __init__(self,m1,m2):
        self.m1 =m1 
        self.m2 = m2

    def sum(self,a,b):
        s = a+b 
        return s

s1 = student(89,55)
print(s1.sum(1000,2000)) # 3000
print(s1.sum(100,200,300)) # error
# we given 2 parameters but we need 3 parameters then 
'''
# Ex 2 creating a method for passing 1,2,3 parmeters
'''
class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        
    
    def sum(self,a=None,b= None,c=None):# we keep none because default will become NONE
        s = 0 
        if a!= None and b != None and c != None:
            s = a+b+c # it will work when we pass 3 aruguments not 2 aruguments
        elif a!= None and b != None:
            s = a+b
        else:
            s = a

        return s

s1 = student(45,78)
print(s1.sum(89,98,99))# 286
print(s1.sum(5)) # 5
print(s1.sum(99,98)) # 197
'''
# Method Overriding

# Ex 1 
'''
class A:
    def show(self):
        print("Show of A")
a1 = A
a1.show() # Show of A
'''
# Ex 2 
'''
class A:
    def show(self):
        print("Show of A")

class B:
    pass
a1 = B
a1.show() # Erroe there is no variable called show 
'''
# Ex 3 
'''
class A:
    def show(self):
        print("Show of A")

class B(A):
    pass
a1 = B
a1.show() # Show of A
'''
#Ex 4 
'''
class A:
    def show(self):
        print("Show of A")

class B(A):
    def show(self):
        print('Show of B')

a1 = B
a1.show()# Show of B
# it will search in insde of that class and then it will search in sub class
'''
# Abstract class and Abstract methods
#                                 ****NOTES*****
# Abstract class - class which have abstract method
# Abstract Method - Method with declaration but not definition ( ex - pass , none ..)
# concrate class - class without abstract methods (all class which get executed)

# we cant execute abstract class so we should change abstract class to concrete class
# because cocrate class is executable
# to change abstract class to concrete we hould write all methods in concrete class
# to get abstracte class we should import ABC module 
# ABC - Abstract base class

# Ex 1
'''
class Aclass():
    
    def display(): # it is not abstact class because we should import abc module
        # we should use @abstractmethod decorator
        pass# or we can use none
'''
# Ex 2 importing abstact class
'''
from abc import ABC, abstractmethod 
class Aclass(ABC):
    @abstractmethod
    def display():
        pass
# to execute abstract class we should create another class
class demo(Aclass):
    def demo1():
        print("demo1 is working")

        
s1 = demo
s1.demo1() # demo1 is working
# we can excute abstract class
# ****we should write all method in abstract in concrete class if not it will be abstract class *****
'''
# Ex 3 
'''
from abc import ABC, abstractmethod
class Aclass(ABC):
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def show(self):
        pass
# to execute abstract class we should create another class

class demo(Aclass):
    def display(self):
        print("demo1 is working")


class demo1(Aclass):
    def show(self):
        print('show is working')
    def display(self):
        print('Display is working')


s1 = demo1()
s1.display() # Display is working
s1.show() # show is working
# https://youtu.be/4Vkt4vUrr28
# only this video only
'''
# iterator 

# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values
# Ex 1 
'''
mystr = "banana"
myit = iter(mystr)

print(next(myit))# b
print(next(myit))# a
print(next(myit))# n
print(next(myit))# a
print(next(myit))# n
print(next(myit))# a
# it will store in its memory to printed last letter and printed new letter 
'''
# Ex 2
'''
nums = [7,8,9,5]

it =iter(nums)

print(it.__next__()) # 7
print(it.__next__()) # 8

# or 

print(next(it))# 9

#it will keep in memory that how amany times does it uses and what to print next
# we do it in loops
'''
# Ex 3 iter in loops
'''
num = [7,8,9,5]

it = iter(num)

for i in num:
    print(i)
# 7,8,9,5 vertically
'''
# Ex 4 creating own iterator of ten
'''
class topten:
    def __init__(self):
        self.dev = 1 # 1 = we want to start from 1 
# we need 2 imporatnt methods 1 iter and next
    def __iter__(self):
        return self

    def __next__(self):
        val = self.dev
        self.dev += 1
        return val

values = topten()
for i in values:
    if i <= 10:
        print(i) # it start printing all values 1,2,3,4,5,6,7,8,9.......
    else:
        break
# 1-10 
'''
# or ( above one is own)
# sir one's
'''
class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <= 10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration


values = TopTen()

print(next(values))

for i in values:
    print(i) # 1-10 
'''
# Genarators
# Ex 1 
'''
def topten():

    yield 5

values = topten()
print(values) # <generator object topten at 0x0000023307EE7C10>
# we can also use print(values.__next__()) directly without creating a function
# if we use return in pace of yield then it will print 5 
'''
# Ex 2 creating loop with genators
'''
def topten():

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

values = topten()
for i in values:
    print(i)
# 1,2,3,4,5 in 
# we can also use print(values.__next__()) directly without creating a funcion
'''
# Ex 3 first 10 square numbers
'''
def square():

    n = 1

    while n<=10:
        sq = n*n
        yield sq 
        n = n+1 

values =square()
for i in values:
    print(i)
# 1, 4, 9, 4, 25, 36, 49, 64, 
'''
# Exception handling - Errors handling - Try and Except, Finally

# try will try wheather it has error or not
# except will lets you handle the error
# finally block lets you execute code, regardless of the result of the try- and except blocks 

# Errors - Compile time , logical , Run Time
# Compile time -eg Syntactical Error eg wrong spelling
# logical - error while programing or bug sloved by developer
# Run time - not defined eg 10/ 0 

# checking wheather it give error or not
# Ex 1 
'''
a = 3
b = 0
try:
    print(a/b)
except Exception :
    print('You got an error')

# 0.6  a = 3, b= 5 now we will change value
# Error when a =3 b = 0
'''
# Ex 2 checking how we got an error
'''
a = 5 
b  =0 

try:
    print(a/b)
except Exception as p :
    print("we got an error : ", p)
# we got an error : division by zero
#if we handling a server if u open a file in try and to close that file if not system may crashed then,
# we use finally and close thst file 
# we can prin some statement using finally 
finally :
    print("file closed")
# finally will print code gets error or excucuted at both scenario

# output is : we got an error :  division by zero
#             file closed
'''
# Ex 3 tell error when we get error because of x
'''
a = 5
b = 0

try:
    print("resource Open")
    print(a/b)
    k = int(input("Enter a number"))
    print(k)

except ZeroDivisionError as e: # we will error code when error is ZeroDivisionError
    print("Hey, You cannot divide a Number by Zero" , e)

except ValueError as e: # we get error when we get error is ValueError
    print("Invalid Input") # we will give alphabits in place of numbers

except Exception as e: #we get error at  all times except valueerror
    print("Something went Wrong...")

finally:
    print("resource Closed")
# resource Open
# Hey, You cannot divide a Number by Zero division by zero
# resource Closed
'''
# Multi Threading
# for beter nderstanding go to https://youtu.be/GqHLztqy0PU?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3
# thearding means doing ultiple work simultaneously 
# now we will do in python
# Ex 1 
'''
class hello:
    def run(self):
        for i in range(5): # we are writing loop insted of typeing
            print("Hello")  

class hi:
    def run(self):
        for i in range(5):
            print("Hi")  

t1 = hello()
t2 = hi()
t1.run()
t2.run()
# it will print 5 hello and then print 5 times hi
# we need hi and hello simultaneously
# by default we have one main thead but we need saparate thereds to exeute simultaneously
'''
# Ex 2
'''
from threading import *

class hello(Thread):
    def run(self):
        for i in range(500): # we are writing loop insted of typeing
            print("Hello")  

class hi(Thread):
    def run(self):
        for i in range(500):
            print("Hi")  

t1 = hello()
t2 = hi()
t1.start() # in therad there is a function called run it automatically call run when we specify start
t2.start()
# some clast happend in that it printed some hi and helo and both in one line also
# so to control time we import time package
'''
# Ex 3 increasing gap between hello and hi
'''
from time import sleep
from threading import Thread

class hello(Thread):
    def run(self):
        for i in range(5): 
            print("Hello") 
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi") 
            sleep(1) 

t1 = hello()
t2 = hi()
t1.start()
t2.start()
# printing hello and hi slowly but some errors due to some collisions
# to remove that errors Ex 4
'''
# Ex 4 to remove minute collisions in program
'''
from time import sleep
from threading import Thread

class hello(Thread):
    def run(self):
        for i in range(5): 
            print("Hello") 
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi") 
            sleep(1) 

t1 = hello()
t2 = hi()
t1.start()
sleep(0.2) # it will wait 0.2 sec and then execute the code
t2.start()
# now there are no collisions in program
# now we will keep bye where it will print ??
print("Bye")
# Hello
# HiBye
# there is a problem that at last bye should print it print in middle
'''
# Ex 5 printing bye at end
'''
from time import sleep
from threading import Thread

class hello(Thread):
    def run(self):
        for i in range(5): 
            print("Hello") 
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi") 
            sleep(1) 

t1 = hello()
t2 = hi()
t1.start()
sleep(0.2) 
t2.start()

t1.join() # it will ask t1 to join(hello) 
t2.join() # it will ask t2 to join (hi)
# by join first it will print hi and hello and at last it wil print bye

print('bye')
# Hello and hi 5 times each and then atlast it print bye
'''
# File handle

# Open,read,write,edit,copy,create .. will come under file handling

# File Opening
'''
f = open('MyData.txt','r')

print(f.read())
# Praneeth
# BORN TO EXPRESS NOT TO IMPRESS
# CAKE MURDER ON 31 MARCH
# A HYDERABAD BOY
# LOVER OF FACTS
'''
# Ex 2 - only single line
'''
f = open('MyData.txt','r')

#print(f.readline()) # Praneeth
#print(f.readline(4)) # it will print 4 characters # Born # 2378 - 1st line so it print 2nd line
print(f.readlines()) 
# ['Praneeth\n', 'BORN TO EXPRESS NOT TO IMPRESS\n', 'CAKE MURDER ON 31 MARCH\n', 'A HYDERABAD BOY\n', 'LOVER OF FACTS ']
print(f.readable()) # true
print(f.tell()) # tell how many lines are there # 99
'''
# Creating file
'''
f = open('trail1','w') # first it will check file is there or not if thwew we can edit
# if not there it will create a new file 
f.write('Something')
# Something added to trail1
f.write('print')
# Somethingprint to give space we can use , end=' ' in first sentance
# if we comment write sentance we lost all data we enter
'''
# Ex 1 not lossing data 
'''
f = open('trail1','a') # a means append i.e. it will get saved even after we remove that sentance

# f.write('Laptop')
# even after commenting there laptop term
'''
# Copying data   Mydata to trail1
'''
f = open('MyData.txt', 'r') # we are just coping so we dot need write permetion

f1 = open('trail1','w') # we have to write so we taking write permetion
# we are usig lop becaues we cant transfer each word to trail1

for i in f:
    f1.write(i)

# Mydata transfer to trail1

# we cant see the image by reading, but we ca copy image1 o image 2 
# we cant see image image but we can see the image binary code by using 'rb' in place of 'r
'''
# Linear search using python

# finding search, postion, of a letter or num from list
'''
def search(list, n) :
    i = 0 
    while i< len(list):
        if list[i] == n:
            return True
        i = i+1    
    return False

list = [5,6,7,8,1,9] # list to search 

n = 7 # number we want to search 

if search(list, n):
    print("Found")
else:
    print("Not found")
# Found 
'''
#Ex 2 finding position also
'''
pos = 0
def search (list,n):
    i = 0
    while i < len(list):
        if list[i] ==n:
            globals()['pos'] = i # globals we kept because pos is global variable and using in local variable
            return True
        i = i+1
    return False
list = [5,6,7,8,1,9]

n = 8

if search(list, n):
    print("Found", pos+1) # pos +1 = it will take int which start from 0but we need from 1 so +1
else:
    print("Not Found")
# found 4  = found at 4rd position
'''
# Same with for loop (own)
'''
pos = 0
def search (list,n):
    j = 0
    x = len(list)
    for j in range(x):
        if list[j] == n:
            globals()['pos'] = j
            return True
    return False

list = [5,6,7,8,1,9]
n= 6
if search(list, n):
    print("Found",pos+1)
else:
    print("Not Found")
'''
# Binary search (For better understanding refer https://youtu.be/DE-ye0t0oxE?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3)

# In binary search value should in assending order / sorted
#In a nutshell, this search algorithm takes advantage of a collection of elements that is already sorted by ignoring half of the elements after just one comparison. 

#Compare x with the middle element.
#If x matches with the middle element, we return the mid index.
#Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
# Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.
# for best theroy refer to the link (line 2851) or 
'''
pos = 0
def search(list,n):

    l = 0 # lower bound
    u = len(list)-1

    while l <= u:
        mid = (l+u) // 2

        if list[mid] == n :
            globals()['pos'] = mid
            return True
        else:
            if list[mid] <= n:
                l =mid + 1
            else:
                u = mid - 1
                
    return False 

list = [4,7,8,12,45,99,102,702,10987,56666]
n = 10

if search(list, n):
    print("Found at ",pos+1)
else:
    print("Not Found")

# not found
'''
# Bubble sort

# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order

# starting element compare with secound with the next element of the list
#  if the current element is greater than the next element of th list swap them
# if the current element is less than the next element , move to the next element repert step 1

# https://youtu.be/GPv7gNRR9W4
# https://youtu.be/Vca808JTbI8?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3
'''
def sort(nums):

    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp


nums = [5, 3, 8, 6, 7, 2]
sort(nums)

print(nums)
'''
# Ex 2 
'''
# Python program for implementation of Bubble Sort

def bubbleSort(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n-1):
	# range(n) also work but outer loop will repeat one time more than needed.

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j + 1] :
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
	print ("% d" % arr[i]),

'''
# Selection Sort using Python

# Even it is also same as above but we have difference that will change min value 
# at starting value it will compare with all other values find the min and replace it   

# The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

# 1) The subarray which is already sorted.
# 2) Remaining subarray which is unsorted.

# In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

# https://youtu.be/5KjapFQNxUo?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3

# Ex 1 
'''
def sort(nums):

    for i in range(5):
        min =i
        for j in range (i,6):
            if nums[j] < nums[min]:
                min = j


        temp =nums[i]
        nums[i] = nums[min]
        nums[min] = temp

        print(nums)


nums = [5, 3, 8, 6, 7, 2]
sort(nums)
print(nums)
# [2, 3, 8, 6, 7, 5]
# [2, 3, 8, 6, 7, 5]
# [2, 3, 5, 6, 7, 8]
# [2, 3, 5, 6, 7, 8]
# [2, 3, 5, 6, 7, 8]
'''
# Socket Pogramming in Python
# Socket pograming means connect 2 or more clients and make them communicate
# now we will comunicate 2 files we can use 2 systems also

import socket

s = socket.socket()
print('Socket Connected')
s.bind(('localhost',9999)) # localhost is ipadd and 9999 is port number

s.listen(3) # 3 clients can connect
print("waiting for connections")

# we are listening ( wheather clint send requrst and get connected)
# now client will send u request to connect but how many we can except 
# first it will send and we will process and loop go on 
# so we will create a loop 

while True:
    c, addr = s.accept()# when connected it will give clien soket = and addr is addr
    print(" Connected with : ", addr) # it will prin client addr

    c.send(bytes("Welcome to praneeth laptop","utf-8")) # this will send to client, client cant take str so we change it to bytes
# now we have to create a client to connect













