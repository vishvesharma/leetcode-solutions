class Solution:
    def totalNQueens(self, n: int) -> int:

        board = [-1] * n
        count = 0

        def solve(row):

            nonlocal count

            if row == n:
                count += 1
                return

            for col in range(n):

                safe = True

                for prev in range(row):

                    if board[prev] == col:
                        safe = False

                    if abs(board[prev] - col) == abs(prev - row):
                        safe = False

                if safe:
                    board[row] = col
                    solve(row + 1)
                    board[row] = -1

        solve(0)

        return count