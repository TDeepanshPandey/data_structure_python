from collections import Counter

def char_dist(a:str):
    temp=Counter(a)
    result = ''
    for char,counter in temp.items():
        result += char + str(counter)
    return result

print(char_dist('python programming'))