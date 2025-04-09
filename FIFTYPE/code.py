"""
https://www.codechef.com/problems/FIFTYPE
"""

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(os.path.join(script_dir, "input.txt"), "r")
sys.stdout = open(os.path.join(script_dir, "output.txt"), "w")

t = int(input())

for _ in range(t):
    battery_percentage = int(input())

    no_of_minutes = 0

    def charging(num: int) -> int:
        return num + 2
    
    def uncharged(num: int) -> int:
        return num - 3

    while battery_percentage != 50:
        if battery_percentage < 50:
            battery_percentage = charging(battery_percentage)
            no_of_minutes += 1
        elif battery_percentage > 50:
            battery_percentage = uncharged(battery_percentage)
            no_of_minutes += 1
    
    print(no_of_minutes)
