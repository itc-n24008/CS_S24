class Rectangle:
    '''長方形'''
    angle = 90

    def __init__(self, width, height):
        self.name = 'rectangle'
        self.width = width
        self.height = height
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()

    def calc_perimeter(self):
        w = self.width
        h = self.height
        return (w + h) * 2

    def calc_area(self):
        w = self.width
        h = self.height
        return w * h

    def show_attributes(self):
        ang = self.angle
        n = self.name
        w = self.width
        h = self.height
        p = self.perimeter
        a = self.area
        print("name: {}, width: {}, height: {}, angle: {}".
                format(n, w, h, ang))
        print("perimeter: {}, area: {}".format(p, a))

# Rectangleクラスを継承して正方形クラスを作成
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        self.name = 'square'

    # show_attributes メソッドは親クラスのをそのまま使う

# インスタンスを作って実行
r1 = Rectangle(4, 3)
r1.show_attributes()

s1 = Square(5)
s1.show_attributes()

