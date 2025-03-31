"""
https://www.codechef.com/problems/KITCHENCOST
"""

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(os.path.join(script_dir, "input.txt"), "r")
sys.stdout = open(os.path.join(script_dir, "output.txt"), "w")

t = int(input())

for _ in range(t):
    items, min_value = map(int, input().split())
    fresh_value : list = list(map(int, input().split()))
    cost : list = list(map(int, input().split()))

    total_cost = 0

    for i in range(items):
        if fresh_value[i] >= min_value:
            total_cost = total_cost + cost[i]
        
    print(total_cost)