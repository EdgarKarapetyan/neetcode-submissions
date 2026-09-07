class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetMap = dict()
        for index, num in enumerate(nums):
            if num in targetMap:
                return [targetMap[num], index]
            targetMap[target - num] = index
        return [-1, -1]
        