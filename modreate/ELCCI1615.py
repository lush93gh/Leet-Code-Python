from typing import List

class ELCCI1615:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        hit = 0
        psudo_hit = 0
        ball_count = {}
        
        for i in range(len(solution)):
            sol_i = solution[i]
            guess_i = guess[i]
            if sol_i == guess[i]:
                hit += 1
            else:
                if ball_count.get(guess_i, 0) > 0:
                    psudo_hit += 1
                ball_count[guess_i] = ball_count.get(guess_i, 0) - 1
                if ball_count.get(sol_i, 0) < 0:
                    psudo_hit += 1
                ball_count[sol_i] = ball_count.get(sol_i, 0) + 1 

        return [hit, psudo_hit]
    
a = ELCCI1615()
print(a.masterMind(solution="RGBY", guess="GGRR"))
print(a.masterMind(solution="RGRB", guess="BBBY"))
print(a.masterMind(solution="YBBY", guess="GYYB"))