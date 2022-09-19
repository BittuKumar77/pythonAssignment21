# 4. Write a recursive python function to print first N odd natural numbers in reverse order

def oddReverse(n):
    if n==1:
        print(1)
    else:
        print((2*n)-1)
        oddReverse(n-1)
oddReverse(10)