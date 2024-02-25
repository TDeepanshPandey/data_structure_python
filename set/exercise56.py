text1 = 'Python'
text2 = 'JavaScript'
text3 = 'Java'

set1 = set(text1.lower())
set2 = set(text2.lower())
set3 = set(text3.lower())

print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))