"""
https://www.codechef.com/problems/KTTABLE
"""

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(os.path.join(script_dir, "input.txt"), "r")
sys.stdout = open(os.path.join(script_dir, "output.txt"), "w")

t = int(input())

for _ in range(t):
    no_of_students = int(input())
    scheduled_time = list(map(int, input().split()))
    time_required = list(map(int, input().split()))

    complete_cooking =  0
    for i in range(no_of_students):
        if i != 0 and (scheduled_time[i] - scheduled_time[i-1]) >= time_required[i]:
            complete_cooking += 1
        elif i == 0 and (scheduled_time[i] >= time_required[i]):
            complete_cooking += 1
        else:
            pass
    
    print(complete_cooking)


