# -*- coding: utf-8 -*-

import unittest
import database_utils

class testBench(unittest.TestCase):
    def setUp(self):
        print "Testing now"
    def tearDown(self):
        print "Done Testing"
    def test1_create_parent(self):
        r = database_utils.valid_create_parent("Alpha1", "Aa1!Aa1!", "Aa1!Aa1!", "Alpha", "1", "Alpha1@hotmail.com")
        self.assertEqual(r[1], True)
    def test2_create_parent(self):
        r = database_utils.valid_create_parent("Beta2", "Bb2!Bb2!", "Bb2!Bb2!2", "Beta", "2", "Beta2@hotmail.com")
        self.assertEqual(r[0], False)
    def test3_create_parent(self):
        r = database_utils.valid_create_parent("Beta2", "Bb2!Bb2!", "Bb2!Bb2!", "Beta", "2", "Alpha1@hotmail.com")
        self.assertEqual(r[0], False)
    def test4_parent_login(self):
        r = database_utils.valid_parent_login("Alpha1", "Aa1!Aa1!")
        self.assertEqual(r, True)
    def test5_parent_login(self):
        r = database_utils.valid_parent_login("Alpha1", "Aa1!Aa1!1")
        self.assertEqual(r, False)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(testBench)
    unittest.TextTestRunner(verbosity=2).run(suite)
