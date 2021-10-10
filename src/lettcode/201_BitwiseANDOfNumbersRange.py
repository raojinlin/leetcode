class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if not left:
            return 0

        shift_count = 0
        while left != right:
            left //= 2
            right //=  2
            shift_count += 1
        
        return left << shift_count


if __name__ == "__main__":
    solution = Solution()
    print(solution.rangeBitwiseAnd(5, 7))
    print(solution.rangeBitwiseAnd(0, 0))
    print(solution.rangeBitwiseAnd(1, 2))
    print(solution.rangeBitwiseAnd(1, 2147483647))
    print(solution.rangeBitwiseAnd(553, 555))
    print(solution.rangeBitwiseAnd(600000000, 2147483647))

        