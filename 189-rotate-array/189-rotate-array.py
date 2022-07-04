class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        temp = []
        for i in range(0,len(nums)-k):
            temp.append(nums[i])
        # print(temp)
        for i in range(len(nums)-k,len(nums)):
            # print(i,nums[i])
            nums[(i+k)%len(nums)] = nums[i]
            # print(nums)
        
        nums[k:]=temp[:]