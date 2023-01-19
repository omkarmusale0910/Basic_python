# print("hellow")
# print("     /|")
# print("    / |")
# print("   /  |")
# print("  /   |")
# print(" /____|")
#



#there are three basc datatype in python number (int ,or float),boolean ,string

# is_male=True
# age=50
# name="omkar muale"
# print("the name of student is "+name+" he is a good student")
# print("he is "+str(age)+" year old") # here age in an integer data it cannot concate with string we need to convert into string
# # with str() function
# print(is_male)

# srings
# str="Omkar Musale"
# print(str.upper())
# print(len(str))
# a=len(str)
# print(a)
# a=a+100
# print(a)
# print(str.lower().islower())
# print(str[0])
# print(str + "\nstudent\"") #backslash \n is used for newline
# print(str.index('O'))
# print(str.index("Musa"))

# playing with number and maths function
# from math import *   #here math is module which contain lots of function releted to math_opration
# a=10
# print(5+8)
# print(pow(2,3))
# print("value of 10^3 is "+str(pow(a,3)))
# print("power of 2 ^3 is "+str(round(pow(2,3))))
# print(sqrt(8))
# print(abs(-8))
# print(floor(2.4))
# print(ceil(2.6))

# taking input from user with input() method
# print("enter yore name ")
# name=input()
# age=input("enter your age  ")#this take as a string not a number
# print("age of "+name+" is "+age)



# age=float(input("enter the age of person "))
# name=input("enter the name of a person ")
# print("the age of "+name+" is "+str(age))



# list
# its a array which contain element (it may be off different data type)
# college=["omkar",208,True,"atigre","pccoe","IT"]
# #         0       1    2     3        4      5
# #        -6      -5   -4    -3       -2     -1
# we can access element with this index

# print(college)
# print(college[2])
# print(college[-4])
# college[0]="sushant"
# print(college)
# print(college[2:])
# print(college[-4:])
# #with this syntax it can give list from [a:] a index to last index (a-> last element)
# print(college[1:3])  #from 1 ->(<3) it not include 3 index element
# print(college[-5:-3])
# college[2]="musale"  # we can change data type of an list element also
# print(college)
# print(len(college))


# Method on List
# list1=[45,36,4,5,9,3,6,6,23,6]
# print(list1)
# list1.append(50)
# list1.sort()
# print(list1)
# list1.insert(2,"inseted_elemet")
# print(list1)
# item=list1.pop()  # pop() method return last elemnet and delete also
# print(list1)
# # list1.sort() #this give erroe because list contain int and string there fore it can not compair int and string \
# # print(list1)
#
# list1.remove("inseted_elemet")
# print(list1)
# list1.reverse()
# print(list1)
# print(list1)
# print(list1.count(6))
# list1.remove(6) # this just remove 1 st occerence of 6 element
# print(list1)


# touple but
#  the main difference btw touple and list is list is mutable but touple is Unmutable (we can not modify it)
# another diff btw them is for creating touple we used () bracket for creating list we used [] bracket
# touple1=(2,3,5,"bbjasbc")
# print(touple1)
# print(touple1[2])
# print(touple1[-1])
# # touple1[0]=45   # this line gives error .
#
# List1=[(23),(1,2,6),("bascvaj",'d'),True]
# print(List1[1])

#basic function
# for writing funtion we use keyword def funtion_name():
# def fun():
#     print("hellow user :")
#     #all the code inside the funtion must be indented
#
# print("top")
# fun()
# print("bottom")
#
#
# def fun(name,age):
#     print("name of an user is "+name)
#     print("age of user is "+str(age))
#
# def fun(name):
#     print("name of an user is "+name) # this overwirte the function now fun named function need only need one parameter there
# #     compiler take letest funcion
#
# fun("omkar",12) # this also give an error s
# # fun() this gives an error
# fun("omkar musale") this is called because this function with one parameter is define at last


# return
# def power(n):
#     L1=[n,n*n,n*n*n,n*n*n*n]
#     return L1
#
# def cube(n):
#     return (n*n*n)
#
# print(cube(3))
#
# a=int(input("enter the number : "))
# n=int(input("enter the power of number you want {1->4}"))
# L1=power(a)
# print(L1[n-1])
# print(L1)



# # if  statement
# is_male=True
#
# if is_male:
#     print("user is male ")
#     print("user is not Female")
#
# #if else
#
# if is_male:
#     print("user is male ")
# else:
#     print("user is not male ")
#
# # else if
#
# is_tall=False
# # complex or simpal statement can be wrriten in (condition)  bracket
# # and , or , not()  this are a conditional opeator


