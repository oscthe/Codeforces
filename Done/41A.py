import sys
def get_string(): return sys.stdin.readline().strip()
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

a = get_string()
b = get_string()
if a == b[-1::-1]:
    print("YES")
else:
    print("NO")