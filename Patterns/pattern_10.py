"""
Link: https://www.naukri.com/code360/problems/rotated-triangle_6573688

Problem statement
Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Rotated Triangle.

Example:
Input: ‘N’ = 3

Output:

*
**
***
**
*

Constraints:
1  <= N <= 20
Time Limit: 1 sec
"""


def nStarDiamond(n: int) -> None:
    for i in range(1, 2 * n):
        if i <= n:
            print("*" * i)
        else:
            print("*" * (2 * n - i))


if __name__ == "__main__":
    n = int(input("Enter the value of N (1 <= N <= 20): "))
    if 1 <= n <= 25:
        nStarDiamond(n)
    else:
        print("N must be between 1 and 20 inclusive.")
