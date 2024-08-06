# 入れ子のリストデータ
data = [
    ['0001', 'Male', 'Yamada', 'Tarou', '25', 'Tokyo'],
    ['0002', 'Male', 'Satou', 'Takeshi', '27', 'Kanagawa'],
    ['0003', 'Female', 'Tanaka', 'Yuko', '25', 'Saitama'],
    ['0004', 'Male', 'Suzuki', 'Ichirou', '35', 'Hokkaido']
]

# データを格納する辞書
data_dict = {}

# 辞書にデータを格納
for record in data:
    member_id = record[0]
    info = record[1:]
    data_dict[member_id] = info

# 結果を表示
print(data_dict)

# 結果
#{'0001': ['Male', 'Yamada', 'Tarou', '25', 'Tokyo'], 
#'0002': ['Male', 'Satou', 'Takeshi', '27', 'Kanagawa'],
#'0003': ['Female', 'Tanaka', 'Yuko', '25', 'Saitama'],
#'0004': ['Male', 'Suzuki', 'Ichirou', '35', 'Hokkaido']}

