# 7. Write a recursive python function to print squares of first N natural numbers

def squareN(n):
    
    if n==1:
        return 1
    return squareN(n-1),n*n
squareN(10)
