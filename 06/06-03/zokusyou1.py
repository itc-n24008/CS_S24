#握り寿司のかつおの同じクラスを考えます。握り寿司のかつおは赤身をねたとしているところはマグロと同じですが、生姜とねぎのトッピングが加わります。Nigiriのクラスを継承して、かつおのくらすを作ってください。なお、show_attributes()というメソッドを特性を表示するようにしてください。
#（ヒント）先程定義したNigiriクラスを継承します。toppingという新しい属性を加えて、その値を"生姜ネギ"にします。価格は１００円です。

# 既存のNigiriクラス
class Nigiri:
    def __init__(self, fish_type, price):
        self.fish_type = fish_type
        self.price = price

    def show_attributes(self):
        print(f"魚の種類: {self.fish_type}")
        print(f"価格: {self.price}円")

# かつおの握り寿司のクラス
class KatsuoNigiri(Nigiri):
    def __init__(self):
        super().__init__(fish_type="かつお", price=100)
        self.topping = "生姜ネギ"

    def show_attributes(self):
        super().show_attributes()
        print(f"トッピング: {self.topping}")

# クラスを使ってみましょう
katsuo = KatsuoNigiri()
katsuo.show_attributes()

