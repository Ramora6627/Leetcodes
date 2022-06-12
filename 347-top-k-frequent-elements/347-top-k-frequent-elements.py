class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = {}
        output = []
        for num in set(nums):
            if nums.count(num) not in hashtable:
                hashtable[nums.count(num)] = [num]
            else:
                hashtable[nums.count(num)].append(num)
        # print(hashtable)
        v = sorted(hashtable.keys(),reverse=True)
        # print(v)
        i = 0
        while len(output) != k:
            # print(hashtable[v[i]])
            for j in range(len(hashtable[v[i]])):
                output.append(hashtable[v[i]][j])
                # print(output)
            if len(output) == k:
                break
            i += 1
        return output
#         hashtable = {}
#         output = []
#         for num in set(nums):
#             if num not in hashtable:
#                 hashtable[num] = nums.count(num)

#         c = hashtable.copy()

#         while hashtable:
#             for key,val in c.items():
#                 if not hashtable.values():
#                     break

#                 if val == max(hashtable.values()):
#                     output.append(key)
#                     del hashtable[key]


#         return output[:k]
        
        