"""
1266. Minimum Time Visiting All Points

On a plane there are n points with integer coordinates points[i] = [xi, yi].
Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit
vertically and one unit horizontally in one second).

You have to visit the points in the same order as they appear in the array.

Example 1:
    Input: points = [[1,1],[3,4],[-1,0]]
    Output: 7
    Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]
    Time from [1,1] to [3,4] = 3 seconds
    Time from [3,4] to [-1,0] = 4 seconds
    Total time = 7 seconds

Example 2:

    Input: points = [[3,2],[-2,2]]
    Output: 5


Constraints:

    points.length == n
    1 <= n <= 100
    points[i].length == 2
    -1000 <= points[i][0], points[i][1] <= 1000



# 暴力方法

# 同X轴
    src=(1, 2), dst=(1, 3)
    * 如果目的Y轴比来源Y轴大，将来源Y轴加1，直到到达目的地
    * 如果目的Y轴比来源Y轴小，将来源Y轴减1，直到到达目的地

    src=(1, 3) <= Arrived!

# 同Y轴
    src=(5, 2), dst=(1, 2)
    * 如果目的X轴比来源X轴大，将来源X轴加1，直到到达目的地
    * 如果目的X轴比来源X轴小，将来源X轴减1，直到到达目的地

    src=(4, 2)
    src=(3, 2)
    src=(2, 2)
    src=(1, 2) <= Arrived!

# 不同X轴，不同Y轴
    src=(1,1), dst=(3,4)
    * 走对角线
        * 右上角：src_x > dst_x && src_y > dst_y => src=(src_x + 1, src_y + 1)
        * 右下角：src_x > dst_x && src_y > dst_y => src=(src_x - 1, src_y - 1)
        * 左上角：src_x < dst_x && src_y > dst_y => src=(src_x + 1, src_y - 1)
        * 左下角：src_x > dst_x && src_y < dst_y => src=(src_x - 1, src_y + 1)


    src=(2,2)
    src=(3,3)
    src=(3,4) <= Arrived!

"""


class Solution(object):
    @staticmethod
    def move_to_the_next_coordinates(src_x, src_y, dst_x, dst_y):
        x = src_x
        y = src_y

        if src_x > dst_x:
            x -= 1

        if src_x < dst_x:
            x += 1

        if src_y < dst_y:
            y += 1

        if src_y > dst_y:
            y -= 1

        return x, y

    def minTimeToVisitAllPoints(self, points):
        """
        :type points: list[list[int]]
        :rtype: int
        """
        result = 0
        x, y = points.pop(0)
        while points:
            dst_x, dst_y = points.pop(0)

            while True:
                x, y = Solution.move_to_the_next_coordinates(x, y, dst_x, dst_y)

                result += 1
                if x == dst_x and y == dst_y:
                    break

        return result

    def solution2(self, points):
        result = 0

        for i in range(len(points) - 1):
            x, y = points[i]
            dx, dy = points[i+1]

            result += max(abs(dx - x), abs(dy - y))

        return result


if __name__ == '__main__':
    print(Solution().minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]))
    print(Solution().minTimeToVisitAllPoints([[3, 2], [-2, 2]]))
    print(Solution().solution2([[1, 1], [3, 4], [-1, 0]]))
    print(Solution().solution2([[3, 2], [-2, 2]]))
    # print(Solution.get_next_coordinate(1, 2, 1, 3))
