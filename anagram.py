# Write a Python program to find Anagram Check?
def anagram(str1, str2):
    return sorted (str1) == sorted(str2)



str1 ="lisen"
str2 = "silent"
ans =anagram(str1, str2)
print(ans )