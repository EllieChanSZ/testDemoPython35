# -*- coding: UTF-8 -*-

import unittest
class StringReplaceTestCase(unittest.TestCase):
    def setUp(self):
        """定义原字符串"""
        self.source = "selenium"

    def testBlank(self):
        """测试空字符串的替换"""
        expect = "selenium"
        result = self.source.replace("","")
        self.assertEqual(expect, result)

    def testBlankOrd(self):
        """测试空字符串的替换字符*"""
        self.source = "sel   eni     um"
        expect = "sel***eni*****um"
        result = self.source.replace(" ","*")
        self.assertEqual(expect, result)

    def testCommonSymbol(self):
        """测试常规字符串的替换空字符"""
        expect = "seleni"
        result = self.source.replace("um","")
        self.assertEqual(expect, result)

    @unittest.skip("ignore this case - testCommonSymbolEx!")
    #@unittest.skipUnless(4<3,"ignore this case - testCommonSymbolEx!")
    #括号中条件为假就跳过，条件为真就执行
    #@unittest.skipIf(4>3,"ignore this case - testCommonSymbolEx!")
    #括号中条件为假就执行，条件为真就跳过
    def testCommonSymbolEx(self):
        """测试常规字符串的替换字符"""
        expect = "seleniumm"
        result = self.source.replace("m", "mm")
        self.assertEqual(expect, result)









