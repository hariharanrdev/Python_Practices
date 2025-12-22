# a=input("enter a number")
# if 'A'<=a<='Z':
#     print(f"{a} is an UC")
# elif 'a'<=a<='Z':
#     print(f"{a} is an LC")
# elif '0'<=a<='9':
#     print(f'{a} IS AN Digit')
# else:
#     print(f'{a} is an SC')

# consider two coordinates extend by and check which quadrants those two points are present.

x=int(input("enter a number"))
y=int(input("enter a number"))
if x>0 and y>0:
    print("first quadrant")
elif x>0 and y<0:
    print("second quadrant")
elif x<0 and y>0:
    print("third quadrant")
else:
    print("fourth quadrant")