def prime(n,i=2):
    if i*i>n:
        return True
    if n%i==0:
        return False
    return prime(n,i+1)
def fun(l,i=0):
    if i==len(l):
        return 0
    if prime(l[i]):
        return 1+fun(l,i+1)
    else:
        return fun(l,i+1)
l=list(map(int,input().split()))
print(fun(l))