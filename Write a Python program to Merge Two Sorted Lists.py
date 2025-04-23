# Write a Python program to Merge Two Sorted Lists?

def merge_lits(lst1 , lst2) :
    
    n = len(lst1)
    m = len(lst2)
    marge_list =[]
    
    i =  j =0
    
    while i <n  and j<m:
        if lst1[i] < lst2[j] :
            marge_list.append(lst1[i])
            i = i+1
        else:
            # lst2[j] <lst1[i]:
            marge_list.append(lst2[j])
            j = j+1
        
    while i <n :
        marge_list.append(lst1[i])
        i = i+1
    
    while j <m :
        marge_list.append(lst2[j])
        j = j+1
        
    return marge_list


list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
ans =merge_lits(list1 ,list2)
print(ans)
        
        
    
            
    
        