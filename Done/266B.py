import sys
def get_string(): return sys.stdin.readline().strip()
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

n, t = get_ints()
vec = list(get_string())

for x in range(t):
    hasMoved = 0
    for i, char in enumerate(vec):
        if char == "B" and i < len(vec) - 1 and vec[i+1] == "G":
            if hasMoved:
                hasMoved = 0
            else:
                vec[i], vec[i+1] = vec[i+1], vec[i]
                hasMoved = 1
        else:
            hasMoved = 0
        
print("".join(vec))