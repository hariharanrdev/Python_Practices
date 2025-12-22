class Demo:
    a=10  # Class variable
    b=20  
obj1= Demo() #object creation
obj2= Demo()
print(obj1.b)
print(obj2.b)
obj1.a=70
obj2.b=100
print(obj1.a)
print(obj2.b)

print(Demo.a)
print(Demo.b)