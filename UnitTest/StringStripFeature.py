# -*- coding: UTF-8 -*-
import unittest

class StringStripTestCase(unittest.TestCase):
    def setUp(self):
        """定义原字符串"""
        self.source = "Pythom"

    def testBlank(self):
        expect = "Python"
        result = self.source.replace("m","n")
        self.assertEqual(expect, result)

