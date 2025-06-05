from typing import List
import queue

class E733:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_color = image[sr][sc]
        if starting_color != color:
            self.dfs(image, sr, sc, starting_color, color)
        return image
    
    def dfs(self, image: List[List[int]], sr: int, sc: int, starting_color: int, target_color: int): 
        image[sr][sc] = target_color
        up = sr - 1
        down = sr + 1
        left = sc - 1
        right = sc + 1
        if up in range(len(image)) and sc in range(len(image[0])) and image[up][sc] == starting_color:
            self.dfs(image, up, sc, starting_color, target_color)
        if down in range(len(image)) and sc in range(len(image[0])) and image[down][sc] == starting_color:
            self.dfs(image, down, sc, starting_color, target_color)
        if left in range(len(image[0])) and image[sr][left] == starting_color:
            self.dfs(image, sr, left, starting_color, target_color)
        if right in range(len(image[0])) and image[sr][right] == starting_color:
            self.dfs(image, sr, right, starting_color, target_color)

    def floodFillBFS(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_pixel = image[sr][sc]
        q = queue.Queue()
        visited = set()
        q.put((sr, sc))
        visited.add((sr, sc))

        while not q.empty():
            y, x = q.get()
            image[y][x] = color
            up = y - 1
            down = y + 1
            left = x - 1
            right = x + 1
            if  up>=0 and image[up][x] == starting_pixel and (up, x) not in visited:
                visited.add((up, x))
                q.put((up, x))
            if (
                down < len(image)
                and image[down][x] == starting_pixel
                and (down, x) not in visited
            ):
                visited.add((down, x))
                q.put((down, x))
            if (
                left >= 0
                and image[y][left] == starting_pixel
                and (y, left) not in visited
            ):
                visited.add((y, left))
                q.put((y, left))
            if  right < len(image[0]) and image[y][right] == starting_pixel and (y, right) not in visited:
                visited.add((y, right))
                q.put((y, right))
        
        return image

    def floodFillLegacy(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
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
    

a = E733()
print(a.floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2)) # [[2,2,2],[2,2,0],[2,0,1]]
print(
    a.floodFill(image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0)
)  # [[0,0,0],[0,0,0]]
