# 9. Write a recursive python function to print first N multiples of a given number.

def first_multiple(n,num_multiples):
    if num_multiples <=0:
        print(end=" ")
    else:
        print(n,end=" ")
        first_multiple(n+n,num_multiples-1)
            
