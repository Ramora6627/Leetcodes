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
        lst = []
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1] and type(nums[i]) == int:
        #         nums.remove(nums[i])
        #         nums.extend("N") 
        #         i = i
        #     else:
        #         i += 1
        # x = {"N"}
        #         # x = {"N"}
        # return len(set(nums).difference(x))   
        i = 0
        while i in range(len(nums)):
            if nums[i] not in lst:
                lst.append(nums[i])
                i += 1      
            elif nums[i] in lst and type(nums[i]) == int:
                nums.remove(nums[i])
        nums.extend(repeat("x",len(lst)))
        # while i in range(len(nums)):
        #     if nums[i] == nums[i-1] and type(nums[i]) == int:
        #         nums.remove(nums[i])
        #         nums.extend("N") 
        #         i = i
        #     else:
        #         i += 1
        x = {"x"}
        return len(set(nums).difference(x))