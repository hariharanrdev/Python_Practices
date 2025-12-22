# Nested IF:
# whenever the multiple condition should be check like condition inside the condition at the time we will be using nested if.
# if condtion inside another condition
# or
# whenver we want to check the condition  before checking the another condtion then we go with nested if condtion

# syntax:
# if condtion:
#     if condtion: - true statement block
#     else: - False sattement block

# else: - False statement block


#eval is useed to change the string input to the required data type like int, float, list, tuple, dict etc.

#write a program to check given character is vowel or consonant

a=eval(input())
if a.isalpha():
    if a.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(f"{a} is a vowel")
    else:
        print(f"{a} is a consonant")
else:
    print("invalid input")


a=eval(input())
if 'A'<=a<='Z' or 'a'<=a<='z':
    if a in 'aeiouAEIOU':
        print(f"{a} is a vowel")
    else:
        print(f"{a} is a consonant")
else:
    print("invalid input")


# write a program to loginto instagram by entering the proper username and password 
username="admin"
password="admin123"
username1=input("Enter username:")
password1=input("Enter password:")

if username1==username:
    if password1==password:
        print("login successful")
    else:
        print("invalid password")
else:
    print("invalid username")

# write a program to print reverse of the string only if it s starting with  uooer case alphabet and ending with digit.

s=input("Enter string:")
if 'A'<=s[0]<='Z':
    if s[-1].isdigit():
        print(s[::-1])
    else:
        print("string is not ending with digit")
else:
    print("string is not starting with upper case alphabet")


#write a program to check the greatest number among three numbers

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))

if num1>=num2:
    if num1>=num3:
        print(f"{num1} is greatest number")
    else:
        print(f"{num3} is greatest number")
else:
    if num2>=num3:
        print(f"{num2} is greatest number")
    else:
        print(f"{num3} is greatest number")

# 04-11-2025

#write porgram to check the second greatest number among four digits.

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
num4=int(input("Enter fourth number:"))

if num1>=num2 and num1>=num3 and num1>=num4:
    if num2>=num3 and num2>=num4:
        print(f"{num2} is second greatest number")
    elif num3>=num2 and num3>=num4:
        print(f"{num3} is second greatest number")
    else:
        print(f"{num4} is second greatest number")

elif num2>=num1 and num2>=num3 and num2>=num4:
    if num1>=num3 and num1>=num4:
        print(f"{num1} is second greatest number")
    elif num3>=num1 and num3>=num4:
        print(f"{num3} is second greatest number")
    else:
        print(f"{num4} is second greatest number")
        
elif num3>=num1 and num3>=num2 and num3>=num4:
    if num1>=num2 and num1>=num4:
        print(f"{num1} is second greatest number")
    elif num2>=num1 and num2>=num4:
        print(f"{num2} is second greatest number")
    else:
        print(f"{num4} is second greatest number")