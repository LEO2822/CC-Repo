"""
https://www.codechef.com/problems/NEWYEAR
"""

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(os.path.join(script_dir, "input.txt"), "r")
sys.stdout = open(os.path.join(script_dir, "output.txt"), "w")

x = int(input())
print(24-x)