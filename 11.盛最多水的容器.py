# @Time: 2019-05-28 07:53
# @Author: 'haifeng.shi@klook.com'
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 暴力解法
        # 1s内解决问题，O(n^2)时间复杂度可以大约处理10^4级别的数据

        i, j = 0, 1  # i=[0...length-1), j=[1...length-1]
        max_area = 0
        length = len(height)
        for i, val_i in enumerate(height):
            j = i + 1
            while j < length:
                temp = min(height[i], height[j]) * (j - i)
                if temp > max_area:
                    max_area = temp
                j += 1
        return max_area

"""
最初我们考虑由最外围两条线段构成的区域。现在，为了使面积最大化，我们需要考虑更长的两条线段之间的区域。
如果我们试图将指向较长线段的指针向内侧移动，矩形区域的面积将受限于较短的线段而不会获得任何增加。但是，
在同样的条件下，移动指向较短线段的指针尽管造成了矩形宽度的减小，但却可能会有助于面积的增大。因为移动
较短线段的指针会得到一条相对较长的线段，这可以克服由宽度减小而引起的面积减小。
"""

class Solution1:
    def maxArea(self, height: List[int]) -> int:
        l, r=0, len(height)-1
        max_area=0
        while l<r:
            temp = min(height[l], height[r])*(r-l)
            if max_area<temp:
                max_area=temp
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area



if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea(height))
