class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        a = set()
        hashtable = {}
        for pair in trust:
            if pair[1] not in hashtable:
                hashtable[pair[1]] = [pair[0]]
            else:
                hashtable[pair[1]].append(pair[0])
            a.add(pair[0])

        print (hashtable,a)
        town = []
        for key,value in hashtable.items():
            if len(value) == n-1 and key not in a:
                town.append(key)
        
        if len(town) == 1:
            return town[0]
        
        return -1