"""
https://www.codechef.com/problems/FOURTICKETS
"""

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(os.path.join(script_dir, "input.txt"), "r")
sys.stdout = open(os.path.join(script_dir, "output.txt"), "w")

t = int(input())

for _ in range(t):
    x = int(input())
    print("yes" if (x*4<=1000) else "no")
