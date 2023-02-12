str='''
{
"name":"omkar",
"age":20,
"male":true
}
'''
print(str)

import json
data=json.loads(str)
#loads method is used to convert json string to dicstionay object
print(type(data))
print(data['name'])

