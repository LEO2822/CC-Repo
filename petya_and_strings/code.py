"""
codeforces
https://codeforces.com/problemset/problem/112/A
"""
import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(script_dir, "input.txt"), "r")
sys.stdout = open(os.path.join(script_dir, "output.txt"), "w")

a = input().lower()
b = input().lower()
print((a > b) - (a < b))