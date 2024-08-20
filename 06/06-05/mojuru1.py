#数字関数my_pow()が含まれる、my_math.pyというモジュールファイルを作成してください。数字関数my_pow()は、引数を2つ受け取り、値を1つに返します。このモジュールファイルをインポートして、引数にx=２とｙ=５を与え、結果が32になることを確認してください

#<ヒント>my_mth.pyの内容は
# def my_pow(x,y):
#   return x ** y

with open("my_math.py","w") as f:
    f.write("""def my_pow(x,y):
    return x ** y\n""")

import my_math
print(my_math.my_pow(2,5))
