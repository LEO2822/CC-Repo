"""
https://www.codechef.com/problems/RIGHTTHERE
"""

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(os.path.join(script_dir, "input.txt"), "r")
sys.stdout = open(os.path.join(script_dir, "output.txt"), "w")

t = int(input())

for _ in range(t):
    x, n = map(int, input().split())
    if x <= n:
        print("yes")
    else:
        print("no")