# This program checks whether a number is even or odd.

num=int(input("Enter a Number:"))
if num%2==0:
    print('Even')
else:
    print("Odd")


# This program checks whether a number is divisible by 3 or not.

num1=int(input("Enter a Number:"))
if num1%3==0:
    print("This Number Divisible by 3")
else:
    print("This Number not Divisible by 3")


# This program checks whether the first character of a string is an alphabet or not.

s=input("Enter a String:")
if s[0].isalpha():
    print("First Character is an Alphabet")
else:
    print("First Character is not an Alphabet")


#This program checks whether a given string is a palindrome or not.

st=input("Enter a String:")
if st==st[::-1]:
    print("Given String is Palindrome")
else:
    print("Given String is Not a Palindrome")


#This program checks whether a given string has more than two 'a' characters.

st="banana"
if st.count('a')>2:
    print("The give string has more than two a's")
else:
    print("The give string has two or fewer a's")


#This program checks whether the length of a list is even or odd. If odd, it appends the first element to the end of the list.
lst=['apple','banana','cherry','guva']
if len(lst)%2==0:
    print(lst)
else:
    lst.append(lst[0])
    print(lst)


#This Program Checks whether a 
num2=int(input("Enter a Number:"))
if num2**num2:


#This program checks whether the length of a string is even or odd. If even, it reverses the first half and the second half separately and concatenates them. If odd, it reverses the entire string.

s=input("Enter a String:")
if len(s)%2==0:
    print(s[:len(s)//2][::-1]  +  s[len(s)//2:][::-1])  
else:
    print(s[::-1])



