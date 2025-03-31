"""
https://www.codechef.com/problems/CHOCDISTRIB
"""

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(os.path.join(script_dir, "input.txt"), "r")
sys.stdout = open(os.path.join(script_dir, "output.txt"), "w")

t = int(input())

for _ in range(t):
    x = int(input())
    min_choco = x - (x//2)
    max_choco = x
    print(min_choco, max_choco)
