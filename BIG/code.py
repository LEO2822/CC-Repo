"""
https://www.codechef.com/problems/BIG
"""

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(os.path.join(script_dir, "input.txt"), "r")
sys.stdout = open(os.path.join(script_dir, "output.txt"), "w")

t = int(input())

for _ in range(t):
    n = int(input())
    all = [int(i) for i in input().split()]

    result = [1]
    max = all[0]

    for i in range(1, n):
        if all[i]>max:
            result.append(1)
            max = all[i]
        else:
            result.append(0)
    print(" ".join(map(str, result)))
