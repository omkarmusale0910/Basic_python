
def sqrt_op(n):
    s=1.0
    e=n*1.0
    diff=0.0000000001
    while((e-s)>=diff):
        mid=(s+e)/2.0
        if(mid*mid<=n):
            s=mid
        else:
            e=mid
    return e

def power_op(a,n):
    ans=1
    while(n>0):
        if(n%2==1):
            ans=(ans*a)
            n-=1
        else:
            a=(a*a)
            n/=2
    return ans

# print(power_op(2,6))
# print(sqrt_op(25))

def power_seq(a,n):
    ans=1;
    for i in range(n):
        ans*=a;
    return ans;