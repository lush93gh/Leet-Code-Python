class E0507:
    def exchangeBits(self, num: int) -> int:
        # 將數字轉換為二進制，並去除開頭的 '0b'，然後反轉字串
        original_binary = bin(num).lstrip('0b')[::-1]
        # 將數字右移一位，然後轉換為二進制，去除開頭的 '0b'，並反轉字串
        shifted_binary = bin(num >> 1).lstrip('0b')[::-1]
        # 如果移位後的二進制長度與原始二進制長度不同，則在移位後的二進制尾端加上 '0'
        if len(shifted_binary) != len(original_binary):
            shifted_binary = shifted_binary + '0'
        result = 0
        mul = 1
        # 每兩位進行一次操作
        for i in range(0, len(original_binary), 2):
            # 將移位後的二進制和原始二進制的對應位元相加，然後乘以相應的倍數
            result += (int(shifted_binary[i]) + 2 * int(original_binary[i]))  * mul
            # 更新倍數
            mul *=  4
        
        return result
    
a = E0507()
print(a.exchangeBits(3))
print(a.exchangeBits(6))
print(a.exchangeBits(2))