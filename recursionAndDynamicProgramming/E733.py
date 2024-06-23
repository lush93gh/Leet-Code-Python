from typing import List

class E733:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        queue = []
        root = (sr, sc)
        queue.append(root)
        visited.add(root)
        while len(queue) >0:
            for i in range(len(queue)):
                node = queue.pop()
                neighbors = self.findFlood(image, node[0], node[1], image[node[0]][node[1]])
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                image[node[0]][node[1]] = color
        return image
                
    def findFlood(self, image: List[List[int]], sr: int, sc: int, color: int):
        result = []
        up = sr - 1
        down = sr + 1
        left = sc - 1
        right = sc + 1

        if up >=0 and image[up][sc] == color:
            result.append((up, sc))
        if down< len(image) and image[down][sc] == color:
            result.append((down, sc))
        if left >=0 and image[sr][left] == color:
            result.append((sr, left))
        if right< len(image[0]) and image[sr][right] == color:
            result.append((sr, right))
        
        return result