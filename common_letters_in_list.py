# Write a Python program to find the common elements between two lists.
def common_list(list_a,list_b):
    common_ele =[]
    for item in list_a:
        if item in list_b:
            common_ele.append(item)
    return common_ele



list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
ans =common_list(list_a , list_b)
print(ans)