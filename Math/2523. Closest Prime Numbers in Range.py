from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ans = [-1, -1]
        primes = [True] * (right + 1)
        primes[0], primes[1] = False, False
        for i in range(2, right + 1):
            if primes[i]:
                for j in range(i * i, right + 1, i):
                    primes[j] = False
        first, sub = -1, 10**6
        for i in range(left, right + 1):
            if primes[i]:
                if first != -1:
                    if i - first < sub:
                        sub = i - first
                        ans = [first, i]
                first = i
        return ans


if __name__ == "__main__":
    print(Solution().closestPrimes(10, 19))
    print(Solution().closestPrimes(4, 6))
