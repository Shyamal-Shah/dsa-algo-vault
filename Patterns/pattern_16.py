"""
Link: https://www.naukri.com/code360/problems/alpha-ramp_6581888

Problem statement
Sam is curious about Alpha-Ramp, so he decided to create Alpha-Ramp of different sizes.

An Alpha-Ramp is represented by a triangle, where alphabets are filled from the top in order.

For every value of ‘N’, help sam to return the corresponding Alpha-Ramp.

Example:
Input: ‘N’ = 3

Output:
A
B B
C C C

Constraints:
1  <= N <= 20
Time Limit: 1 sec
"""


def alphaRamp(n: int) -> None:
    for i in range(1, n + 1):
        print(f"{chr(64 + i)} " * i)


if __name__ == "__main__":
    n = int(input("Enter the value of N (1 <= N <= 20): "))
    if 1 <= n <= 25:
        alphaRamp(n)
    else:
        print("N must be between 1 and 20 inclusive.")
