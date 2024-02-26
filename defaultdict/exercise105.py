from collections import defaultdict


comments = defaultdict(list)

comments['4052'].append('This is interesting')
comments['4052'].append('Great!')
comments['4052'].append('Terrible... :/')

comments['3950'].append('Sounds good')
comments['3950'].append('I have to try this ;)')

print(comments)

print(comments['3950'][1])