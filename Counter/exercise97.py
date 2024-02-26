from collections import Counter


test_results = {
    '230': '3+',
    '435': '2',
    '642': '5',
    '623': '4',
    '662': '3+',
    '762': '3+',
    '723': '4',
    '653': '4+',
    '433': '2',
    '622': '3+',
    '612': '4',
}

grades = Counter(test_results.values())

print(grades)

