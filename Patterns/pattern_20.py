"""
Link: https://www.naukri.com/code360/problems/symmetry_6581914

Problem statement
Sam is curious about symmetric patterns, so he decided to create one.

For every value of ‘N’, return the symmetry as shown in the example.

Example:
Input: ‘N’ = 3

Output:
*         *
* *     * *
* * * * * *
* *     * *
*         *

Constraints:
1  <= N <= 20
Time Limit: 1 sec
"""


def symmetry(n: int) -> None:
    for i in range(1, 2 * n):
        if i <= n:
            print("* " * i + "  " * 2 * (n - i) + "* " * i)
        else:
            print("* " * (2 * n - i) + "  " * 2 * (i - n) + "* " * (2 * n - i))


if __name__ == "__main__":
    n = int(input("Enter the value of N (1 <= N <= 20): "))
    if 1 <= n <= 25:
        symmetry(n)
    else:
        print("N must be between 1 and 20 inclusive.")
