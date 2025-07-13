"""
Link: https://www.naukri.com/code360/problems/alpha-hill_6581921

Problem statement
Sam is curious about Alpha-Hills, so he decided to create Alpha-Hills of different sizes.

An Alpha-hill is represented by a triangle, where alphabets are filled in palindromic order.

For every value of ‘N’, help sam to return the corresponding Alpha-Hill.

Example:
Input: ‘N’ = 3

Output:
    A
  A B A
A B C B A

Constraints:
1  <= N <= 20
Time Limit: 1 sec
"""


def alphaHill(n: int) -> None:
    for i in range(1, n + 1):
        str = " ".join(chr(65 + j) for j in range(i))
        print(" " * (n - i) * 2 + str + str[-2::-1])


if __name__ == "__main__":
    n = int(input("Enter the value of N (1 <= N <= 20): "))
    if 1 <= n <= 25:
        alphaHill(n)
    else:
        print("N must be between 1 and 20 inclusive.")
