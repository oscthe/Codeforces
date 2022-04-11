import sys
def get_string(): return sys.stdin.readline().strip()
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

N = int(input())
setN = {int(x): str(N).count(x) for x in set(str(N)) if x in ("4", "7")}
if sum(setN.values()) == 7 or sum(setN.values()) == 4:
    print("YES")
else:
    print("NO") 