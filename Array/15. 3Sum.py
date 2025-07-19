from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                if cur_sum == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif cur_sum < 0:
                    j += 1
                else:
                    k -= 1
        return ans


if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    # print(Solution().threeSum([-1, 0, 1, 2]))
    print(
        Solution().threeSum(
            [2, -3, 0, -2, -5, -5, -4, 1, 2, -2, 2, 0, 2, -4, 5, 5, -10]
        )
    )
    print(Solution().threeSum([0, 1, 1]))
    print(Solution().threeSum([0, 0, 0]))
