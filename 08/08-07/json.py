import json

name_list = {
    'tanaka':{
        'age':20,
        'bloodtype':'A',
        'gender':'nale'
    },
    'satou':{
        'age':19,
        'bloodtype':'O',
        'gender':'female'
    },
    'suzuki':{
        'age':20,
        'bloodtype':'AB',
        'gender':'male'
    }
}

with open('name_list.json','w') as f1:
    json.dump(name_list,f1)

with open('name_list.json', 'r') as f2:
    name_list_1 = json.load(f2)

for key, val in name_list_1.items():
    print(key, val)
