# @Time: 2019-04-25 20:08
# @Author: 'haifeng.shi@klook.com'

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_copy=[[i for i in item ] for item in matrix]
        for j, item in enumerate(matrix_copy[::-1]):
            for i, value in enumerate(item):
                matrix[i][j]=value