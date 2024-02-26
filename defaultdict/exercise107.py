from collections import defaultdict


tech_stacks = defaultdict(set)

tech_stacks['4355'].add('python')
tech_stacks['4355'].add('javascript')
tech_stacks['4355'].add('html/css')
tech_stacks['9876'].add('aws')
tech_stacks['9876'].add('gcp')
tech_stacks['9876'].add('python')

print(tech_stacks)