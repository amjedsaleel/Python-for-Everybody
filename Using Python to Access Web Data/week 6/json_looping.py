import json

data = '''[
    {
        "id": "001",
        "x": "7",
        "name": "chunck"
    },
    {
        "id": "002",
        "x": "2",
        "name": "danwnd"
    } 
  
]'''

info = json.loads(data)
print('User count:', len(info))

count = 0
for user in info:
    count += 1
    print("id:", user['id'])
    print("x:", user['x'])
    print("Name:", user['name'])
    if count < len(info):
        print('\n')


