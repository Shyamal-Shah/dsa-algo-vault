"""
Link: https://www.naukri.com/code360/problems/symmetric-void_6581919

Problem statement
Sam is curious about symmetric patterns, so he decided to create one.

For every value of ‘N’, return the symmetry as shown in the example.

Example:
Input: ‘N’ = 3

Output:
* * * * * *
* *     * *
*         *
*         *
* *     * *
* * * * * *

Constraints:
1  <= N <= 25
Time Limit: 1 sec
"""


def symmetry(n: int) -> None:
    for i in range(n):
        print("* " * (n - i) + "  " * (i * 2) + "* " * (n - i))
    for i in range(n - 1, -1, -1):
        print("* " * (n - i) + "  " * (i * 2) + "* " * (n - i))


if __name__ == "__main__":
    n = int(input("Enter the value of N (1 <= N <= 25): "))
    if 1 <= n <= 25:
        symmetry(n)
    else:
        print("N must be between 1 and 25 inclusive.")
