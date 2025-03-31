"""
https://www.codechef.com/problems/HWFIN
"""

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(os.path.join(script_dir, "input.txt"), "r")
sys.stdout = open(os.path.join(script_dir, "output.txt"), "w")

already_answered_question, questions_in_each_sheet = map(int, input().split())

total_questions_in_all_sheets =  questions_in_each_sheet * 10
total_answered_questions = already_answered_question + total_questions_in_all_sheets

if total_answered_questions >= 100:
    print("yes")
else:
    print("no")