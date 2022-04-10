import sys
def get_string(): return sys.stdin.readline().strip()
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

a, b = get_ints()
for _ in range(b):
    if a % 10 == 0:
        a /= 10
    else:
        a -= 1
        
print(int(a))