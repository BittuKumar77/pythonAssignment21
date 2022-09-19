# 5. Write a recursive python function to print first N even natural numbers.

def even(n):
    if n>0:
        even(n-1)
        print(2*n)
even(20)