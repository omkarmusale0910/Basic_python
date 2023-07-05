import os

# print(os.getcwd())

# change directory
# os.chdir('../')
# print(os.getcwd())

# path=os.getcwd()
# print("path")
# print(path)
# try:
#    new_dir='subprocess_module.py'
#    new_dir=os.path.join(path,new_dir)
#    os.mkdir(new_dir)
#    os.makedirs(os.path.join(new_dir,'timepass')) #makedir used for makeing nexted directory abc/xyz while mkdir only make one level down directory abc
# except FileExistsError as er:
#    print(er)


# list down the directory

# list_dir=os.listdir(os.getcwd())
# print(list_dir)

# os.chdir('./subprocess_module.py/')
# list_dir=os.listdir(os.getcwd())
# print(list_dir)

# os.rmdir('./subprocess_module.py/timepass/')
# it delete dir when dir is empty else it raise Oserror and 
# os.remove(path) this method used for remove file from the directory

print(os.name)