class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # m = len(nums1)
        # n = len(nums2)
        i = m-1
        j = n-1
        k = i+j +1 
        
        nums1[m:] = nums2[:n]
        # print (i,j,k)
        while k >=0:
            # print (i,j,k)
            if i>=0 and j>=0 and nums2[j] <=  nums1[i]:
                nums1[k] = nums1[i]
                # print (nums1)
                i -= 1 
            # elif nums2[j] == nums1[i]:
            #     nums1[k] = nums1[i]
            #     nums1.pop(j+i)
            #     j -= 1
            #     i -= 1 
            #     print (nums1)
            elif j>=0:
                nums1[k] = nums2[j]
                j-=1
                # print (nums1)
            k -= 1
        # print (nums1)
        return nums1
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
#         nums1[m:] = nums2  
#         nums1 = nums1.sort()
        
        # return nums1[len(nums1)-(n+m):]
            # nums1 = nums1[(m-n):] + nums1[:(m-n)]
            # print(nums1)
            # return nums1
        # return nums1

#         nums1[m:] = nums2[:n]
#         print (nums1)
#         while m>1:
#             if nums1[m-1] < nums1[m]:
#                 return nums1
#             elif nums1[m-1] > nums1[m]:
#                 print(nums1[m-1])
#                 nums1.insert(m+n-1,nums1[m-1])
#                 nums1.remove(nums1[m-1])
#                 # nums1[-1] = nums1[m-1]
#                 print (nums1)
#                 m -= 1
#         return nums1

        
