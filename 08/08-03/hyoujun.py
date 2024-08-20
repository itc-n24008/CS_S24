import collections
data = 'すもももももものうち'
count = collections.Counter(data)
res_dict = collections.defaultdict(list)
for ch, cnt in count.items():
    res_dict[cnt].append(ch)
res_dict[1]
print(data)
