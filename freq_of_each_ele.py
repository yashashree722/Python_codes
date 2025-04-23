def freq_ele(nums):
    freq ={}
    
    for i in nums:
        if i  in freq:
            freq[i] +=1 
        else:
            freq[i] =1 
    return freq
    
    
    

num = [11,4,3,2,1,1,11,2,2,1,1,3,3,3,3]    
ans =freq_ele(num)
print(ans)