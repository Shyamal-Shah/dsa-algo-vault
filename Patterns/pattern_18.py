"""
Link: https://www.naukri.com/code360/problems/alpha-triangle_6581429

Problem statement
Sam is researching on Alpha-Triangles. So, he needs to create them for different integers ‘N’.

An Alpha-Triangle is represented by the triangular pattern of alphabets in reverse order.

For every value of ‘N’, help sam to print the corresponding Alpha-Triangle.

Example:
Input: ‘N’ = 3

Output:
C
C B
C B A

Constraints:
1  <= N <= 20
Time Limit: 1 sec
"""


def alphaTriangle(n: int) -> None:
    for i in range(n, 0, -1):
        print(" ".join(chr(65 + n - 1 - j) for j in range(n - i + 1)))


if __name__ == "__main__":
    n = int(input("Enter the value of N (1 <= N <= 20): "))
    if 1 <= n <= 25:
        alphaTriangle(n)
    else:
        print("N must be between 1 and 20 inclusive.")
