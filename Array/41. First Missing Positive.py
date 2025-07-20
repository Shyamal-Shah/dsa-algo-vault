from typing import List
from collections import Counter


class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        largest = max(nums)
        nums = Counter(nums)
        for i in range(1, largest + 1):
            if i not in nums:
                return i
        return max(largest + 1, 1)

    def firstMissingPositiveV2(self, nums: List[int]) -> int:
        nums = set(nums)
        i = 1
        while i in nums:
            i += 1
        return i


if __name__ == "__main__":
    print(Solution().firstMissingPositiveV2([-5]))
    print(Solution().firstMissingPositiveV2([1, 2, 0]))
    print(Solution().firstMissingPositiveV2([3, 4, -1, 1]))
    print(Solution().firstMissingPositiveV2([7, 8, 9, 11, 12]))
