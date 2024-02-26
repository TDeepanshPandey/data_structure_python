from collections import deque


jobs = deque()
jobs.append(('3724', 'chrome.exe'))
jobs.append(('3740', 'pycharm64.exe'))
jobs.appendleft(('17264', 'Calculator.exe'))
jobs.append(('4796', 'postgres.exe'))

while jobs:
    print(jobs.pop())
