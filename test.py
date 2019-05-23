
import unittest
from unittest import TestCase
from dictnamespace import DictNamespace


class Test(TestCase):
    def test_indexing(self):
        d = dict(a=1, b=2)
        dn = DictNamespace(d)

        self.assertEqual(dn.a, d['a'])
        self.assertEqual(dn['a'], d['a'])

    def test_modify(self):
        d = dict(a=3)
        dn = DictNamespace(d)

        self.assertEqual(dn.a, 3)

        dn.a = 4
        self.assertEqual(dn.a, 4)
        self.assertEqual(d['a'], 4)

        d['a'] = 5
        self.assertEqual(dn.a, 5)

    def test_del(self):
        d = dict(a = 1, b = 2)
        dn = DictNamespace(d)
        del dn['a']
        self.assertNotIn('a', dn)
        self.assertNotIn('a', d)

    def test_metamethods(self):
        d = dict(a = True, b = 2, c = 'Hello world')
        dn = DictNamespace(d)

        self.assertIn('b', dn)
        self.assertNotIn('d', dn)

        self.assertEqual(frozenset(iter(dn)), frozenset(d.keys()))
        self.assertEqual(len(d), len(d))

        self.assertEqual(str(dn), str(d))
        self.assertEqual(repr(dn), repr(d))

if __name__ == '__main__':
    unittest.main()
