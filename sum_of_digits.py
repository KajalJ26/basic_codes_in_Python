def sum_digits(num):
    sum_num=0
    while num!=0:
        digit=num%10 #extracting each digit
        sum_num+=digit #adding every digit of given number to sum_num var
        num//=10 
    return sum_num    
n=123
print(sum_digits(n))
