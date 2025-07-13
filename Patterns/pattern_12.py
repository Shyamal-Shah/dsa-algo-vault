"""
Link: https://www.naukri.com/code360/problems/number-crown_6581894

Problem statement
Aryan and his friends are very fond of the pattern. They want to make the Reverse N-Number Crown for a given integer' N'.

Given 'N', print the corresponding pattern.

Example:
Input: ‘N’ = 3

Output:

1    1
12  21
123321

Constraints:
1  <= N <= 20
Time Limit: 1 sec
"""


def numberCrown(n: int) -> None:
    for i in range(1, n + 1):       
        print(
            "".join(map(str, range(1, i + 1)))
            + " " * ((n - i) * 2)
            + "".join(map(str, range(i, 0, -1)))
        )


if __name__ == "__main__":
    n = int(input("Enter the value of N (1 <= N <= 20): "))
    if 1 <= n <= 25:
        numberCrown(n)
    else:
        print("N must be between 1 and 20 inclusive.")
