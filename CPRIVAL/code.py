"""
https://www.codechef.com/problems/CPRIVAL
"""

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(os.path.join(script_dir, "input.txt"), "r")
sys.stdout = open(os.path.join(script_dir, "output.txt"), "w")

r1, r2 = map(int, input().split())
d1, d2 = map(int, input().split())

if ((d1+r1)>(d2+r2)):
    print("dominator")
else:
    print("everule")