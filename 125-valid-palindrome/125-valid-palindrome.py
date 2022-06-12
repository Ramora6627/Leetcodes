class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for char in s:
            if not char.isalnum(): 
                s = s.replace(char,'') 
        
        return s == s[::-1]
        
        