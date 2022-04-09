import sys
def get_string(): return sys.stdin.readline().strip()
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

