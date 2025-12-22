# Looping Statement
# Looping Statement is a CONTROL statement which will control the flow of execution by reapting the same task again and again for n number of times
# while loop
# for loop

# while loop:
#     It is a looping statement which is used to execute the same set of instructions repeatively again and again untill my condition fails.
#     2-things are mandatory:
#     1. condition
#     intialization if the looping variable
#     updation

# write a program to find the factorial numberes.

num=int(input("Enter a Number"))
i=1
fact=1
while i <= num:
    fact=fact*i
    i+=1
    print(fact)


#write a program print the n natural numbers
n=int(input("Enter a Number"))
i=1
while i<n:
    print(i,end='')
    i+=1


#extract even numberse between the erange for 1 to 50
        
n=int(input())
i=2
while i<=n:
        print(i, end=' ')
        i+=2

# find the sum of n natural numbers
n=int(input("Enter a Number"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i+=1
print(sum)

#find the product of n natural numbers
n=int(input("Enter a Number"))
i=1
product=1
while i<=n:
    product=product*i
    i+=1
print(product)

#find the sum of even numbers between 1 to n
n=int(input("Enter a Number"))  
i=2
sum=0
while i<=n:
    sum=sum+i
    i+=2
print(sum)

#find the sum of odd numbers between 1 to n
n=int(input("Enter a Number"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i+=2
print(sum)

#find the reverse of a given number
n=int(input("Enter a Number"))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)


#Wap to reverse a given string
S=input
i=0
rev=""
while i<len(S):
    rev=S[i]+rev
    i+=1
print(rev)

#check how many alphabets in the string
s=input("g00d night") 
i=0
count=0
while i<len(s):
    if <'a' <= [i] <='z' or 'A' <= s[i] <='Z':
        count += 1
    i += 1
print(count)


#WAP to check whether even upper case alphabets or odd uppercasea are there.
s='pRoGrAmminG'
i=0
count=0
while i < len(s):
    if 'A' <= s[i] <= 'Z':
        count += 1
    i += 1
if count % 2 == 0:
    print('Words have even Upper case numbers')
else:
    print('Words have odd Upper case numbers')
    

#WAP to check whether given string have any special characters.

s = input("Enter a string: ")
i = 0
count = 0
while i < len(s):
    if (s[i] < '0' or s[i] > '9') and (s[i] < 'A' or s[i] > 'Z') and (s[i] < 'a' or s[i] > 'z') and s[i] != ' ':
        count += 1
    i += 1

if count > 0:
    print("String has special characters")
else:
    print("No special characters")


#WAP to check a number is having

num=1234
rev=0
while num>0:
    rev+=10
    rev +=num%10
    num = num// 10
print(rev)

#WAP to check a number is prime or not
num=int(input("Enter a Number"))
prime = True
i=2
while i<num:
    if num%i==0:
        prime=False
    i+=1
if prime:
    print("Number is prime")
else:
    print("Number is not prime")



# compute Armstrong total

# Get the number from user
n = int(input("Enter a number: "))

# Count number of digits (order)
temp = n
order = 0
while temp > 0:
    order += 1
    temp //= 10

# Handle special case for 0
if n == 0:
    print("Number is armstrong")
else:
    # Calculate sum of digits raised to power of order
    temp = n
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** order
        temp //= 10

    # Check if number is Armstrong
    if total == n:
        print("Number is armstrong")
    else:
        print("Number is not armstrong")




#Wap to check the given number is palindrome or not
num = int(input("Enter a Number: "))
n = num
if n < 0:
    print("Number is not palindrome")
else:
    rev = 0
    temp = n
    while temp > 0:
        LD=temp % 10
        rev = rev * 10 + LD
        temp //= 10

    if rev == n:
        print("Number is palindrome")
    else:
        print("Number is not palindrome")
