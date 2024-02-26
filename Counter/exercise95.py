from collections import Counter

answers = ['A', 'C', 'C', 'B', 'A', 'D', None, 'A', 'C', 'D', 'B', 'A', 'A']

ant = Counter(answers)

print(ant.most_common(1))