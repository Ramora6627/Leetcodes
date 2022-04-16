class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i in range(len(nums)):
            if nums[i] == nums[i-1] and type(nums[i]) == int:
                nums.remove(nums[i])
                nums.extend("N") 
                i = i
            else:
                i += 1
        x = {"N"}
        return len(set(nums).difference(x))