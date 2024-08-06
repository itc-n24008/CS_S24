# 入れ子のリストデータ
data = [
    ['01', '0001', 'Male', 'Yamada', 'Tarou', '25', 'Tokyo'],
    ['01', '0002', 'Male', 'Satou', 'Takeshi', '27', 'Kanagawa'],
    ['01', '0003', 'Female', 'Tanaka', 'Yuko', '25', 'Saitama'],
    ['02', '0001', 'Male', 'Smith', 'Mike', '22', 'NewJersey'],
    ['02', '0002', 'Male', 'Turner', 'Tom', '27', 'Kansas'],
    ['02', '0003', 'Male', 'Jackson', 'David', '25', 'Florida']
]

# データを格納する辞書
data_dict = {}

# 辞書にデータを格納
for record in data:
    key = (record[0], record[1])  # 国番号と会員番号をタプルとしてキーにする
    info = record[2:]  # 残りの情報を値とする
    data_dict[key] = info

# 結果を表示
for k, v in data_dict.items():
    print(f"{k}: {v}")

# 出力結果
#('01', '0001'): ['Male', 'Yamada', 'Tarou', '25', 'Tokyo']
#('01', '0002'): ['Male', 'Satou', 'Takeshi', '27', 'Kanagawa']
#('01', '0003'): ['Female', 'Tanaka', 'Yuko', '25', 'Saitama']
#('02', '0001'): ['Male', 'Smith', 'Mike', '22', 'NewJersey']
#('02', '0002'): ['Male', 'Turner', 'Tom', '27', 'Kansas']
#('02', '0003'): ['Male', 'Jackson', 'David', '25', 'Florida']

