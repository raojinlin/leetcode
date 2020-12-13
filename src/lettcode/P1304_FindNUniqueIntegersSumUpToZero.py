"""
1304. Find N Unique Integers Sum up to Zero

Given an integer n, return any array containing n unique integers such that they add up to 0.



Example 1:
    Input: n = 5
    Output: [-7,-1,1,3,4]
    Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

Example 2:
    Input: n = 3
    Output: [-1,0,1]

Example 3:
    Input: n = 1
    Output: [0]

Constraints:
    1 <= n <= 1000
"""


class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: list[int]
        """
        if n == 1:
            return [0]

        if n == 2:
            return [-1, 1, 0]

        if n == 3:
            return [-n, n, 0]

        result = [n, -n]
        if n % 2 != 0:
            result.append(0)

        i = len(result)
        while i < n:
            result.append(-i)
            result.append(i)
            n -= 1
            i += 1

        return result


if __name__ == '__main__':
    print(Solution().sumZero(7))
