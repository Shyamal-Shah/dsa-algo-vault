"""
Link: https://www.naukri.com/code360/problems/increasing-number-triangle_6581893

Problem statement
Aryan and his friends are very fond of patterns. For a given integer ‘N’, they want to make the Increasing Number Triangle.

Example:
Input: ‘N’ = 3

Output:

1
2 3
4 5 6

Constraints:
1  <= N <= 20
Time Limit: 1 sec
"""


def nNumberTriangle(n: int) -> None:
    c = 1
    for i in range(n):
        print(" ".join(str(c + j) for j in range(i + 1)))
        c += i + 1


if __name__ == "__main__":
    n = int(input("Enter the value of N (1 <= N <= 20): "))
    if 1 <= n <= 25:
        nNumberTriangle(n)
    else:
        print("N must be between 1 and 20 inclusive.")
