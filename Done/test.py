import sys
def get_string(): return sys.stdin.readline().strip()
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

tmp = get_string()
print(tmp[0].upper() + tmp[1:])