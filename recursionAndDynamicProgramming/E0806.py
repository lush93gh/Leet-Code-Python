from typing import List

class E0806:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        self.move_disks(A, B, C, len(A), [1,3])
    
    def move_disks(self, A: List[int], B: List[int], C: List[int], num_disks: int, move_direction: List[int]) -> None:
        # 如果只有一個圓盤，直接移動
        if num_disks == 1:
            self.move(A, B, C, move_direction)
        else:
             # 決定移動的來源和目的地
            source = move_direction[0]
            dest = move_direction[1]

            # 找出未使用的桿子
            rods = [1, 2, 3]
            rods.remove(source)
            rods.remove(dest)
            unused_rod = rods[0]

            # 遞迴地移動圓盤
            self.move_disks(A, B, C, num_disks -1, [source, unused_rod])
            self.move(A, B, C, [source, dest])
            self.move_disks(A, B, C, num_disks -1, [unused_rod, dest])

    def move(self, A: List[int], B: List[int], C: List[int], direction: List[int]) -> None:
        source = direction[0]
        dest = direction[1]
        sourceValue = 0
        if source == 1:
            sourceValue = A.pop()
        elif source == 2:
            sourceValue = B.pop()
        else:
            sourceValue = C.pop()
        
        if dest == 1:
            A.append(sourceValue)
        elif dest == 2:
            B.append(sourceValue)
        else:
            C.append(sourceValue)


a = E0806()
print(a.hanota([2, 1, 0], [], []))
print(a.hanota([1, 0], [], []))