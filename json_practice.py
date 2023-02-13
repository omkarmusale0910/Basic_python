# str='''
# {
# "name":"omkar",
# "age":20,
# "male":true
# }
# '''
# print(str)

# import json
# # data=json.loads(str)
# # #loads method is used to convert json string to dicstionay object
# # print(type(data))
# # print(data['name'])
# # # dump convert dic object to json string
# # str1=json.dumps(data,indent=2)
# # print(type(str1))
# # print(str1)
#
# # when we want read from a json file use load methhod
# # before load the json file we need to open it in read mode
# with open('new_states.json','r') as f: # when we used open() syntax alonge with keyword there is no need to colse the file file.close()
#     obj=json.load(f)
#     # print(type(obj))
#     print(obj['states'][0].keys())
#     for ele in obj['states']:
#         ele['age']=20
#         for k,v in ele.items():
#             pass;
#             # print(k)
#     print(obj)
#
#     # print(obj)
#
# # dump(a) method used for write to a json file it take 1 arg as obj(dic) 2 arg is file pointer which open is write mode
# with open('new_states.json','w') as f:
#     json.dump(obj,f,indent=2)



# dic={
#     1:1,
#     2:4,
#     3:9
# }
#
# print(dic.keys())
# print(type(dic))


