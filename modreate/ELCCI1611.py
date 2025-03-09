from typing import List

class ELCCI1611:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if shorter == longer:
            return [k * shorter]
        result = [k//2 * (shorter + longer)] * (k+1)
        for i in range((k+1)//2):
            result[i] = (k-i) * shorter + i * longer
            result[k-i] = i * shorter + (k - i) * longer
        return result

a = ELCCI1611()
print(a.divingBoard(1, 2, 3))
print(a.divingBoard(1, 1, 0))