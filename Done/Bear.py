import sys
def get_string(): return sys.stdin.readline().strip()
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

a,b = get_ints()

counter = 0
while not a > b:
    counter += 1
    a *= 3
    b *= 2
    
print(counter)