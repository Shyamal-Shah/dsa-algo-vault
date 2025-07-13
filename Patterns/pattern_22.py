"""
Link: https://www.naukri.com/code360/problems/ninja-and-the-number-pattern-i_6581959

Problem statement
Ninja has been given a task to print the required pattern and he asked for your help with the same.

You must print a matrix corresponding to the given number pattern.

Example:
Input: ‘N’ = 4

Output:

4444444
4333334
4322234
4321234
4322234
4333334
4444444

Constraints:
1  <= N <= 10^2
Time Limit: 1 sec
"""


def getNumberPattern(n: int) -> None:
    for i in range(n, 0, -1):
        pattern = []
        for j in range(n, 0, -1):
            pattern.append(str(max(i, j)))
        print("".join(pattern) + "".join(pattern[-2::-1]))
    for i in range(2, n + 1):
        pattern = []
        for j in range(n, 0, -1):
            pattern.append(str(max(i, j)))
        print("".join(pattern) + "".join(pattern[-2::-1]))


if __name__ == "__main__":
    n = int(input("Enter the value of N (1 <= N <= 10^2): "))
    if 1 <= n <= 36:
        getNumberPattern(n)
    else:
        print("N must be between 1 and 10^2 inclusive.")
