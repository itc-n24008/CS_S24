import sqlite3

db = 'test.db'
con = sqlite3.connect(db)
csr = con.cursor()

# テーブルを作成（カラムのデータ型を指定）
csr.execute('create table human(name TEXT, nickname TEXT);')

# データを挿入
csr.execute("insert into human(name) values('Ichiro');")
csr.execute("insert into human(name) values('Jiro');")
csr.execute("insert into human(name) values('Saburo');")

# "execute" のタイポを修正し、データを更新
csr.execute("update human set nickname ='Lazer' where name = 'Ichiro';")

# テーブルからデータを取得（コロンをセミコロンに修正）
csr.execute("select * from human;")
print(csr.fetchall())

# 変更をコミットして、接続を閉じる
con.commit()
con.close()

