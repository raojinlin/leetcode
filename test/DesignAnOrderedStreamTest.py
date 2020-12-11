import unittest
from lettcode.DesignAnOrderedStream import OrderedStream


class DesignAnOrderedStreamTest(unittest.TestCase):
    def test_ordered_stream(self):
        os = OrderedStream(9)
        self.assertEqual(os.insert(9, 'nghbm'), [])
        self.assertEqual(os.insert(7, 'hgeob'), [])
        self.assertEqual(os.insert(6, 'mwlrz'), [])
        self.assertEqual(os.insert(4, 'oalee'), [])
        self.assertEqual(os.insert(2, 'bouhq'), [])
        self.assertEqual(os.insert(1, 'mnknb'), ['mnknb', 'bouhq'])
        self.assertEqual(os.insert(5, 'qkxbj'), [])
        self.assertEqual(os.insert(8, 'iydkk'), [])
        self.assertEqual(os.insert(3, 'oqdnf'), ["oqdnf", "oalee", "qkxbj", "mwlrz", "hgeob", "iydkk", "nghbm"])

        o = OrderedStream(5)
        self.assertEqual([], o.insert(3, 'ccccc'))
        self.assertEqual(['aaaaa'], o.insert(1, 'aaaaa'))
        self.assertEqual(['bbbbb', 'ccccc'], o.insert(2, 'bbbbb'))
        self.assertEqual([], o.insert(5, 'eeeee'))
        self.assertEqual(['ddddd', 'eeeee'], o.insert(4, 'ddddd'))
