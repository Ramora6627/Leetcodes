class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # """
        # Do not return anything, modify nums1 in-place instead.
        # """
        # # solution 1
        # i = 0
        # while i < n and nums1[-1] == 0:
        #     nums1.pop(-1)
        #     i += 1
        # nums1.extend(nums2)
        # nums1.sort()
        
#         solution 2:
        # nums1[:] = sorted(nums1[:m]+nums2[:n])
    
# solution 3:
        nums1[m:] = nums2  
        nums1 = nums1.sort()
        
        # return nums1[len(nums1)-(n+m):]
            # nums1 = nums1[(m-n):] + nums1[:(m-n)]
            # print(nums1)
            # return nums1
        # return nums1
        