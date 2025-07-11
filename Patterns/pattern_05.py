"""
Link: https://www.naukri.com/code360/problems/seeding_6581892

Sam is planting trees on the upper half region (separated by the left diagonal) of the square shared field.

For every value of ‘N’, print the field if the trees are represented by ‘*’.

Example:
Input: ‘N’ = 3

Output:
* * *
* *
*

Constraints :
1  <= N <= 25
Time Limit: 1 sec
"""


def seeding(n: int) -> None:
    for i in range(n, 0, -1):
        if i == 1:
            print("*")
        else:
            print(("* " * i).rstrip())


if __name__ == "__main__":
    n = int(input("Enter the value of N (1 <= N <= 25): "))
    if 1 <= n <= 25:
        seeding(n)

    else:
        print("N must be between 1 and 25 inclusive.")
