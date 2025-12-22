input=456789
output=789654

n=456789
last_3=n%1000   #taking last 3 digits from the string.
first_3=n//1000   #taking first 3 digits from the string.
temp = first_3   #storing first_3 in temp variable to reverse it.
rev_first = 0   #variable to store reversed first_3 digits.
while temp>0:   #loop to reverse the first_3 digits.
    ld = temp%10   #getting last digit of temp.
    rev_first = rev_first*10 + ld    #forming the reversed number.
    temp = temp//10   #getting remaining digits after removing last digit.
print(str(last_3)+str(rev_first))   #concatenating last_3 and reversed first_3 and printing the result.



def reverse_first_lasthree_numbers(n):
    last_3 = n % 1000
    first_3 = n // 1000
    temp = first_3
    rev_first = 0
    while temp > 0:
        ld = temp % 10
        rev_first = rev_first * 10 + ld
        temp = temp // 10
    return int(str(last_3) + str(rev_first))