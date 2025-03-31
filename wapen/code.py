"""
https://www.codechef.com/problems/WAPEN
"""

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(os.path.join(script_dir, "input.txt"), "r")
sys.stdout = open(os.path.join(script_dir, "output.txt"), "w")


x, y = map(int, input().split())
result = x + (y * 10)
print(result)