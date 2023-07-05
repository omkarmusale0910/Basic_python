import retry
import random

@retry.retry(exceptions=ZeroDivisionError,tries=5,delay=1,backoff=2)
def fun():
    a=10
    b=random.randint(0,1)
    print(a,b)
    c=a/b
    return c


print(fun())