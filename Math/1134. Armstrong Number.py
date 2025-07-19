import math


class Solution:
    def isArmstrongNumber(self, num: int) -> bool:
        sum, ori = 0, num
        if num == 0:
            return True
        if num < 0:
            return False
        size = int(math.log10(num)) + 1
        while num > 0:
            sum += (num % 10) ** size
            num //= 10
        return ori == sum


if __name__ == "__main__":
    print(Solution().isArmstrongNumber(1))
    print(Solution().isArmstrongNumber(103))
    print(Solution().isArmstrongNumber(1634))
    print(Solution().isArmstrongNumber(0))
