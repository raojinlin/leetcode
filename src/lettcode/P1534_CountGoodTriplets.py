"""
1534. Count Good Triplets

Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.


A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

    0 <= i < j < k < arr.length
    |arr[i] - arr[j]| <= a
    |arr[j] - arr[k]| <= b
    |arr[i] - arr[k]| <= c

Where |x| denotes the absolute value of x.
Return the number of good triplets.

Example 1:
    Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
    Output: 4
    Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

Example 2:
    Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
    Output: 0
    Explanation: No triplet satisfies all conditions.


Constraints:
    3 <= arr.length <= 100
    0 <= arr[i] <= 1000
    0 <= a, b, c <= 1000
"""


class Solution(object):
    def is_good_triplets(self, i, j, k, a, b, c):
        return abs(i - j) <= a and abs(j - k) <= b and abs(i - k) <= c

    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        res = 0

        for i in range(len(arr)):
            j = i + 1

            while j < len(arr):
                k = j + 1

                while k < len(arr):
                    if self.is_good_triplets(arr[i], arr[j], arr[k], a, b, c):
                        res += 1

                    k += 1

                j += 1

        return res


if __name__ == '__main__':
    print(Solution().countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3))
    print(Solution().countGoodTriplets(arr=[1, 1, 2, 2, 3], a=0, b=0, c=1))
