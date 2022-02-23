import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''
# JSONs are practically a list of dictionaries.

info = json.loads(data)
print('User count:', len(info))  # Literally, a list of dictionaries. One dict per entity (in this case: person)

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

