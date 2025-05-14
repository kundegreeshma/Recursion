def fun(i,n):
    if i>n:
        return
    print(i,end=' ')
    fun(i+1,n)
n=int(input())
fun(1,n)