class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        output = []
        for num in nums:
            indx = abs(num)%len(nums)
            if nums[indx] < 0:
                output.append(abs(num))
            else:
                nums[indx] = - nums[indx]
        
        return output
        