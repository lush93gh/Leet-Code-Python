class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        for index in range(len(goal)):
            if(goal[index] == s[0]):
                j = index
                hasFaild = False
                for c in s:
                    if c != goal[j]:
                        hasFaild = True
                        break
                    j = (j + 1) % len(goal)
                if not hasFaild:
                    return True
        return False