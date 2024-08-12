from typing import List

def main():
    t = input()
    for _ in range(int(t)):
        n = input()
        a = [0 for _ in range(int(n))]
        b = [int(b_i) for b_i in input().split(" ")]
        result = reconstruct(a, b)
        print(*result)


def reconstruct(a: List[int], b: List[int]) -> List[int]:
    for i in range(len(a)):
        if i == 0:
            a[i] = b[i]
        elif i == len(a) - 1:
            a[i] = b[-1]
        else:
            a[i] = b[i] | b[i - 1]
        
        if i > 0 and b[i -1] != a[i] & a[i-1]:
            return [-1]

    return a


main()

# print(reconstruct([1]))
# print(reconstruct([2,0]))
# print(reconstruct([1,2,3]))
# print(reconstruct([3,5,4,2]))
