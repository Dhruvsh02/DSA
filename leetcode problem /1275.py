from typing import List
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        rows = [0]*3
        cols = [0]*3
        diag = 0
        antidiag = 0

        for i,move in enumerate(moves):
            r,c = move 
            player = 1 if i % 2 == 0 else -1

            rows[r] += player
            cols[c] += player

            if r == c:
                diag += player
            if r+c == 2:
                antidiag += player

            if abs(rows[r]) == 3 or abs(cols[c]) == 3 or abs(diag) == 3 or abs(antidiag) == 3:
                return "A" if player == 1 else "B"

        return "Draw" if len(moves) ==9 else "Pending" 