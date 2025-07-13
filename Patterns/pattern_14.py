"""
Link: https://www.naukri.com/code360/problems/increasing-letter-triangle_6581897

Problem statement
Aryan and his friends are very fond of patterns. For a given integer ‘N’, they want to make the Increasing Letter Triangle.

Example:
Input: ‘N’ = 3

Output:

A
A B
A B C

Constraints:
1  <= N <= 20
Time Limit: 1 sec
"""


def nLetterTriangle(n: int) -> None:
    for i in range(n):
        print(" ".join(chr(65 + j) for j in range(i + 1)))


if __name__ == "__main__":
    n = int(input("Enter the value of N (1 <= N <= 20): "))
    if 1 <= n <= 25:
        nLetterTriangle(n)
    else:
        print("N must be between 1 and 20 inclusive.")
