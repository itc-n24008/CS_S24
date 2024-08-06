#円柱を表すクラスを作成してください。円柱を半径と高さによって特徴づけて、任意の半径と高さを持つ円柱について、表面積と体積を計算してください。

#円周は半径ｒと高さｈを使って特徴づけることができます。これらを使うと、底面の面積ｃは円の面積なので、　ｃ＝πｒ²　と表すことができます。側面の面積は、底面の円周の長さと高さを隣り合う二辺とする長方形の面積ｓと同じになるので、　ｓ＝２πｒｈ　となります。表面積Sは、底面積ｃ２つ分と側面積ｓ一つ分をあわせたものになるので、S＝ｃ２＋ｓ＝２πｒ²＋２πｒｈ＝２πｒ(r＋h)　となります。更に、体積は、底面積ｃと高さｈを掛けたものになるので、　V＝ｃｈ＝πｒ²ｈ　となります。コーティングするときは、次のような名称を使うと良いでしょう。円周率πの値は、3.14としておきます。

#円柱(cylinder)　底面(base)　面積(area)　側面(side)　円周(circumference)　表面積(surface area)　体積(volume)　円周率(pi)

import math

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.pi = 3.14  # または math.pi を使用できます

    def surface_area(self):
        base_area = self.pi * self.radius ** 2
        side_area = 2 * self.pi * self.radius * self.height
        return 2 * base_area + side_area

    def volume(self):
        base_area = self.pi * self.radius ** 2
        return base_area * self.height

# 使用例
radius = 3
height = 5
cylinder = Cylinder(radius, height)

print(f"円柱の表面積: {cylinder.surface_area()} 平方単位")
print(f"円柱の体積: {cylinder.volume()} 立方単位")

