"""
1656. Design an Ordered Stream

There is a stream of n (id, value) pairs arriving in an arbitrary order, where id is an integer between 1 and n and value is a string.
No two pairs have the same id.

Design a stream that returns the values in increasing order of their IDs by returning a chunk (list) of values after each insertion.
The concatenation of all the chunks should result in a list of the sorted values.

Implement the OrderedStream class:

OrderedStream(int n) Constructs the stream to take n values.
String[] insert(int id, String value) Inserts the pair (id, value) into the stream,
then returns the largest possible chunk of currently inserted values that appear next in the order.

Input
    ["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
    [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
Output
    [null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]

Explanation
    // Note that the values ordered by ID is ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"].
    OrderedStream os = new OrderedStream(5);
    os.insert(3, "ccccc"); // Inserts (3, "ccccc"), returns [].
    os.insert(1, "aaaaa"); // Inserts (1, "aaaaa"), returns ["aaaaa"].
    os.insert(2, "bbbbb"); // Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
    os.insert(5, "eeeee"); // Inserts (5, "eeeee"), returns [].
    os.insert(4, "ddddd"); // Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].
    // Concatentating all the chunks returned:
    // [] + ["aaaaa"] + ["bbbbb", "ccccc"] + [] + ["ddddd", "eeeee"] = ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"]
    // The resulting order is the same as the order above.
"""


class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.list = [None for _ in range(n)]
        self.ptr = 0

    def move_ptr(self, j):
        """
        move the pointer from j to next available slot eg. self.list[j] is None
        :param j: the start position
        :return:
        """
        while j < len(self.list):
            if self.list[j] is None:
                # found a available slot
                self.ptr = j
                return
            j += 1

        # not found, set pointer to len(self.list)
        self.ptr = len(self.list)

    def insert(self, id, value):
        """
        :type id: int
        :type value: str|None
        :rtype: List[str]
        """

        i = id - 1
        self.list[i] = value

        if i == self.ptr:
            self.move_ptr(i)
            return self.list[i:self.ptr]

        return []


if __name__ == '__main__':
    o = OrderedStream(5)
    print(o.insert(3, 'ccccc'))
    print(o.insert(1, 'aaaaa'))
    print(o.insert(2, 'bbbbb'))
    print(o.insert(5, 'eeeee'))
    print(o.insert(4, 'ddddd'))
