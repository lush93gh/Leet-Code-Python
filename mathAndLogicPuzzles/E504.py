class E504:
    def convertToBase7(self, num: int) -> str:
        sign = '' if num >= 0 else '-'
        num = abs(num)
        result = f'{num%7}'
        num = num // 7
        while num > 0:
            result = f'{num % 7}{result}'
            num = num // 7

        return sign + result

a= E504()
print(a.convertToBase7(100))
print(a.convertToBase7(-7))
print(a.convertToBase7(0))