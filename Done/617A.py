import sys
def get_string(): return sys.stdin.readline().strip()
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

x = int(input())
if x < 6:
    print(1)
else:
    steps = 1
    while x > 5:
        x -= 5
        steps += 1
    print(steps)