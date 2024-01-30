from collections import Counter

class E0104:
    def canPermutePalindrome(self, s: str) -> bool:
        grouped =  list(zip(Counter(s).keys(), Counter(s).values()))
        filtered = list(filter(lambda t: t[1] %2 == 1, grouped))
        return len(filtered) <= 1


a = E0104()
print(a.canPermutePalindrome("aabb"))