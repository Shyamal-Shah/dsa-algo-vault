from typing import List


class Solution:

    def isPrime(self, n: int) -> bool:
        if n < 2:
            return False
        sqrt = int(n**0.5)
        for i in range(2, sqrt + 1):
            if n % i == 0:
                return False
        return True

    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        frequency = dict()
        for i in nums:
            if frequency.get(i):
                frequency[i] += 1
            else:
                frequency[i] = 1
        for value in frequency.values():
            if self.isPrime(value):
                return True
        return False


if __name__ == "__main__":
    print(Solution().checkPrimeFrequency([1, 2, 3, 4, 5]))
    print(Solution().checkPrimeFrequency([1, 2, 3, 4, 5, 4]))
    print(Solution().checkPrimeFrequency([2, 2, 2, 4, 4]))
