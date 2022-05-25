class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        index = [i for i in range(len(s)) if s[i] == goal[0]]
        # print(index)
        new = []
        for i in index:
            new = s[i:] + s[:i]
            # print(new)
            if new == goal:
                return True
        return False