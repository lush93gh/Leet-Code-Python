from typing import List

class E0306:

    def __init__(self):
        self.anyQueue = []
        self.dogQueue = []
        self.catQueue = []


    def enqueue(self, animal: List[int]) -> None:
        self.anyQueue.append(animal)
        if animal[1] == 0:
            self.catQueue.append(animal)
        elif animal[1] == 1:
            self.dogQueue.append(animal)


    def dequeueAny(self) -> List[int]:
        if self.anyQueue: 
            animal = self.anyQueue[0]
            if animal[1] == 0:
                self.catQueue.remove(animal)
            elif animal[1] == 1:
                self.dogQueue.remove(animal)
            self.anyQueue.remove(animal)
            return animal
        else:
            return [-1, -1]


    def dequeueDog(self) -> List[int]:
        if self.dogQueue: 
            animal = self.dogQueue[0]
            self.anyQueue.remove(animal)
            self.dogQueue.remove(animal)
            return animal
        else:
            return [-1, -1]


    def dequeueCat(self) -> List[int]:
        if self.catQueue: 
            animal = self.catQueue[0]
            self.anyQueue.remove(animal)
            self.catQueue.remove(animal)
            return animal
        else:
            return [-1, -1]