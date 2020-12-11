"""
1365. How Many Numbers Are Smaller Than the Current Number

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is,
for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Example 1:

    Input: nums = [8,1,2,2,3]
    Output: [4,0,1,1,3]
    Explanation:
    For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
    For nums[1]=1 does not exist any smaller number than it.
    For nums[2]=2 there exist one smaller number than it (1).
    For nums[3]=2 there exist one smaller number than it (1).
    For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).


Example 2:

    Input: nums = [6,5,4,8]
    Output: [2,1,0,3]
    Example 3:

    Input: nums = [7,7,7,7]
    Output: [0,0,0,0]


O(n) solution

Nothing too special. The 'counts' array records the frequency of each number(the index),
the 'countUntil' array records the total number less than this number(the index),
so if we need the number less than a number just use the countUntil - counts to exclude itself.

public int[] smallerNumbersThanCurrent(int[] nums) {
    int[] counts = new int[101];
    int[] countUntil = new int[101];
    for(int num : nums){
        counts[num]++;
        countUntil[num]++;
    }

    for(int i = 1; i<counts.length; i++){
        countUntil[i]+=countUntil[i-1];
    }

    int[] res = new int[nums.length];
    for(int i = 0; i<nums.length; i++){
        res[i] = countUntil[nums[i]] - counts[nums[i]];
    }

    return res;
}
"""


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    res[i] += 1

        return res


if __name__ == '__main__':
    print(Solution().smallerNumbersThanCurrent([1, 2, 3, 4]))
    print(Solution().smallerNumbersThanCurrent([8, 2, 3, 4]))
