"""
709. To Lower Case


Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.



Example 1:

    Input: "Hello"
    Output: "hello"

Example 2:

    Input: "here"
    Output: "here"

Example 3:

    Input: "LOVELY"
    Output: "lovely"
"""


class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """

        r = ''
        for c in str:
            if 65 <= ord(c) < 97:
                r += chr(ord(c) + 32)
            else:
                r += c

        return r


if __name__ == '__main__':
    print(Solution().toLowerCase('ABCD.'))