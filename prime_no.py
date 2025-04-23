def prime_no(no):
    if no <2 :
        return False
    for i in range(2, int(no**0.5)+1):
        if no %i == 0 :
            return False
    return True
        
    
    
ans =prime_no(20)
print(ans)