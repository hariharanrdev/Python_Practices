# Arguments
# -Positonal Arguments
# -Keywords Arguments

# Positonal Arguments
def add(a,b, c, d):
    print(a+b+c+d)
add(10,20,30,40)

# Keywords Arguments
def add(a,b, c, d):
    print(a+b+c+d)
add(a=10,b=20,c=30,d=40)


# Combination of Positonal and Keywords Arguments
def add(a,b, c, d):
    print(a+b+c+d)
add(10,20,c=30,d=40)

# combination of only positional and keyword arguments
def add(a,b, /, *, c, d):
    print(a+b+c+d)
add(10,20,c=30,d=40)


# variable number of positional arguments (tuple_positional_arguments)
def add (*coll):
    print(coll)
add(10,20,30,40)

# variable number of keyword arguments(dictionary_keyword_arguments)
def add(**kwargs):
    print(kwargs)
add(a=10,b=20,c=30,d=40)

# combination of positional and keyword arguments
def add(*args, **kwargs):
    print(args)
    print(kwargs)
add(10,20,30,40,a=10,b=20,c=30,d=40)
