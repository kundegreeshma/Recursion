def s(li,i=0):
    if i==len(li):
        return 0
    return li[i]+s(li,i+1)
li=list(map(int,input().split()))
print(s(li))