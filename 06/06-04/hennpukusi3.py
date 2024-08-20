#素数を返すジェネレーター関数を作成してください。素数とは、その数自身以外に約数を持たない自然数のことです。たとえば、最初の１０個の素数は、2､3､5､7､11､13､17､19､23､29です。素数は無限個あることが証明されます。

#（ヒント）定義通りにｘが素数かどうかを愚直に調べていく方法を実装する場合は、次のアルゴリズムを使います。

#① ２からｘ−１までの数字でｘが割り切れるか調べる、このアルゴリズムの実装を言葉で書くと下記になります。

#１，以上の整数ｘを選びます。２，２以上、ｘ−１までの整数についでループを作り、ループの変数をｉとします。３，ｘがｉで割り切れるか調べ、割り切れたら素数ではないのでループをぬけます。４，割り切れなかったら次のｉに１をインクリメントします。５，３〜４の手順を繰り返して、ついにｘ−１がｉでわりきてなかったら、そのｘは素数です。６，ｘをyieldでかえします。７，ｘに１をインクリメントします。８，１〜７の手順を無限に繰り返します。

#更に、ｘが２つ以上の素数を因数にもつ数(合成数)であれば、ｘは√ｘより小さい素数で割り切れることから、次のことが言えます。② ｘが√ｘ以下の数で割り切れなければ、ｘは素数である。平方根の計算をするには、mathモジュールをインポートしてmath.sqrt()を使っています。あるいは、数値ｘの平方根の計算が（ｘ**0.5）であることを使っても良いでしょう。

import math

def is_prime(n):
    """nが素数かどうかを判定する関数"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    sqrt_n = math.isqrt(n)  # math.sqrt(n)を使っても良い
    for i in range(5, sqrt_n + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def prime_generator():
    """無限に素数を生成するジェネレーター関数"""
    x = 2
    while True:
        if is_prime(x):
            yield x
        x += 1

# 最初の10個の素数を表示する
gen = prime_generator()
for _ in range(10):
    print(next(gen))

