class Solution:
    def countDigits(self, num: int) -> int:
        x, count = num, 0
        while x > 0:
            r = x % 10
            if r != 0 and num % r  == 0:
                count += 1
            x //= 10
        return count


if __name__ == "__main__":
    print(Solution().countDigits(7))
    print(Solution().countDigits(121))
    print(Solution().countDigits(660))
