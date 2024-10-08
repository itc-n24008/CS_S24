#次の文章から、半角英字、ハイフン、数字が組み合わさった単語をすべて抜き出してください。

#かなり昔のRX-7で東京駅まで送ってもらい、成田空港からBoeing787で高松空港めで行き、帰りはN700系で岡山から戻りました。

#<ヒント>reモジュールにはfindallという関数があり、文字列の中から指定された正規表現にマッチする部分をすべて探すことができます

import re

text = "かなり昔のRX-7で東京駅まで送ってもらい、成田空港からBoeing787で高松空港めで行き、帰りはN700系で岡山から戻りました。"

# 正規表現を使用して半角英字、ハイフン、数字が組み合わさった単語をすべて抽出
matches = re.findall(r'[a-zA-Z-]+\d+', text)

print(matches)

