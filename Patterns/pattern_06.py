"""
Link: https://www.naukri.com/code360/problems/reverse-number-triangle_6581889

Aryan and his friends are very fond of the pattern. For a given integer ‘N’, they want to make the Reverse N-Number Triangle.

Example:
Input: ‘N’ = 3

Output:

1 2 3
1 2
1

1  <= N <= 20
Time Limit: 1 sec
"""


def nNumberTriangle(n: int) -> None:
    for i in range(n, 0, -1):
        print(" ".join(str(j) for j in range(1, i + 1)))


if __name__ == "__main__":
    n = int(input("Enter the value of N (1 <= N <= 25): "))
    if 1 <= n <= 25:
        nNumberTriangle(n)

    else:
        print("N must be between 1 and 25 inclusive.")
