mport sqlite3

db = 'test.db'
con = sqlite3.connect(db)
csr = con.cursor()

csr.execute("update human set nickname = 'Lazer' where name = 'Jiro';")

csr.execute("delete from human where nickname = 'Lazer';")

csr.execute("select *from human;")
priint(csr.fetchall())

con.commit()
con.close()
