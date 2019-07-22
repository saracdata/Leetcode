class Solution:
    def judgeCircle(self, moves: str) -> bool:
            R = 1
            L = -1
            U = 1
            D = -1
            x = 0
            y = 0
            
            for letter in moves:
                if letter == 'R' or 'L':
                    x += eval(letter)
                elif letter:
                    y += eval(letter)
                    
            return (x,y) == (0,0)
