"""
https://www.codechef.com/problems/CHEFAPPS
"""

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(os.path.join(script_dir, "input.txt"), "r")
sys.stdout = open(os.path.join(script_dir, "output.txt"), "w")

t = int(input())

for _ in range(t):
    total, app1, app2, app3 = map(int, input().split())
    
    remaining_memory = total - (app1 + app2)
    heavy_app = max(app1, app2)

    if remaining_memory>=app3:
        print(0)
    elif (remaining_memory + heavy_app) >= app3:
        print(1)
    else:
        print(2)
