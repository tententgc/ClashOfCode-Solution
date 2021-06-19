import sys
import math

while True:
    opponent_row, opponent_col = [int(i) for i in input().split()]
    valid_action_count = int(input())
    for i in range(valid_action_count):
        row, col = [int(j) for j in input().split()]
    print(row, col)