# if is_tall and is_male:
#     print("user is male and tall")
# elif is_tall and not(is_male):
#     print("user is tall but not male ")
# elif not(is_tall) and is_male:
#     print("user is male but not tall")
# else:
#     print("user is not male and tall")



# if else statement with operator
# n1=int(input("enter the first number: "))
# n2=int(input("enter the second  number: "))
# n3=int(input("enter the third number: "))
#
#
# if (n1>=n2 and n1>=n3):
#     print(str(n1)+" is a greater number ")
# elif n2>=n1 and n2>=n3:
#     print(str(n2)+" is a greater number ")
# else:
#     print(str(n3)+" is a greater number ")

# def calculator(n1,n2,op):
#     if(op=='+'):
#         return n1+n2
#     elif(op=="-"):     # there is no character concept in python it all string string csn be represet in ''  "" quote
#         return n1-n2
#     elif(op=='*'):
#         return n1*n2
#     elif(op=='/'):
#         return n1/n2
#     else :
#         return "invalid Oprator"
#
#
# n1=int(input("enter the number "))
# op=input("enter the oprator ")
# n2=int(input("enter the number "))

# print(calculator(n1,n2,op))


#dicsionry

#it is in the form of key value pair

# Student={
#     1:"omkar",
#     2:"pooja",
#     3:"poonam",
#     4:"joy",
#     5:"john",
#     6:"sudhant",
#     7:70,
#     8:15.25,
#     9:'+',
#     10:True,
#
# }
# Student[10]=False
# print(Student)
# print(Student[1])
# #print(Student[11]) # we get error here
# print(Student.get(11,"this key in not present in dic")) # if 11 key is not preasent than it return second paremter in the get fun
# a=Student.get(12)  # we get None here
# print(a) #print None
#
# if(a==None):
#     print("key in not in Dicsionery")


# while loop
# i=1
# while (i<=10):
#     print(i)
#     #i=i+1
#     i+=1
# print(str(i)+" outside of the loop ")

# word guess game using while loop
# word="omkar"
# guess=""
# num_of_guess=0
# total_guess=3
# is_out_of_guess=False
#
# while (word!=guess and not(is_out_of_guess) ):
#     if(num_of_guess<total_guess):
#         guess = input("enter the word ")
#         num_of_guess += 1
#     else:
#         is_out_of_guess=True
#         #break
#
# if is_out_of_guess:
#     print("you loss the game")
# else:
#     print("You win")
#

# for loop
# list1=[1,2,3,4,5,6,7,8,9,10]
# for x in list1:
#     print(x,end=" ") # end="" this argument help to new print statement done not start with new line
# # if we write something in end="hii" it can be print after the element in print() method is printed
#
# print()
# # in range if we secified only one parameter than it treate it as a stoping condition
# #with default start value =0 and increment  value by 1 and stoping condition is like
# # <paramter
# # in the down case len of list is 10 but for loop run from 0->9
# for i in range(len(list1)):
#     print(list1[i],end=" ")
# else:
#     print()
# # this else statement is exicuted when for loop end this else can work without if condition
#
# print("abscbjhas")
#
# #in range if two parameter is present than ( start_vaue ,ending_value) but end at ending-1
# for i in range(0,len(list1)):
#     print(list1[i],end=" , ")
# else:
#     print()
#
#
# #in range if three parameter is present than ( start_vaue ,ending_value,increment) but end at ending-1
# for i in range(0,len(list1),3):
#     print(list1[i],end=" , ")
# else:
#     print()


# creating power function
# def power(a,n):
#     ans=1
#     for i in range(0,n,1):
#         ans*=a
#     return ans
#
# def optimized_power(a,n):
#     ans=1
#     ct=0
#     while(n>0):
#        ct+=1
#        if(n%2==1):
#            ans=(ans*a)
#            n-=1
#        else :
#            a=(a*a)
#            n/=2
#     print(ct)
#     return ans
#
#
# print(power(2,100))
# print(optimized_power(2,100))

#print(2**6) # ** can act as power ^ oprator 2^6 =~ 2**6

# dic={
#     1:1,
#     2:4,
#     3:9,
#     4:16,
#     5:25,
# }
# print(dic)
# for i in range (6,11):
#     dic[i]=i*i
#
# print(dic)

#creating a 2D list and travers it with the help of nested for loop

# L1=[]
# n=5
# for i in range(1,n+1):
#     L2=[]
#     for j in range((i-1)*n+1,i*5+1):
#         L2.append(j)
#     L1.append(L2)
#
# for row in L1:
#     for ele in row:
#         print(ele,end=" ")
#     print()
#
# print("--------------------------------------------")
#
# for i in range(5):
#     for j in range(5):
#         print(L1[i][j],end=" ")
#     print()

