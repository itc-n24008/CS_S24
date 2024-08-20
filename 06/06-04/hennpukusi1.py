#１００万行からなるファイルの最初の３行を表示するプログラムを作成してください。ただし、１００万行からなるファイルは、下記の方法で制作したものを使います。

import random
# 何回実行しても同じ結果になるように乱数の種(seed)を固定する
random.seed(1)
msgs = ["Hi", "Hello", "Good morning", "Good night", "See you later", "How are you", "Have a good day"]
with open("some.txt","w") as f:
    for i in range(1000000):
        f.write("{}, {}\n".format(i, random.choice(msgs)))

#ファイルsome.txtはカンマ区切りの２列からなり、最初の列は番号、次の列はメッセージです。

0, Hello
1, See you later
2, Have a good day

    <中略>

999999, Hi

#（ヒント）下記のようにファイルをすべて読み込んでから処理すると、時間がかかりますので避けてください。Jupyter Notebookを使っている場合は、％％timeを実行するセルの先頭行につけることで、セルの処理時間を計測することができます。

%%time
f - open('some.txt')
body = f.read()
lines = body.split('\n')
print('\m'.join(lines[:3]))

#open()ファイルを開いたときに返されるファイルオブジェクトは、すでに反復子担っています。

f = open('some.txt')
print(next(f), end="")
print(next(f), end="")
f.close()
