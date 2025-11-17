class E125:
    def isPalindrome(self, s: str) -> bool:
        processed_string = ""
        for c in s:
            ascii =ord(c)
            if (ascii >= 65 and ascii <=90) or (ascii >= 97 and ascii <= 122) or (ascii >= ord('0') and ascii <= ord('9')):
                processed_string += c
        processed_string = processed_string.lower()
        n= len(processed_string) - 1
        for i in range(len(processed_string)):
            if processed_string[i] != processed_string[n -i]:
                return False
            
        return True
    
a= E125()
print(a.isPalindrome("A man, a plan, a canal: Panama"))
print(a.isPalindrome("race a car"))
print(a.isPalindrome(" "))
print(a.isPalindrome("0P"))
