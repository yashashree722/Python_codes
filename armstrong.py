#  Write a Python program to check for Armstrong Number?
def fun(number):
    str_num = str(number)
    
    str_len = len(str_num)
    
    armstrong_no=0
    for digit in str_num:
        armstrong_no += int(digit) **str_len
    return number ==armstrong_no


ans =fun(153)
print(ans)