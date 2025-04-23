# Write a Python program to Count Vowels in a String



def check_vow(my_str):
    vow ='aeiouAEIOU'
    count =0
    for s in my_str:
        if s in vow:
            count +=1 
    return count

input_str = "Hello, World!"
ans =check_vow(input_str)
print(ans)