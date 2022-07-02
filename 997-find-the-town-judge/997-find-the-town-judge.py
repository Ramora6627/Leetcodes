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
        
        if set.intersection(*candidate.values()):
            common = set.intersection(*candidate.values())
            u = set.union(*candidate.values())
            if len(common)==1 and list(common)[0] not in candidate and len(candidate.keys()) == n-1:
                        return list(common)[0]

        return -1
        