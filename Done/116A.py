import sys
def get_string(): return sys.stdin.readline().strip()
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

passengers = []
currPass = 0
for _ in range(int(input())):
    a, b = get_ints()
    currPass += b - a
    passengers.append(currPass)
    
print(max(passengers))