class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        if not trust and n != 1:
            return -1
        candidate = {}
        for pair in trust:
            if pair[0] not in candidate:
                candidate[pair[0]] = [pair[1]]
            else:
                candidate[pair[0]].append(pair[1])
        
        for key,value in candidate.items():
            candidate[key] = set(value)
        print (candidate)
        
        if set.intersection(*candidate.values()):
            common = set.intersection(*candidate.values())
            u = set.union(*candidate.values())
            print (common)
            print(u)
            a = list(common)[0]
            print (u.remove(a))
            if len(common)==1 and a not in candidate and len(candidate.keys()) == n-1:
                        return a

        return -1
        