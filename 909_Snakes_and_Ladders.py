# n = len(board)
# time: O(n^2)
# space: O(n^2) 

from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()

        def int_to_pos(square): # given square number, return r, c of the square
            square = square -1
            row = square//length
            col = square%length
            if row%2 !=0:
                col = length-1-col
            return [row, col]

        
        q = deque([[1, 0]])#square, moves
        visited =set()
        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                next_square = square+i
                r, c = int_to_pos(next_square)
                if board[r][c]!=-1:
                    next_square = board[r][c]
                if next_square ==length*length:
                    return moves+1
                if next_square not in visited:
                    visited.add(next_square)
                    q.append([next_square, moves+1])
        return -1