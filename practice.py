# print("hellow world")

# is_male=True
# age=20
# name="omkar musale"
# gender="x"
# if(is_male):
#     gender="male"
# else:
#     gender="female"


# print("name of a student is "+name+" his age is "+str(age)+" his is "+gender)


str="omkar, prakash musale"

# print(str.upper())
# print(str.lower())
# print(str.islower())

# print(str[2])
# print(str[2:12])

# print(len(str))
# for i in range(len(str)):
#     if(str[i]!=" "):
#         print(str[i],end="")

# str.index("musa")
# print(str.index("musa"))
# l=str.split()
# l1=str.split(", ")
# print(l1+l)

# 22*7 =180
# x    =45 

# import math
# a=10
# b=2.5
# print(pow(a,6))
# print(a**6)
# print(b**2)
# print(type(pow(b,2)))
# print(math.ceil(b))
# print(math.floor(b))
# print(math.factorial(4))
# print(math.log2(16))
# print(math.tan(22/(7*4)))
# print(math.tan(math.pi/4))
# print(min(2,8,96)) # sililar max
# other fun abs,

# till=range(1,10,2)
# for i in till:
#     print(i)

# for i in range(1,13,2):
#     print(i)
# for i in range

# x=None
# print(x)
# x=123
# print(x)

# if("musale" in str):
#     print("musale is present in string ")

# print(15//2) # floor division it return only int part of ans
# l=[8,9,6,4,7,6,1,2,3,56,45,6,9,10]
# print(l)
# l.sort()
# print(l)
# a=l.pop()
# print(a)
# l1=l[::2] # sliceing return list 
# print(l1)
# l.insert(1,1000)
# print(l)
# l.remove(6);
# print(l)

# touple
# t1=(1,2)
# print(type(t1))

# x,y,z=(1,2,3);
# print(x,y,z) # by addding comma it take space between the value

# def fun():
#     print("fun1");
# def fun(a):
#     print("fun2");
# def fun(a,b):
#     print("fun3");

# fun funtion has assigne to letest function


# recursion
# f=[0]*1001;
# def fact(a):
#     if(a==0):
#         return 1;
#     elif(f[a]!=0):
#         return f[a];
#     f[a]=a*fact(a-1);
#     return f[a]


# for i in range(1,11):
#     print(fact(i));


# l=[1,2,3,4,5,6,7]
# while(l):             #when list become empty it become boolean false
#     print(l.pop())


# if else   or not and

# if statement can not be empty 
# if(11>10):
#     pass
# else:
#     print("xyz")

# if we there is not a single line of code in if statement than we can give pass keyword


# dicstonary
# dict1={
#     1:1,
#     2:4,
#     3:9,
#     4:"4^2=16"
# }
# print(dict1)

# dict2=dict(name="omkar",age=20,ismale=True)
# for x in dict2:
#     print(x)

# for x in dict2.keys():
#     print(x);
# for y in dict2.values():
#     print(y);
# for x,y in dict2.items():
#     print(x,y);


# any condition statement can not empty 
# like function  def,if ,for 
# for i in range(6):
#     pass 

# Dict=dict();
# print(type(Dict))
# for i in range(10):
#     Dict.update({i:i*i})
    
# print(Dict)

# print(Dict.get(10,"not fount")) 
# # print(Dict[10])  # if key is not in dict and we want to acces it with this method we get error


# coverting vowels to # in given string 
# vowels=['a',"e","i","o","u"]
# new_str=''
# for i in range(len(str)):
#     if(str[i] in vowels):
#         l1=list(new_str);
#         l1.append('#');
#         new_str=''.join(l1);
#     else:
#         l1=list(new_str);
#         l1.append(str[i]);
#         new_str=''.join(l1);
# print(new_str)
        
# new_str1=None
# l2=list(str);
# for i in range(len(l2)):
#     if(l2[i] in vowels):
#         l2[i]="#";

# # print(l2)
# # str[0]='a' # this kind of assigement is not work in python 
# new_str1=''.join(l2);
# print(new_str1)



# try catch block
# try:
#     a=10/0
# except ZeroDivisionError as err:
#     print(err)
# except:
#     print("some error is occered in code")

# # in above example if error get as Zero.. err than only that block is excuted 


# try:
#     a=int(input("enter the num1"))
#     b=int(input("enter the num2"))
#     if(a<b):
#         raise Exception("resultant value is <1")
#     c=a/b
# except ZeroDivisionError as e1:
#     print(e1)
# except ValueError as e2:
#     print(e2)
# except :
#     print("some unknow error is occer ")


