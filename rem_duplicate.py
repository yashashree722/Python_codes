def rem_duplicate(lst) :
    unique_list =[]
    n = len(lst)
    
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
ans = rem_duplicate(nums)
print(ans)