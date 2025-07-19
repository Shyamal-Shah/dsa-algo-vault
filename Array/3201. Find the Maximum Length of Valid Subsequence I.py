from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ans = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                parity = (nums[i] + nums[j]) % 2
                ans.append(2)
                skip = 1
                for k in range(j + 1, len(nums)):
                    if (nums[k - skip] + nums[k]) % 2 == parity:
                        ans[-1] += 1
                        skip = 1
                    else:
                        skip += 1

        return max(ans)

    def maximumLengthV2(self, nums: List[int]) -> int:
        if nums[0] % 2 == 0:
            even_count = 1
            odd_count = 0
        else:
            odd_count = 1
            even_count = 0
        alternate_count = 1
        for i in range(1, len(nums)):
            if (nums[i - 1] + nums[i]) % 2 == 1:
                alternate_count += 1
            if nums[i] % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        return max([even_count, odd_count, alternate_count])


if __name__ == "__main__":
    print(Solution().maximumLengthV2([1, 2, 3, 4]))
    print(Solution().maximumLengthV2([1, 2, 1, 1, 2, 1, 2]))  # 1,2,1,2,1,2
    print(Solution().maximumLengthV2([1, 3, 3, 1, 2, 1, 1, 2, 1, 2]))
    print(Solution().maximumLengthV2([1, 5, 9, 4, 2]))
    print(Solution().maximumLengthV2([2, 13, 26, 70, 76]))
