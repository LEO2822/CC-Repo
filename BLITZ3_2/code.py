"""
https://www.codechef.com/problems/BLITZ3_2
"""

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(os.path.join(script_dir, "input.txt"), "r")
sys.stdout = open(os.path.join(script_dir, "output.txt"), "w")

t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())

    total_time = 2 * (180 + n) - (a + b)
    print(total_time)