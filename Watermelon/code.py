"""
codeforces
https://codeforces.com/problemset/problem/4/A
"""

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(os.path.join(script_dir, "input.txt"), "r")
sys.stdout = open(os.path.join(script_dir, "output.txt"), "w")

w = int(input())

if 1 <= w <= 100 and w%2 == 0:
    print("YES")
else:
    print("NO")