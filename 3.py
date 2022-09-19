# 3. Write a recursive python function to print first N odd natural numbers

def odd(n,count=1):
    if (count<=n):
        print(2*count-1)
        odd(n,count+1)
odd(10)