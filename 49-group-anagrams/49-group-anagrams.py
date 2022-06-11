class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        pairs = []
        
        for st in strs:
            k = sorted(st)
            k =  ''.join(k)
            print(k)
            if k in output: 
                
                output[k].append(st)
            else:
                output[k] = [st]
        return output.values()
#         hashtable = {}
#         output = []
#         for st in strs:
            
#             pairs = [st]
#             for word in strs[strs.index(st)+1:]:
                
#                 print(check_anagrams(st,word))
#                 if check_anagrams(st,word)==True:
#                     if not [word,st] in pairs: 
#                         pairs.append(word)
                    
#             print(pairs)
#             output.append(pairs)
#         return output
                    
                    
                
                    

# def check_anagrams(s,t):
#     if len(s) != len(t):
#         return False
#     hashtable = {}

#     for letter in set(s):
#         hashtable[letter] = s.count(letter)
#     new = ""
#     for st in t:
#         if st not in hashtable:
#             return False
#         elif st in hashtable and hashtable[st] != 0:
#             new += st
#             hashtable[st] -= 1
#     return len(new) == len(s)