from collections import defaultdict


levels = defaultdict(int)

print(levels)
print(levels['4323'])
levels['4323'] = 80
levels['2340'] = 54
print(levels)
