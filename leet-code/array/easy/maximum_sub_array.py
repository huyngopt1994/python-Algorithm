from typing import List


class Solution:
    def maxSubArray_without_dividing_and_conquer(self, nums: List[int]) -> int:
        # Create the sum of array
        min_left = 0
        max_sum = float('-inf')
        current_sum = 0
        for num in nums:
            current_sum += num
            current_max = current_sum - min_left
            if current_max > max_sum:
                max_sum = current_max
            if current_sum < min_left:
                min_left = current_sum

        return max_sum
    def max

solution = Solution()
print(solution.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
