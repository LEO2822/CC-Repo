"""
https://www.codechef.com/problems/CHEAPFOOD
"""
import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(os.path.join(script_dir, "input.txt"), "r")
sys.stdout = open(os.path.join(script_dir, "output.txt"), "w")

t = int(input())

for _ in range(t):
    x = int(input())
    percent = 0.1 * x
    flat = 100
    print(int(max(percent, flat)))