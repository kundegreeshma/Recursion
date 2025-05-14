def fun(n,i=0):
    if n==i:
        return
    print(i+1,end=' ')
    fun(n,i+1)
    if i!=(n-1):
        print(i+1,end=' ')
n=int(input())
fun(n)


    