# user define exception
# class lessThanZeroException(Exception):
#     def __init__(self,message):
#         self.message=message;


# try:
#     a=int(input("enter num1"))
#     b=int(input("enter num2"))
#     if(a<b):
#         raise lessThanZeroException("value of divident is less than value of divisor")
# except lessThanZeroException as err:
#     print(err);
# except:
#     print("some error is occerds")



# file 
'''
we can create a file with 'a' ,'w', 'x' mode 
and also 2 etra modes like binery and text 
text mode is default
but for binery 
'rb' read in binery  
'''

# try:

#     f1=open('college.txt','x')
#     if(f1):
#         print("file create sucssesfully")
#     f1.close()
# except:
#     print("file is already exits")
# finally:
#     choice=int(input("1:write \n2:append \ndefault:read"))
#     if(choice==1):
#         # pass 
#         f1=open('college.txt','w')
#         if(f1.writable()):
#             print("file in writable mode")
#             str=input("write into file")
#             f1.write(str);
#             f1.close()
#     elif choice==2:
#         f1=open('college.txt','a')
#         if(f1.writable()):
#             print("file is in append mode")
#             str=input("append into file")
#             f1.write("\n"+str);
#             f1.close()
#     else:
#         f1=open('college.txt','r')
#         if(f1.readable()):
#             print("file in read mode")
#             print(f1.read())
#             f1.seek(0)
#             list1=f1.readline() # just reed one line 
#             print(list1)
#             f1.seek(0)
#             list1=f1.readlines(); # return every line in file 
#             print(list1)
#             f1.close()
       

# # for delete the file 
# # import os
# # os.remove('college.txt')




# class 

# class Person:
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender

#     def p(self):
#         print(f'name of the person is {self.name} age of a person is {self.age} and his gender is {self.gender}')


# p1=Person("omkar musale",20,"male")
# p1.p()


# inheritance 

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def p(self):
#         print(f'name of the person is {self.name} age of a person is {self.age} ')


# class Student(Person):
#     def __init__(self,name,age,roll_no):
#         super().__init__(name,age)
#         self.roll_no=roll_no
#     def funp(self):
#         print(self.roll_no)
#         self.p()


# std=Student("omkar",20,8);
# std.funp();


# variable length argument 
#  by using * and ** 
# def fun(*args):
#     ans=1
#     for x in args:
#         ans*=x;
#     return ans;

# print(fun(1,2,4,5,3,0))

# if the argument is in the form of key pair than used ** with variable length argument


# def fun1(**args):
#     for x,y in args.items():
#         print(x,y);


# fun1(name="omkar",age=10,is_male=True)


# # lamda function it is maily used in reduce and map method and u
# lam1=lambda *args:max(args)

# print(lam1(2,3,5,9))

# lam2=lambda x,y,z:x+y+z
# print(lam2(1,2,3))
# lam2=lambda x,y,z:x+y+z
# # print(lam2(1,2,3))
# list1=[(1,2),(2,-3),(-4,100),(-4,101),(100,8)]
# list1.sort() # this sort based of 1st argument is 1 parameter is same then only it sort based of second argument
# print(list1)
# list1.sort(key=lambda x:x[1])
# print(list1)


# without using lamda 
# def sorting(l):
#     ans=0
#     for x in l:
#         ans+=x
#     return ans

# two_D_list=[[1,2,3],[4,5-2],[-52,36,23],[0,-9,4]]
# two_D_list.sort(key=sorting)
# print(two_D_list)


# map 
# this usefull when we want to appaly function to list of input
# map(function,input_list)
# num=[1,2,3,4,5,6]
# sq=[]
# sq=list(map(lambda x:x*x,num))
# print(sq)

# list_input contain function 
# import math
# squ=lambda x:x*x
# cube=lambda x:x**3
# sqrt=lambda x:math.sqrt(x);

# funcs=[squ,cube,sqrt] #list of functions
# l=[]
# for i in range(10):
#     l.append(list(map(lambda x:x(i),funcs)))

# print(l)



# filter
# we can applay filter on list of element and filter appropriate element 
# print(type(range(-5,5)))
# R=range(-5,5)
# value_even=list(filter(lambda x:not(x&1),R))
# print(value_even)



# reduce
# l=[1,2,3,4,5]
# from functools import reduce
# value=reduce(lambda x,y:x*y,l)
# add_value=reduce(lambda x,y:x+y,l)
# print(value,add_value)

