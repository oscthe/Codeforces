import sys
def get_string(): return sys.stdin.readline().strip()
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

x = get_string()
if len(set(x)) % 2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")