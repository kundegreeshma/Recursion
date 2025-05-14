def reduceToOne(n,steps=0):
    if n==1:
        return steps
    elif n%2==0:
        return reduceToOne(n//2,steps+1)
    else:
        return min(reduceToOne(n+1,steps+1),reduceToOne(n-1,steps+1))
n=int(input())
print(reduceToOne(n))

'''
def fun(n):
    if n==1:
        return 0
    elif n%2==0:
        return 1+fun(n//2)
    else:
        return 1+min(fun(n-1),fun(n+1))
n=int(input())
print(fun(n))'''