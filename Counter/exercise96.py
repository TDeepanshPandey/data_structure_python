from collections import Counter


group_1 = (1, 2, 0, 3, 2, 1, 0, 0, 3, 2, 2, 1)
group_2 = (2, 2, 1, 4, 2, 0, 0, 1, 2, 2, 1, 2, 3, 2, 0, 1)

cnt = Counter(group_1 + group_2)

print(cnt)