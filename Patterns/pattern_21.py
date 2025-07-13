"""
Link: https://www.naukri.com/code360/problems/ninja-and-the-star-pattern-i_6581920

Problem statement
Ninja has been given a task to print the required star pattern and he asked your help for the same.

You must return an ‘N’*’N’ matrix corresponding to the given star pattern.

Example:
Input: ‘N’ = 4

Output:

****
*  *
*  *
****

Constraints:
1  <= N <= 20
Time Limit: 1 sec
"""


def getStarPattern(n: int) -> None:
    for i in range(n):
        if i == 0 or i == n - 1:
            print("*" * n)
        else:
            print("*" + " " * (n - 2) + "*")


if __name__ == "__main__":
    n = int(input("Enter the value of N (1 <= N <= 20): "))
    if 1 <= n <= 25:
        getStarPattern(n)
    else:
        print("N must be between 1 and 20 inclusive.")
