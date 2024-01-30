class E290:
    def wordPattern(self, pattern: str, s: str) -> bool:
        tokens = s.split(" ")
        if len(tokens) != len(pattern):
            return False
        tokenDict = {}
        patternDict = {}
        for index, token in enumerate(tokens):
            currentPattern = pattern[index]
            tokenMatched = True
            patternMatched = True
            if not currentPattern in tokenDict:
                tokenDict[currentPattern] = token
            else:
                tokenMatched = (tokenDict[currentPattern] == token)
            
            if not token in patternDict:
                patternDict[token] = currentPattern
            else:
                patternMatched = (patternDict[token] == currentPattern)
            
            if not tokenMatched or not patternMatched:
                return False
            
        return True
    
a = E290()
print(a.wordPattern("abba", "dog cat cat dog"))
print(a.wordPattern("abc", "b c a"))