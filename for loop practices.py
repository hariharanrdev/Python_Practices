#write a program to check the given number is present in loop even or odd 
#if it s even print jinga 
# if it is odd prinnt lala

coll=[1,2,3,4,5,6,7,8,9,10]
for i in coll:
    if i%2==0:
        print("jninga",end=" ")
    else:
        print("lala", end=" ")


#wap to print only vowel strat words from the collection

coll=['google','apple','microsoft','amazon','facebook','ibm']
for i in coll:
    if i[0] in 'aeiouAEIOU':
        print(i,end=' ')
    else:
        print(i,"Doesn't Starts with Vowels",end=' ')

#added to string
coll=['google','apple','microsoft','amazon','facebook','ibm']
for i in coll:
    res=[]
    if i[0] in 'aeiouAEIOU':
        res.append(i)
print(res)

    '''WAP to print a collection have tuples of elements tuple have 1st element is word second element as ✔️ if element
     startswith uppercase ❌ for lowercase startting else print ➖'''

coll=['Google','apple','Microsoft','amazon','Facebook','ibm','123abc']
res=[]
for i in coll:
    if i[0].isupper():
        res.append((i,'✔️'))
    elif i[0].islower():
        res.append((i,'❌'))
    else:
        res.append((i,'➖'))
print(res)


#coll=[('Google','✔️'),('apple','❌'),('Microsoft','✔️'),('amazon','❌'),('Facebook','✔️'),('ibm','❌'),('123abc','➖')]

#wap to create a dictionary of word and reverse word pairs from a given collection
coll=['google','apple','microsoft','amazon','facebook','ibm']
res={}
for i in coll:
    res[i]=i[::-1] #res[key]=value
print(res)

#wap to print a dictionary have word and length of word length pair
#if word startswith vowel else word and rev word pair

coll=['google','apple','microsoft','amazon','facebook','ibm']
res={}
for i in coll:
    if i[0] in 'aeiouAEIOU':
        res[i]=len(i)
    else:
        res[i]=i[::-1]
print(res)

#assignments