# create a translater in which vowels convert into '#'
# str="omkar prakash musale"
# new_str=""
# def is_vowel(char):
#     vowel=['a','e','i','o','u']
#     for i in range(len(vowel)):
#         if(char==vowel[i]):
#             return True
#     return False
#
# for char in str:
#     if(is_vowel(char)):
#         new_str+='#'     # string are unmutable here new string is created
#     else:
#         new_str+=char
# print(new_str)

'''
this is used for multipal line of comment
ksjacvad
scnkhavcn
asbchjanas
'''

# try except block to find error
# if we dose not specified error with except than it catches all type of error

# try:
#     a=10/0
# except:
#     print("error is occer ")
#
# try:
#     a = int(input("enter the number "))
#     b = int(input("enter the number "))
#     c = a / b
#     print(c)
# except ZeroDivisionError as err: # here we can get mesegge in the error
#     print(err)
# except ValueError:
#     print("invalid input is take")
#

#reading from the file

# open() method is used to open the file it take 1st argument as file_path ,2nd is mode in which file open

# def string_con(str):
#     '''
#     new_str=""
#     for i in range(len(str)-1):
#         new_str+=str[i]
#     return new_str
#     '''
#     list1=list(str);
#     list2=list1[:len(str)-1] #len1-1 because of last character of line may be '\n'
#     return ''.join(list2)


# f1=open("salary.txt",'r') #type of mode r->read , r+ ->read+write , a -> append , w->write x->create file
# if(f1.readable()):
#     print("file is sucseesfully open ")
#     # print(f1.read())
#     # print(f1.readline()) # after this line exicution read_head go to next line
#     # print(f1.readline())
#     # List11=f1.readlines() # this line return array contaion each line in file
#     # print(List11)
#     # print(List11[0])
#     # for line in List11:
#     #     print(line,end="")


#     for line in f1.readlines():
#         line=string_con(line) #this line string contain new line character at the end of string (\n)
#         print(line,end="")

# else:
#     print("file is not in read mode ")

# f1.close()

# for creating new file and write into it
# you can create any type of file  like html file open("abc.html",'w')
# f2=open("timepass.txt",'w') # only write,append mode can create new file
# print(f2.writable())
# # write method overide the the content of file if file is already present
# str=input("enter some text ")
# f2.write(str+"\n")
# str=input("enter some text ")
# f2.write(str+'\n')
#
# f2.close()


# appending to exiting file
# f3=open("salary.txt",'a')
# if(f3.writable()):
#     print("text can be append ")
#     f3.write("\n joy - 15001")
# f3.close()
#


# module and pip
# pip is pakage maneger (which can maneages ,install python module )
# module is a python file with contain function ,class ,variable which acn be  used for easy programing

# # import Module_name # if we want to used functon inside of that than use Module_name.fun()
# to avoid this lengthy code we can you in follwing way
# from firstModule import power_op
# from firstModule import *
# print(power_op(2,8))

#
# import firstModule
# print(firstModule.power_op(2,8))

# a=10
# print(a)
# a="abc"
# print(a)
# a=12.56
# print(a)

# class
# class Student:
#
#     def __init__(self,name,age,mark,is_pass): # this is like a constructor
#         self.Name=name
#         self.Age=age
#         self.Mark=mark
#         self.Is_pass=is_pass
#         self.Dep="IT"
#
#     def printing(self):  # this is object function   we can take any name other than self as first argument in class fun
#         print(self.Name)
#         print(self.Age)
#         print(self.Mark)
#         print(self.Is_pass)
#         print(self.Dep)
#
#     def fun(self):
#         if(self.Mark>=75):
#             return True
#         else:
#             return False
#
#
# std1=Student("omkar",20,96,True)
# std1.printing()
# print(std1.fun())
# # print(std1.Name)
# # print(std1.Mark)
# # print(std1.Dep)
#

# from chefClass import Chef
#
# class Chinese_chef(Chef):  # this way we inherited class
#
#     def make_chiken(self): # function overiding
#         print("chef can make orange chicken ")
#
#     def make_pasta(self):
#         print("chef can make very good pasta ")
#
#
# chef=Chef()
# chinese_chef=Chinese_chef()
# print(chef.make_chiken())
# print(chinese_chef.make_chiken())
# print(chinese_chef.make_pasta())
#


class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def output(self):
        print(self.fname,self.lname)



class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname) # when we used super method there is dont need of self parametr
        self.year=year
        # Person.__init__(self,fname,lname)

    def out(self):
        return 1


std=Student("omkar","musale",20)

std.output()



for i in range (10):
    print(i,end=" , ");