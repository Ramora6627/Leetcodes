class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i = 1
        # while i in range(len(nums)):
        #     if nums[i] == nums[i-1] and type(nums[i]) == int:
        #         nums.remove(nums[i])
        #         nums.extend("N") 
        #         i = i
        #     else:
        #         i += 1
        # x = {"N"}
        # return len(set(nums).difference(x))
        # S 2
        # lst = []
        # i = 0
        # while i in range(len(nums)):
        #     if nums[i] not in lst:
        #         lst.append(nums[i])
        #         i += 1      
        #     elif nums[i] in lst and type(nums[i]) == int:
        #         nums.remove(nums[i])
        # nums.extend(repeat("x",len(lst)))
        # x = {"x"}
        # return len(set(nums).difference(x))
        # S3
        i = 0
        for idx, num in enumerate(nums):
            if nums[idx] > nums[i]:
                nums[i+1] = nums[idx]
                i += 1
        #
        return i+1