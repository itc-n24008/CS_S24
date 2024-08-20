# 100万行からなるファイルの作成
import random

random.seed(1)
msgs = ["Hi", "Hello", "Good morning", "Good night", "See you later", "How are you", "Have a good day"]
with open("some.txt", "w") as f:
    for i in range(1000000):
        f.write("{}, {}\n".format(i, random.choice(msgs)))

# 最初の3行を表示するプログラム
def display_first_three_lines(file_path):
    with open(file_path, "r") as f:
        for _ in range(3):
            print(next(f), end="")

# some.txt の最初の3行を表示
display_first_three_lines("some.txt")

