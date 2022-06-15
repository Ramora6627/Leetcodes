class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums) and nums[i]< target :
            if nums[i] == target:
                return i
            else:
                temp = i
                i += 1
        return i
        