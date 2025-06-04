class E405:
    def hexStr(self, num: int) -> str:
        if num < 10:
            return str(num)
        else:
            return chr(num - 10 + ord('a'))
    
    def toHex(self, num: int) -> str:
        base = 2**32
        num = (base + num) % base
        result = self.hexStr(num & 15)
        num = num >> 4
        while num > 0:
            result = f'{self.hexStr(num & 15)}{result}'
            num = num >> 4
        
        return result



print((2**32 - 2**31) % 2**32)
print(ord('a'))
print(-1 & 15)
a = E405()
print(a.toHex(26))
print(a.toHex(-1))