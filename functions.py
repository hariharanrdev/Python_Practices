#wap to check given number is palindrome or not



#wap to check is it kaprekar number or not
# algo:square,split into two, check sum

def is_kaparekar (num):
    sq = num* num
    n=sq
    l = 0
    while n:
        n // = 10
        ln+=1
    ln // = 2
return num == ((sq// (10 ** ln))) + (sq % (10 ** ln))




#waf to convert binary to decimal

1



#waf to convert decimal to binary





#wap to check given number is automorphic or not

def isautomorphic(num):
    sq = num * num
    temp_num = num
    len_ = 0
    while temp_num > 0:
        temp_num //= 10
        len_ += 1
    divisor = 10 ** len_
    return num == (sq % divisor)