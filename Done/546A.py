import sys
def get_string(): return sys.stdin.readline().strip()
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

k, n, w = get_ints()

tot_cost = sum([i*k for i in range(1,w+1)])
print(tot_cost - n if tot_cost > n else 0)