import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        #     return False
        # if x < 10:
        #     return True
        # i = int(math.log10(x))
        # while i > 0:
        #     if x // (10**i) != x % 10:
        #         return False
        #     x %= 10**i
        #     x //= 10
        #     i -= 2
        # return True
        rev, y = 0, x
        if x < 0:
            return False

        while x != 0:
            rev = rev * 10 + x % 10
            x //= 10

        return y != rev


if __name__ == "__main__":
    print(Solution().isPalindrome(1234321))
    print(Solution().isPalindrome(12342321))
    print(Solution().isPalindrome(-121))
    print(Solution().isPalindrome(0))
