class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        # i = 0
        # while i in range(len(nums)):
        #     if  sum(nums[i:i+1], total) > sum(nums[i:i+2], total):
        #         i += 1
        #         print ("z", total)
        #     elif sum(nums[i:i+1], total) <= sum(nums[i:i+2], total): 
        #         total = sum(nums[i:i+1], total)
        #         print (total)
        #         i += 1 
        # return total
#         total = nums[0]
        
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 if sum(nums[i:j+1]) > total:
#                     total = sum(nums[i:j+1],total)

#         return total
            
#         total = nums[0]    
#         lst = []        
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 if sum(nums[i:j+1]) >= total:
#                     total = sum(nums[i:j+1])
#                     lst.append(sum(nums[i:j+1]))

#         return max(lst)
          
    
#         total = nums[0]
#         max_end_here = nums[0]
#         for i in range(1,len(nums)):
#             if nums[i] > total and nums[i] + max_end_here < nums[i]:
#                 total = nums[i]
#                 max_end_here = total
#                 print("t",total)
#                 print("z",max_end_here)
#             elif nums[i] > total and nums[i] + max_end_here > nums[i]:
#                 max_end_here = max_end_here + nums[i]
#                 total = max_end_here
#                 print("b",total)
#                 print("f",max_end_here)
#             elif nums[i] < total and nums[i] + max_end_here < total:
#                 max_end_here = max_end_here + nums[i]
#                 print("d",total)
#                 print("e",max_end_here)
#             elif nums[i] < total and nums[i] + max_end_here > total:
#                 max_end_here = max_end_here + nums[i]
#                 total = max_end_here
#                 print("x",total)
#                 print("y",max_end_here)
#         return total
#         best_sum = float('-inf')
#         best_start = best_end = 0  # or: None
#         current_sum = 0
#         for current_end, x in enumerate(nums):
#             if current_sum <= 0:
#                 # Start a new sequence at the current element
#                 current_start = current_end
#                 current_sum = x
#             else:
#                 # Extend the existing sequence with the current element
#                 current_sum += x

#             if current_sum > best_sum:
#                 best_sum = current_sum
#                 best_start = current_start
#                 best_end = current_end + 1  # the +1 is to make 'best_end' match Python's slice convention (endpoint excluded)

#         return best_sum
        max_so_far =nums[0]
        curr_max = nums[0]

        for i in range(1,len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            max_so_far = max(max_so_far,curr_max)

        return max_so_far
 
#         max_so_far = nums[0]
#         max_ending_here = 0

#         for i in range(len(nums)):
#             max_ending_here = max_ending_here + nums[i]
#             print(max_ending_here)
#             if max_ending_here < 0:
#                 max_ending_here = 0

#             # Do not compare for all elements. Compare only  
#             # when  max_ending_here > 0
#             elif (max_so_far <= max_ending_here):
#                 max_so_far = max_ending_here

#         return max_so_far
                    
                
            