#input & output statements:
#===========================


#ouput statement (print statement):
#-----------------------------------
#print is an inbuilt function which is used to print the given data in console.
#Here we can pass any number of elements and at last it accepts 2 keyword arguments.
#keyword argumnets are optional which defaultly sep=' ' & end= '\n'

#Syntax: print(ele-1, ele-2, ele-3..... sep=' ', end='\n')
#sep (separator): Which separates the elements present in print statement
#end: it prints at last of all the elements and sep


'''
print('Good Afternoon Everyone')
print('Listen Everyone Here')


print('apple', 'mango', 'dell', 'oppo')
apple mango dell oppo


print('apple', 'mango', 'dell', 'oppo', sep= ' ')
apple mango dell oppo

print('apple', 'mango', 'dell', 'oppo', sep= '')
applemangodelloppo

print('apple', 'mango', 'dell', 'oppo', sep= ', ')
apple, mango, dell, oppo

print('apple', 'mango', 'dell', 'oppo', sep= '#')
apple#mango#dell#oppo




print('shankar', 'harish', 'parama', 'yadav', 'goind', sep="-")
shankar-harish-parama-yadav-goind



print('shankar', 'harish', 'parama', 'yadav', 'goind', sep="-", end=' The End')
shankar-harish-parama-yadav-goind The End

print('Parama', end= '->')
print('Chutki', end= '\n')
print('Chota', end= '->')
print('indumathi', end= '\n')



print('chota', 'bheem', 'chutki', 'kaliya', sep=' --> ')
chota --> bheem --> chutki --> kaliya

print('chota', 'bheem',  sep=' --> ', 'chutki', 'kaliya')
SyntaxError: positional argument follows keyword argument

print('chota', 'bheem', 'chutki', 'kaliya',end=' Tata Bye Bye ', sep=' --> ')
chota --> bheem --> chutki --> kaliya Tata Bye Bye

'''

#input statement:
#---------------
#It is an inbuilt function which is used to take input at runtime.
#her we can also pass an argument to input function which to display in
#    console to ask input.
#input() reads the data always in string type.
#
#syntax: input()    or   input('message')

'''
data= input()

data= input('Enter Your Message: ')
print('Hello Everyone Listen Here, Read Double time: "', data, '"')

#Enter Your Message: Sleep at Night Not in class
#Hello Everyone Listen Here, Read Double time: " Sleep at Night Not in class "
'''

#formatting string:
#------------------
#it is used to inject/include the data into a string at runtime.
#here we have 3 types:

#1. using % operator
#2. using format method
#3. using f-string/ f-literals 

'''

name= 'Shankar'
age= 15

print('My Name is', name, 'and iam', age, 'years old')
My Name is Shankar and iam 15 years old


#1. using % operator
#using % operator include/inject the data at runtime
#use %s for string
#use %d for digit
#use %f for float  value injecting

#syntax: 'string %s string %d string %f ....'%(sting, dig, float)

print('My Name is %s and iam  %d years old'%(name, age))
      
My Name is Shankar and iam  15 years old


print('The value of pi is %f'%(3.14))
      
The value of pi is 3.140000


from math import pi
      


print('The value of pi is %f'%(pi))
      
The value of pi is 3.141593


print('The value of pi is %0.2f'%(pi))
      
The value of pi is 3.14


print('The value of pi is %0.6f'%(pi))
      
The value of pi is 3.141593

print('The value of pi is %0.10f'%(pi))
      
The value of pi is 3.1415926536


print('The value of pi is %0.15f'%(pi))
      
The value of pi is 3.141592653589793


#2. using format method
#Create a placeholders where need to include the data
#utilize formate method to work with it
#Syntax: string.format(str-1, str-2....)

name= 'Parama'
      
age= '61'
      

print('My Name is {} and iam  {} years old'.format(name, age))
      
My Name is Parama and iam  61 years old


print('My Name is {0} and iam  {1} years old'.format(name, age))
      
My Name is Parama and iam  61 years old


print('My Name is {1} and iam  {0} years old'.format(name, age))
      
My Name is 61 and iam  Parama years old


#3. using f-string/ f-literals

#create a place holder where need to include data and mention variable name in it
#Prefix a string with f (f string)

#syntax: f'string {var} string....'

name= 'Darshan'
      
age= 75
      

print('My Name is {name} and iam  {age} years old')
      
My Name is {name} and iam  {age} years old

print(f'My Name is {ame} and iam  {age} years old')
      
My Name is Darshan and iam  75 years old

'''

#date: 28-10-25
# #                       Control Statements
#
# #               Control statements are those statements which are used to control
# # the flow of execution of a program by the decision we make in certain situations
# # or conditions.
#
# #In control statements we have two types.
#
# #1. Conditional/ Decisional statement.
# #   a. If
# #   b. If else
# #   c. If elif
# #   d. Nested if
#
# #2. Looping Statement
# #   a. While
# #   b. For
#
# ### Conditional Statements:
# #   Conditional statements are those statements which will decide what to be done if
# # the condition is True and what to be done if condition is False.
#
# #if:
# #       simple if statement is used to execute some set of statements only if the
# # condition is True.
# # Here to perform this we are utilizing a keyword called 'if'.
# '''
# syntax:
# if condition:
#      ____________
#     |           |
#     |    TSB    |
#     |           |
#     |___________|
# '''
#
# #Working: In simple 'if' the True Statement Block(TSB) will be executed only if
# # the condition True, if the condition is False nothing will be executed.

