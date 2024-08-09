class E0503:
    def reverseBits(self, num: int) -> int:
        normalizedNum = num
        if num < 0:
            normalizedNum = pow(2, 32) + num
        normalizedNum = bin(normalizedNum).lstrip('0b')
        split = normalizedNum.split("0")
        max = float('-inf')
        for i in range(len(split)):
            length = len(split[i])
            if i+1 < len(split):
                length += len(split[i+1])
            if length > max:
                max = length
        if len(normalizedNum) < 32 or "0" in normalizedNum:
            return int(max + 1)
        else:
            return int(max)
        
a = E0503()
print(a.reverseBits(-1))
print(a.reverseBits(2147483647))