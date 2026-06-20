"""
codeforces
https://codeforces.com/problemset/problem/71/A
"""

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(os.path.join(script_dir, "input.txt"), "r")
sys.stdout = open(os.path.join(script_dir, "output.txt"), "w")

t = int(input())

for _ in range(t):
    x = input()
    # print(x)

    if len(x) > 10:
        n = str((len(x)-2))
        print(x[0]+n+x[-1])

    else:
        print(x)