'''
#1. Write a program to check whether given number is greater than 20.
num= 50
if num > 20:                                    # 50>20 --> True
    print('given number is greater than 20')    # it will enter into TSB to execute

#o/p: given number is greater than 20
'''

###2. Write a program to check given number is lesser than 100.
##num = input('Enter Your Number: ')
##
##if int(num) < 100:
##    print('given number is lesser than 100')

###3. WAP to check given number is divisible by 3 by taking user input.
##
##num = int(input('Enter a number: '))
##if num % 3 == 0:
##    print('Divisible')

###4. WAP to check given number divisible by 2 and 3.
##num = 66
##if num % 2 == 0 and num % 3 == 0:
##    print('Num is divisible by 2 & 3')      #    0     == 0 and     0   == 0
##                                            #         True   and     True
##                                            #                True 

###5. WAP to check given string is startswith vowel.
##st= 'Apple'
##if st[0] in 'AEIOUaeiou':
##    print('Startswith vowel')

###6. WAP to check given string is ending with vowel.
##st = 'Apple'
##if st[-1] in 'AEIOUaeiou':
##    print('Endswith vowel')

###7. WAP to check given string is startswith uppercase.
##st = 'Apple'
##if st[0].isupper():
##    print('startswith uppercase')
    
###without using inbuilt method
##st= 'Apple'
##if 'A' <= st[0] <= 'Z':
##    print('Startswith uppercase')

###8. WAP to check the middle char of a string is consonat.?
##st= 'subarao'
##if st[len(st)//2] not in 'AEIOUaeiou':
##    print('Middle char of st is consonant')
##

###9. WAP to check given list have even elements.
##lst= [2, 3, 6, 4]
##if len(lst) % 2 == 0:
##    print('Even elements')
##
###10, WAP to check last element of string is endswith  ing:
##l= ['python', 'is', 'programming']
##
##if l[-1].endswith('ing'):
##    print('endswith ing')


#if else:
#if-else statement is used to execute some set of statements. If the condition is
# True than the code which is present in True statement Block will be executed,
# if condition is False than some other code which is present in FSB will be
# executed.

'''
syntax:
if condition:
     ____________
    |           |
    |    TSB    |
    |___________|
else:
     ____________
    |           |
    |    FSB    |
    |___________|
'''

# Working:   In if-else, the condition will always be associated with 'if' keyword
# if ever the condition is True than the code which is present in TSB will  be
# executed.
# if ever the condition is False than the code which is present in FSB will be
# executed.


# The condition can be a True or False that means among TSB & FSB any one of the
# statement block will be executed.
#
# #Examples.

###1. WAP to check given number is greaterthan 50 or not.
##num = 55
##if num > 50:
##    print('Number is greater than 50')
##else:
##    print('Number is less than 50')

###2. WAP to check given number is even or odd.
##num = 45
##if num % 2 == 0:
##    print('Given number is even')
##else:
##    print('Given number is odd')
##
##
###3. WAP to check given number is divisible by 3 or not
##num = 64
##if num % 3 == 0:
##    print('Divisible by 3')
##else:
##    print('Not divisible by 3')
##
###4. WAP to check given string is startswith alphabet or not
##s= '#apple'
##if s[0].isalpha():
##    print('Startswith alphabet')
##else:
##    print('not Startswith alphabet')

###5. WAP to check given string is palindrome or not.
##st = input('Enter a string: ')
##if st == st[::-1]:
##    print(f'{st} is a palindrome')
##else:
##    print(f'{st} is Not a palindrome')

###6. WAP to check given string is have char 'a' more than 2 times or not.
##s= 'Banana'
##if s.count('a') > 2:
##    print(f'{s} have more than 2 a')
##else:
##    print(f'{s} have less than 2 a')

###7. WAP to check given list have even length or odd length, if it is even print it
###    directly else add first element at last and print.
##lst= ['apple', 'mango', 'grapes', 'banana', 'orange']
##if len(lst) % 2 == 0:
##    print(lst)
##else:
##    lst.append(lst[0])
##    print(lst)

###8. WAP to split the given number into two parts and sum it and check
###   it is even or not.
##num = input('Enter a number: ')
##if (int(num[:len(num)//2]) + int(num[len(num)//2:])) % 2 == 0:
##    print('Even')
##else:
##    print('odd')


#9. WAP to check length of word is even or not, if it is odd print reverse word else
#   divide word into two parts, reverse each and concatinate.
s= 'Programa'

if len(s)%2==0:
    print(s[:len(s)//2][::-1]  +  s[len(s)//2:][::-1])  
else:
    print(s[::-1])

























