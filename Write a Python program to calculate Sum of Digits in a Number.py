def fun(num):
    num_str  = str(num)
    sum =0
    
    for digit in num_str:
        sum += int(digit)
    return sum


ans =fun(12345)
print(ans)
        
    