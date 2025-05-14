def rev(n,re=0):
    if n==0:
        return re
    d=n%10
    re=(re*10)+d
    return rev(n//10,re)
num=int(input())
print(rev(num))