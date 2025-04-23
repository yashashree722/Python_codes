# Write a Python program to find the largest element in a list.
def fun(lst) :
    largest = lst[0]
    
    for num in lst:
        if num> largest:
            largest = num
    print(largest)
    
    
nums = [10, 500, 8, 20, 3]
fun(nums)