"""
Link: https://www.naukri.com/code360/problems/triangle_6573690

Sam is making a Triangular painting for a maths project.

An N-dimensional Triangle is represented by the lower triangle of the pattern filled with integers representing the row number.

For every value of ‘N’, help sam to print the corresponding Triangle.

Example:
Input: ‘N’ = 3

Output:
1
2 2
3 3 3

Constraints :
1  <= N <= 25
Time Limit: 1 sec
"""


def nTriangle(n: int) -> None:
    for i in range(1, n + 1):
        if i == 1:
            print(str(i))
        else:
            print(" ".join([str(i)] * i))


if __name__ == "__main__":
    n = int(input("Enter the value of N (1 <= N <= 25): "))
    if 1 <= n <= 25:
        nTriangle(n)

    else:
        print("N must be between 1 and 25 inclusive.")
