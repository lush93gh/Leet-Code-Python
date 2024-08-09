from typing import List

class E1005:
    def findString(self, words: List[str], s: str) -> int:        
        return self.bSearch(words, s, 0 ,len(words) - 1)
    
    def bSearch(self, words: List[str], s: str, low: int, high: int) -> int:
        if low > high:
            return -1
        mid = low + (high - low) // 2
        word = words[mid]
        if word == "":
            left = self.bSearch(words, s, low, mid - 1)
            if left != -1:
                return left
            right = self.bSearch(words, s, mid + 1, high)
            if right != -1:
                return right
            return -1
        elif word < s:
            return self.bSearch(words, s, mid + 1, high)
        elif word > s:
            return self.bSearch(words, s, low, mid -1)
        else:
            return mid
        
    
a = E1005()
print(a.findString(["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], "ball"))
