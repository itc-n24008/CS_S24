a = {x for x in 'abcabcabc' if x not in 'ab'}
b = {y for y in 'abcabcabc' if y not in 'bc'}
print(a | b)

#① {'a', 'c'}である
