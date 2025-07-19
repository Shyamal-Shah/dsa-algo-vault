from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min, max = 1001, 0
        for i in nums:
            if i > max:
                max = i
            if i < min:
                min = i
        gcd = 1
        max_sqrt = int(max**0.5) + 1
        for i in range(1, max_sqrt):
            factor = max // i
            if i > gcd or factor > gcd:
                if max % i == 0 and min % i == 0:
                    gcd = i
                if max % factor == 0 and min % factor == 0:
                    gcd = factor
        return gcd


if __name__ == "__main__":
    print(Solution().findGCD([10, 20]))
    print(Solution().findGCD([7, 5, 6, 8, 3]))
