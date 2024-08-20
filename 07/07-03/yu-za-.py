color_reference = {1: 'red', 2: 'blue', 3: 'yellow', 4: 'green', 5: 'purple'}

class MyDictKeyError(Exception):
    def __init__(self, key):
        self.key = key
    def __str__(self):
        return '辞書にkeyが登録されていません{0}'.format(self.key)

def get_dict_value(dict_tbl, key):
    if key not in dict_tbl:
        raise MyDictKeyError(key)
    else:
        return dict_tbl[key]

my_dict = {1: 'red', 2: 'blue', 3: 'yellow'}

try:
    my_color = get_dict_value(my_dict, 5)
except MyDictKeyError as err:
    print(err)
    key = err.args[0]
    my_dict[key] = color_reference[key]
    print(key,color_reference[key],'をmy_dictに追加しました')
    my_color = color_reference[key]

print(my_color)
