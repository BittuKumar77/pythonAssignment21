# 6. Write a recursive python function to print first N even natural numbers in reverse
# order.

def evenRev(n):
    if n>0:
        print(2*n,end=" ")
        evenRev(n-1)
        
evenRev(20)