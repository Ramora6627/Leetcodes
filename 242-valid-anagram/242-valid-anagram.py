class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashtable = {}
        
        for letter in set(s):
            hashtable[letter] = s.count(letter)
        new = ""
        for st in t:
            if st not in hashtable:
                return False
            elif st in hashtable and hashtable[st] != 0:
                new += st
                hashtable[st] -= 1
        return len(new) == len(s)