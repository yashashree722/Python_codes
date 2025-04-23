#  Write a Python program to find Fibonacci Sequence?
def fib_seq(n) :
    fib =[0,1]
    for i in range (2,n) :
        next_terms = fib[-1] + fib[-2]
        fib.append(next_terms)
    return fib

num_terms = 10
fib_sequence = fib_seq(num_terms)
print("Fibonacci sequence up to", num_terms, "terms:", fib_sequence)