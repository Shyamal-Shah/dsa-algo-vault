"""
Link: https://www.naukri.com/code360/problems/n-forest_6570177

Sam is making a forest visualizer. An N-dimensional forest is represented by the pattern of size NxN filled with ‘*’.

For every value of ‘N’, help sam to print the corresponding N-dimensional forest.

Example:
Input: ‘N’ = 3

Output:
* * *
* * *
* * *

Constraints :
1  <= N <= 25
Time Limit: 1 sec

"""


def nForest(n: int) -> None:
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    n = int(input("Enter the value of N (1 <= N <= 25): "))
    if 1 <= n <= 25:
        nForest(n)
    else:
        print("N must be between 1 and 25 inclusive.")
