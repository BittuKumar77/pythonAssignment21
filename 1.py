# 1. Write a recursive python function to print first N natural numbers.

def Number(n):
    if n>0:
        Number(n-1)
        print(n,end =" ")
n=10
Number(n)