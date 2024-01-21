class E242:
    def isAnagram(self, s: str, t: str) -> bool:
        table = [0] * 26
        for c in s:
            index  = ord(c)-ord('a')
            table[index] += 1

        for c in t:
            index  = ord(c)-ord('a')
            table[index] -= 1

        return not any(table)