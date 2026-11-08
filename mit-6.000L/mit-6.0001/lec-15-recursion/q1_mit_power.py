# Source: MIT 6.0001 Lec 15 | Q1
# Question: Calculate n**p using recursion.
# Approach: Reduce p by 1 in every call, base case p == 0.
# Time Complexity: O(p)
# Status: Solved

def power_recur(n, p):
    if p == 0:
        return 1
    return n * power_recur(n, p - 1)

# print(power_recur(2, 3))