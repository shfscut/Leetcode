# @Time: 2019-04-25 19:51
# @Author: 'haifeng.shi@klook.com'

class Solution:
    def isValidList(self, nums):
        temp = [i for i in nums if i != '.']
        if len(temp) == len(set(temp)):
            return True
        return False

    def isValidSudoku(self, board) -> bool:
        for j in range(9):
            row = []
            for i in range(9):
                row.append(board[i][j])
            result = self.isValidList(row)
            if result is True:
                continue
            else:
                return False

        for i in range(9):
            row = []
            for j in range(9):
                row.append(board[i][j])
            result = self.isValidList(row)
            if result is True:
                continue
            else:
                return False

        i = 0
        while i < 9:
            j = 0
            while j < 9:
                t = [(i + 0, j), (i + 0, j + 1), (i + 0, j + 2),
                     (i + 1, j), (i + 1, j + 1), (i + 1, j + 2),
                     (i + 2, j), (i + 2, j + 1), (i + 2, j + 2)]
                result = self.isValidList([board[x][y] for x, y in t])
                if result is True:
                    j += 3
                    continue
                else:
                    return False
            i+=3
        return True

board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))