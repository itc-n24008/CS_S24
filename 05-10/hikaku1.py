#引数xが10以上、20未満であるか否かを判定する関数is_number_of_positions_of_10(x)を、比較演算子の連鎖を使って生成してください。

#<ヒント>引数xが10以上であることの条件と、引数xが20未満であることの条件の論理積を、短絡表現で表現することが必要です。「以上」の比較演算子は「<=」、「未満」の条件式は「<」となります。

def is_number_of_positions_of_10(x):
    return 10 <= x < 20

# テスト
print(is_number_of_positions_of_10(9))   # False
print(is_number_of_positions_of_10(10))  # True
print(is_number_of_positions_of_10(15))  # True
print(is_number_of_positions_of_10(20))  # False
print(is_number_of_positions_of_10(21))  # False

