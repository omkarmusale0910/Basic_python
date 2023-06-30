
'''
import time 
import threading

def cal_square(num_arr):
    print("calculating square")
    for num in num_arr:
        time.sleep(0.2)
        print("square :",num**2)


def cal_cube(num_arr):
    print("calculating cube")
    for num in num_arr:
        time.sleep(0.2)
        print("cube :",num**3)


# create thread and assigne a task/function and also parameters it neded 
# after creating we have to start the thread (it start excuting task/function assigne to it)
# Thread.join() used for util thread compleate its excution it wait stop afterward program excution
arr=list(range(1,6,1))


thread1=threading.Thread(target=cal_square,args=(arr,)) #args must given as tuple (arg1,)
thread2=threading.Thread(target=cal_cube,args=(arr,))

t=time.time()

thread1.start()
thread2.start()

# thread1.join()
# thread2.join()

# if we dont wirte .join() code afterword also excute .join() is used as stop excuting proram afterword 


# cal_square(arr)
# cal_cube(arr)

print("time taken by program is ",time.time()-t)

for i in range(1,600,1):
    print(f'current number is {i}')
    time.sleep(0.002)

'''

'''
# multiprocessing

from multiprocessing import Process
from threading import Thread
import time
import os


def cal_square(num_arr):
    print("calculating square")
    for num in num_arr:
        time.sleep(0.002)
        print("curr Time: ",time.time())
        print("square :",num**2)


def cal_cube(num_arr):
    print("calculating cube")
    for num in num_arr:
        time.sleep(0.2)
        print("cube :",num**3)

start_t=time.time()
process_arr=[]
thread_arr=[]
for p_num in range(os.cpu_count()+10):
    T=Thread(target=cal_square,args=([2,3],))
    thread_arr.append(T)
    # p=Process(target=cal_square,args=([2,3],))
    # process_arr.append(p)

# for process in process_arr:
#     process.start()
for thread in thread_arr:
    thread.start()


# for process in process_arr:
#     process.join()
for thread in thread_arr:
    thread.join()

end_t=time.time()
print("all process end :",abs(start_t-end_t))

'''

# print(os.cpu_count()) =8


'''

from multiprocessing import Process
from threading import Thread
import time
import os


def cal_square(num_arr):
    val=0
    for num in num_arr:
        val+=(num**2)


def cal_cube(num_arr):
    val=0
    for num in num_arr:
        val+=(num**3)

arr=list(range(1,10000000,1))
p1=Process(target=cal_square,args=(arr,))
p2=Process(target=cal_cube,args=(arr,))

t=time.time()
cal_square(arr)
cal_cube(arr)
# p1.start()
# p2.start()
# p1.join()
# p2.join()
print(time.time()-t)

# 0.031215190887451172

'''

# each process have its own memory when we want some result back from process we can not get 
# we need to used shared memory

'''
from multiprocessing import Process
from multiprocessing import Array,Value

def cal_square(num_arr,result,val):
    val.value=9.999
    for id,num in enumerate(num_arr):
        result[id]=(num**2)

arr=[1,2,3]
result=Array('i',3) #  i for integer type 'd' for double
val=Value('d',0.1)
p1=Process(target=cal_square,args=(arr,result,val))
p1.start()
p1.join()
print(result[:])
print(val.value)

# Queue in multiprocessing also used as Array as shared memory 
# it is different than normal queue which is act as inprocess memory only aceesible with in memory


'''

# lock when we are using shaired memory there is chance of irreguler behaviour(when two process try to access and change at the same time same value)
# for avoid this we used Lock in multiprocessing

'''
import multiprocessing
import time

def deposit(balance,lock):
    for i in range(100):
        lock.acquire()  # here is apply locking mechanisum
        time.sleep(0.01)
        balance.value+=1  # this is a critical secsion of a code
        lock.release()




def withdrow(balance,lock):
    for i in range(100):
        lock.acquire()
        time.sleep(0.01)
        balance.value-=1
        lock.release()


balance=multiprocessing.Value('i',200)
lock=multiprocessing.Lock()
p_1=multiprocessing.Process(target=deposit,args=(balance,lock))
p_2=multiprocessing.Process(target=withdrow,args=(balance,lock))

p_1.start()
p_2.start()

p_1.join()
p_2.join()

print(balance.value)
'''


# pool 
import numpy as np
import multiprocessing
from multiprocessing import Pool
import time



def fun(n:int):
    sum:int=0
    for i in range(n):
        sum+=(i**2)
    return sum

def fun_1(n,power):
    sum:int=0
    for i in range(n):
        sum+=(i**power)
    return sum



arr=list(range(1,100,1))
# arr_np=np.arange(1000).reshape(10,100)
# print(arr_np.shape)
# arr_np=arr_np.tolist()



if __name__=="__main__":
    pool=Pool()
    t=time.time()
    # with map we only send one argument to task
    result=pool.map(fun,arr) # pool used for map reduce here we pass function and iterable .map function divide input to multipal core
    # each core compute and after computaion it agrrigate result and retrn 
    pool.close()
    pool.join()
    print(time.time()-t)



    # with starmap  we can pass multipal agumet to task or function
    pool=Pool(processes=multiprocessing.cpu_count())
    t=time.time()
    result=pool.starmap(fun_1,list(map(lambda x:(x,2),arr))) # pool used for map reduce here we pass function and iterable .map function divide input to multipal core
    # each core compute and after computaion it agrrigate result and retrn 
    pool.close()
    pool.join()
    print(time.time()-t)
    # print(result)









