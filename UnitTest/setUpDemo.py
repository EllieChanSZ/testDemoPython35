# -*- coding: UTF-8 -*-
# *************
# 构建单元测试用例
# *************
import unittest

class StringStripTestCase(unittest.TestCase):
    def setUp(self):
        self.source = "Pythom"
    def testBlank(self):
        expect = "Python"
        result = self.source.replace("m","n")
        self.assertEqual(expect, result)

class StringReplaceTestCase(unittest.TestCase):
    """定义原字符串"""
    def setUp(self):
        self.source = "selenium"

    """测试空字符串的替换"""
    def testBlank(self):
        expect = "selenium"
        result = self.source.replace("","")
        self.assertEqual(expect, result)

    """测试空字符串的替换字符*"""
    def testBlankOrd(self):
        self.source = "sel   eni     um"
        expect = "sel***eni*****um"
        result = self.source.replace(" ","*")
        self.assertEqual(expect, result)

    """测试常规字符串的替换空字符"""
    def testCommonSymbol(self):
        expect = "seleni"
        result = self.source.replace("um","")
        self.assertEqual(expect, result)

    """测试常规字符串的替换字符"""
    def testCommonSymbolEx(self):
        expect = "seleniumm"
        result = self.source.replace("m", "mm")
        self.assertEqual(expect, result)

# *************
# 构建单元测试套件-部分
# *************
#
# def suite():
#     StringReplaceTestSuite = unittest.TestSuite
#     StringReplaceTestSuite.addTest(StringReplaceTestCase("testBlank"))
#     StringReplaceTestSuite.addTest(StringReplaceTestCase("testCommonSymbol"))
#     return StringReplaceTestSuite

# *************
# 构建单元测试套件-全部-嵌套
# *************
def suite():
    StringReplaceTestSuite = unittest.makeSuite(StringReplaceTestCase,'test')
    StringStripTestSuite = unittest.makeSuite(StringStripTestCase, 'test')
    allTests = unittest.makeSuite(StringReplaceTestSuite, StringStripTestSuite)
    return allTests
