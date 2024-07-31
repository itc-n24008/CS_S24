#ラムダ式を工夫することで、下記の辞書変数mountain_in_japanを、標高の逆順にソートしてください。

mountain_in_japan = {'fuji': 3776, 'kitadake': 3193, 'okuhodakadake': 3190, 'dummy': 0}

sorted_mountains = sorted(mountain_in_japan.items(), key=lambda x: x[1], reverse=True)

print(sorted_mountains)
#[('fuji', 3776), ('kitadake', 3193), ('okuhodakadake', 3190), ('dummy', 0)]
