class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        j = 0
        output = []
        while i < len(nums) :
            print (i,j)
            while  j < len(nums)-1 and nums[j+1] == nums[j] + 1 :
                j += 1
                print(j)
            if i == j: 
                output.append(str(nums[i]))
                i += 1
                j += 1
            else:
                st = str(nums[i]) + "->" + str(nums[j])
                output.append(st)
                i = j + 1
                j += 1
        if i < len(nums):
            output.append(str(nums[-1]))
        return output