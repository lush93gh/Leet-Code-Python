class E1607:
    def maximum(self, a: int, b: int) -> int:
        x = b - a
        return (x + abs(x)) // 2 + a
    
a = E1607()

print(a.maximum(2147483647, -2147483648))
print(a.maximum(-73383683, -2537))