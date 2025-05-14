def armstrong(n,power):
    if n==0:
        return 0
    return(n%10)**power+armstrong(n//10,power)
num=int(input())
power=len(str(num))
if armstrong(num,power)==num:
    print("Armstrong")
else:
    print("Not Armstrong")