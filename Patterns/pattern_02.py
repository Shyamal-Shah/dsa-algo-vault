"""
Link: https://www.naukri.com/code360/problems/n-2-forest_6570178

Sam is making a forest visualizer. An N-dimensional forest is represented by the pattern of size NxN filled with ‘*’.

An N/2-dimensional forest is represented by the lower triangle of the pattern filled with ‘*’.

For every value of ‘N’, help sam to print the corresponding N/2-dimensional forest.

Example:
Input:  ‘N’ = 3

Output:
*
* *
* * *

Constraints :
1  <= N <= 25
Time Limit: 1 sec
"""


def nForest(n: int) -> None:
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    n = int(input("Enter the value of N (1 <= N <= 25): "))
    if 1 <= n <= 25:
        nForest(n)
    else:
        print("N must be between 1 and 25 inclusive.")
