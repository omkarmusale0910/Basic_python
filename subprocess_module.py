import subprocess

# subprocess.run('ls -la',shell=True)
# shell =True can help you to give whole string as cmd

# subprocess.run(['ls','-la']) 
# if we dont give shell =True than we have to give list to pass for complicated argument

# p1=subprocess.run('ls -la',shell=True)
# print(p1)
# print(p1.args) # it give what we pass cmd to subprocess
# print(p1.returncode) # is it is 0 than cmd run sucessfully


# if we want to capture ouput in console in variable than set capture_output to True in run()

# p1=subprocess.run('ls -la',shell=True,capture_output=True)

# print(p1.stdout)
# p1.stdout this gives a binery string if we want to convert binery to string by decode

# print(p1.stdout.decode())

# if you dont want to decode and want stdout as normal string than pass text=True

# p1=subprocess.run('git status',shell=True,capture_output=True,text=True)

# print(p1.stdout)


'''

import os
import re
from multiprocessing import Process
from pprint import pprint

l_txt=[]
map_using=[file_name for file_name in os.listdir(os.getcwd()) if re.search(r'.txt$',file_name) is not None]

for file_name in os.listdir(os.getcwd()):
    if re.search(r'.txt$',file_name) is not None:
        l_txt.append(file_name)
       

# print(l_txt)
# print(map_using)

combined_file_txt=''

def fun(path):
    sub_pro=subprocess.run(f'cat {path}',shell=True,capture_output=True,text=True)
    return sub_pro.stdout


# for path in l_txt:
#     fun(path=path)

from multiprocessing import Pool

pool =Pool(processes=os.cpu_count())

result= pool.map(fun,l_txt)

print(len(result))
pprint(result)

'''


def git_add_commit_push(msg:str="added os,subprocess,re,gcs module code"):
    git_add=subprocess.run('git add .',shell=True,text=True,capture_output=True)
    if git_add.returncode!=0:
        return Exception("git add . cmd not run")
    else:
        print(git_add.stdout)
    git_commit=subprocess.run(f'git commit -m "{msg}"',shell=True,text=True,capture_output=True)
    if git_commit.returncode!=0:
        return Exception("git commit -m msg cmd not run")
    else:
        print(git_commit.stdout)
    git_push=subprocess.run(f'git push origin master"',shell=True,text=True,capture_output=True)
    if git_push.returncode!=0:
        return Exception("git push origin master cmd not run")
    else:
        print(git_push.stdout)   


try:
    print("come")
    ex=git_add_commit_push("added os,subprocess,re,gcs module script")
    print(ex)
    print("succesful")
except Exception as e:
    print(e)

