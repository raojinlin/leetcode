"""
1309. Decrypt String from Alphabet to Integer Mapping

Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:
    Characters ('a' to 'i') are represented by ('1' to '9') respectively.
    Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.

Return the string formed after mapping.
It's guaranteed that a unique mapping will always exist.

Example 1:
    Input: s = "10#11#12"
    Output: "jkab"
    Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

Example 2:
    Input: s = "1326#"
    Output: "acz"

Example 3:
    Input: s = "25#"
    Output: "y"

Example 4:
    Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
    Output: "abcdefghijklmnopqrstuvwxyz"

Constraints:
    1 <= s.length <= 1000
    s[i] only contains digits letters ('0'-'9') and '#' letter.
    s will be valid string such that mapping is always possible.

"""


def encode(s):
    result = ''
    for c in s:
        code = ord(c) - 96
        if code >= 10:
            result += '%d#' % code
        else:
            result += str(code)

    return result


class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums = []
        for c in s:
            if c == '#' and len(nums) >= 2:
                first_digits = len(nums) - 2
                last_digits = len(nums) - 1
                number = "%d%d" % (nums[first_digits], nums[last_digits])
                nums[first_digits] = int(number)
                nums.pop(last_digits)
            else:
                nums.append(int(c))

        result = ''
        for n in nums:
            result += chr(96 + n)

        return result


if __name__ == '__main__':
    print(Solution().freqAlphabets('10#11#12'))
    print(Solution().freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))
    print(encode('jkab'))


