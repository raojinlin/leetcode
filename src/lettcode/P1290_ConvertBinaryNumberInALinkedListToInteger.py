"""
1290. Convert Binary Number in a Linked List to Integer

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.



Example 1:

    [1] -> [0] -> [1]

    Input: head = [1,0,1]
    Output: 5
    Explanation: (101) in base 2 = (5) in base 10


Example 2:

    Input: head = [0]
    Output: 0

Example 3:

    Input: head = [1]
    Output: 1

Example 4:

    Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
    Output: 18880

Example 5:

    Input: head = [0,0]
    Output: 0
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(*values):
        values = list(values)
        head = ListNode(values.pop(0))

        current = head
        while values:
            current.next = ListNode(values.pop(0))
            current = current.next

        return head


class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        result = head.val
        while head.next:
            result = result * 2 + head.next.val
            head = head.next

        return result

    def getDecimalValueBit(self, head):
        result = head.val
        while head.next:
            result = (result << 1) | head.next.val
            head = head.next

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.getDecimalValue(ListNode.from_list(1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0)))
    print(s.getDecimalValueBit(ListNode.from_list(1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0)))
    print(s.getDecimalValueBit(ListNode.from_list(1, 0, 1)))
