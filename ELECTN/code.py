"""
https://www.codechef.com/problems/ELECTN
"""

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(os.path.join(script_dir, "input.txt"), "r")
sys.stdout = open(os.path.join(script_dir, "output.txt"), "w")

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    all = list(map(int, input().split()))
    count = 0
    for i in range(x):
        if all[i]>= y:
            count += 1
        else:
            pass
    print(count)
