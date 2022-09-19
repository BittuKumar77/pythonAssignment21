# 8. Write a recursive python function to print cubes of first N natural numbers


def cubeN(n):
    
    if n==1:
        return 1
    return cubeN(n-1),n*3
cubeN(10)