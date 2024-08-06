#次のような4つの属性を持つ、Personというクラスを作成してください。ただし、生成されるインスタンスは、様々な名前や国籍、生年、住所の場合があり得ることを想定してください。更に、これらの属性をあらをすためのshow_attributes()というメッソドをもたせてください

#名前　国籍　生年　住所
#コーティングの際は、次のような英語名を使ってください
#名前(name)　国籍(nationality)　生年(birtt)　住所(address)

class Person:
    def __init__(self, name, nationality, birth, address):
        self.name = name
        self.nationality = nationality
        self.birth = birth
        self.address = address

    def show_attributes(self):
        print(f"Name: {self.name}")
        print(f"Nationality: {self.nationality}")
        print(f"Birth Year: {self.birth}")
        print(f"Address: {self.address}")

# サンプルインスタンスの作成と属性の表示
person = Person("雪花ラミィ", "ユニーリア", 1810 ,"？？？")
person.show_attributes()

