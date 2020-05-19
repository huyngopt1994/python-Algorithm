class Solution:
    def twoSum(self, nums, target: int):
        built_map = {}
        for index, num in enumerate(nums):
            if built_map.get(target - num) is not None:
                return [built_map[target - num], index]
            built_map[num] = index


sol = Solution().twoSum([2, 7, 11, 15], 9)
print(sol)
