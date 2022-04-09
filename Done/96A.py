import sys
from tkinter import Y
def get_string(): return sys.stdin.readline().strip()
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

x = get_string()
y = x.split("0")
z = x.split("1")

ans = False
for i in y:
    if len(i) > 6:
        ans = True
        
for i in z:
    if len(i) > 6:
        ans = True
        
print("YES" if ans else "NO")