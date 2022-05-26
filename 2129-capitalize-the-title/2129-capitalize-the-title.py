class Solution:
    def capitalizeTitle(self, title: str) -> str:
        m = title.lower()
        n = m.split(" ")
        m = [word.capitalize() if len(word)>2 else word for word in n]
        s = " ".join(m)
        return s