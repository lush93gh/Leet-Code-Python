class E0106:
    def compressString(self, S: str) -> str:
        if len(S) == 0: 
            return S
        result = ""
        prevChar = S[0]
        count = 0
        totalLength = 0
        for char in S:
            if char == prevChar:
                count+=1
            else:
                appendString = "{}{}".format(prevChar, count)
                if totalLength + len(appendString) >= len(S):
                    return S
                result += appendString
                totalLength += len(appendString)
                count = 1
            prevChar = char
        
        if count > 0:
            appendString = "{}{}".format(prevChar, count)
            if totalLength + len(appendString) >= len(S):
                    return S
            result += appendString

        return result
