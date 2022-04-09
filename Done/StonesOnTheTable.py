import sys
def get_string(): return sys.stdin.readline().strip()
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

x = get_ints()
y = get_string()

tmpList = list(y)
counter = 0

for i in range(1,len(tmpList)):
    if tmpList[i-1] == tmpList[i]:
        counter += 1
    else:
        pass

print(counter)