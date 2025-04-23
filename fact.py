# Write a Python program to find the factorial of a number.


def fact(num) :
    if num ==0 :
        return 1 
    else:
        return num * fact(num-1)
    
    
ans =fact(5)
print(ans)