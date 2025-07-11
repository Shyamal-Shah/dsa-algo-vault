"""
Link: https://www.naukri.com/code360/problems/n-triangles_6573689

Sam is making a Triangular painting for a maths project.

An N-dimensional Triangle is represented by the lower triangle of the pattern filled with integers starting from 1.

For every value of ‘N’, help sam to print the corresponding N-dimensional Triangle.

Example:
Input: ‘N’ = 3

Output:
1
1 2
1 2 3

Constraints :
1  <= N <= 25
Time Limit: 1 sec
"""


def nTriangle(n: int) -> None:
    for i in range(n):
        for j in range(i + 1):
            print(j + 1, end=" ")
        print()


if __name__ == "__main__":
    n = int(input("Enter the value of N (1 <= N <= 25): "))
    if 1 <= n <= 25:
        nTriangle(n)
    else:
        print("N must be between 1 and 25 inclusive.")
