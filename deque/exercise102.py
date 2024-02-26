from collections import deque


jobs = deque(maxlen=3)

jobs.appendleft(('3724', 'chrome.exe'))
jobs.appendleft(('3740', 'pycharm64.exe'))
jobs.append(('17264', 'Calculator.exe'))
jobs.appendleft(('4796', 'postgres.exe'))
jobs.appendleft(('39628', 'Spotify.exe'))

print(jobs)