class E0103:
    def replaceSpaces(self, S: str, length: int) -> str:
        result = ""
        for i in range(length):
            result += "%20" if S[i] == ' ' else S[i]
        return result