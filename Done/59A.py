import sys
def get_string(): return sys.stdin.readline().strip()
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

word = get_string()
countLower = [x for x in word if x.islower()]
if len(countLower) >= len(word) / 2:
    print(word.lower())
else:
    print(word.upper())