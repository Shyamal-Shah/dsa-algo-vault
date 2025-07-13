"""
Link: https://www.naukri.com/code360/problems/binary-number-triangle_6581890

Problem statement
Aryan and his friends are very fond of the pattern. For a given integer ‘N’, they want to make the N-Binary Number Triangle.

You are required to print the pattern as shown in the examples below.

Example:
Input: ‘N’ = 3

Output:

1
0 1
1 0 1

Constraints:
1  <= N <= 20
Time Limit: 1 sec
"""


def nBinaryTriangle(n: int) -> None:
    for i in range(1, n + 1):
        c = i % 2
        print(" ".join(str((j % 2)) for j in range(c, i + c)))


def nBinaryTriangleV2(n: int) -> None:
    pattern = "01" * n
    for i in range(1, n + 1):
        start = i % 2
        print(pattern[start : start + i])


if __name__ == "__main__":
    n = int(input("Enter the value of N (1 <= N <= 20): "))
    if 1 <= n <= 25:
        nBinaryTriangleV2(n)
    else:
        print("N must be between 1 and 20 inclusive.")
