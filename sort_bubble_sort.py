def bubble_sort(lst) :
    n = len(lst)
    for i in range(0, n) :
        for  j in range(0 , n-1):
            if lst[j] > lst[j+1]:
                lst[j] , lst[j+1] = lst[j+1] , lst[j]
    return lst
    
    
    

nums = [5,2,1]
ans =bubble_sort(nums)
print(ans)