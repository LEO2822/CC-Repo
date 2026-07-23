"""
codeforces
https://codeforces.com/problemset/problem/236/A
"""
import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(script_dir, "input.txt"), "r")
sys.stdout = open(os.path.join(script_dir, "output.txt"), "w")

s = input()
print("CHAT WITH HER!" if len(set(s)) % 2 == 0 else "IGNORE HIM!")