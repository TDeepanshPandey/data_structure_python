from collections import deque


jobs = deque()

jobs.appendleft(('3724', 'chrome.exe'))
jobs.appendleft(('3740', 'pycharm64.exe'))
jobs.appendleft(('17264', 'Calculator.exe'))
jobs.appendleft(('4796', 'postgres.exe'))
jobs.appendleft(('39628', 'Spotify.exe'))

jobs.rotate(1)
print(jobs)