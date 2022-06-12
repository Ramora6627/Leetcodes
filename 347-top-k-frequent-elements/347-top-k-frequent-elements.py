class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = {}
        output = []
        for num in set(nums):
            if num not in hashtable:
                hashtable[num] = nums.count(num)
        # print (hashtable)
        c = hashtable.copy()
        # print(c)
        while hashtable:
            for key,val in c.items():
                if not hashtable.values():
                    break
                # print(key,val)
                # print(max(hashtable.values()))
                # print(hashtable.values())
                if val == max(hashtable.values()):
                    output.append(key)
                    del hashtable[key]
                    # print(hashtable)
        # print(output)
        return output[:k]
                
        