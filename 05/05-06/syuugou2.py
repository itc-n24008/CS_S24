A = {x for x in range(21)}
B = {y for y in range(21) if y % 2 == 0}

C = A - B 

print(C)

#出力結果{1, 3, 5, 7, 9, 11, 13, 15, 17, 19}である
