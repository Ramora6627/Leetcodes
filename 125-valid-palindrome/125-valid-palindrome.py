class Solution:
    def isPalindrome(self, s: str) -> bool:
        # l =''.join( c for c in s if  c not in '?:!/;' )
        s = s.lower()
        for char in s:
            if not char.isalnum(): 
                s = s.replace(char,'') 
        
        return s == s[::-1]
        
        