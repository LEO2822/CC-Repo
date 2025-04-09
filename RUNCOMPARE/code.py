"""
https://www.codechef.com/problems/RUNCOMPARE
"""

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(os.path.join(script_dir, "input.txt"), "r")
sys.stdout = open(os.path.join(script_dir, "output.txt"), "w")

t = int(input())

for _ in range(t):
    no_of_days = int(input())
    alice = list(map(int, input().split()))
    bob = list(map(int, input().split()))

    happy_days = 0

    for i in range(no_of_days):
        if (alice[i] / bob[i] <= 2) and (bob[i] / alice[i] <= 2):
            happy_days += 1

    print(happy_days)