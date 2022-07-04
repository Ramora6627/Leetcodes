class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        space = 0
        output = ""
        while space<k:
            for char in s:
                if char == " " and space<k:
                    output += char
                    space += 1
                elif space<k:
                    print (char,space)
                    output += char
            if space==k-1:
                break
        return output.strip()
            