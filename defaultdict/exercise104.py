from collections import defaultdict

comments = defaultdict(list)
print(comments['4052'])
comments['4052'].append('This is interesting')
comments['4052'].append('Great!')
comments['4052'].append('Terrible... :/')
print(comments)
print(comments['4052'])