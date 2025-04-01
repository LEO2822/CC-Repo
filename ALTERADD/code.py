"""
https://www.codechef.com/problems/ALTERADD
"""

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(os.path.join(script_dir, "input.txt"), "r")
sys.stdout = open(os.path.join(script_dir, "output.txt"), "w")

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    difference = b - a
    if (difference % 3 != 2):
        print("yes")
    else:
        print("no")


