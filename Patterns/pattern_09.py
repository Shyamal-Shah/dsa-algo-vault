"""
Link: https://www.naukri.com/code360/problems/star-diamond_6573686

Problem statement
Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Diamond.

Example:
Input: ‘N’ = 3

Output:

  *
 ***
*****
*****
 ***
  *

Constraints:
1  <= N <= 20
Time Limit: 1 sec
"""


def nStarDiamond(n: int) -> None:
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))


if __name__ == "__main__":
    n = int(input("Enter the value of N (1 <= N <= 20): "))
    if 1 <= n <= 25:
        nStarDiamond(n)
    else:
        print("N must be between 1 and 20 inclusive.")
