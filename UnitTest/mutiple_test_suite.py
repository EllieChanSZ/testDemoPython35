# *************
# 构建单元测试套件-全部-嵌套
# *************
import unittest
from UnitTest.StringReplaceFeature import StringReplaceTestCase
from UnitTest.StringStripFeature import StringStripTestCase
if __name__ == "__main__":
		#运行部分用例方式1 - addTest
		# StringReplaceTestSuite = unittest.TestSuite()
		# StringReplaceTestSuite.addTest(StringReplaceTestCase("testBlank"))
		# StringReplaceTestSuite.addTest(StringReplaceTestCase("testCommonSymbol"))
		# StringReplaceTestRunner = unittest.TextTestRunner()
		# StringReplaceTestRunner.run(StringReplaceTestSuite)

		#运行部分用例方式2 - addTests
		# StringReplaceTestSuite = unittest.TestSuite()
		# StringReplaceTestSet = [StringReplaceTestCase("testBlank"),
		# 						StringReplaceTestCase("testBlankOrd"),
		# 						StringReplaceTestCase("testCommonSymbol")]
		# StringReplaceTestSuite.addTests(StringReplaceTestSet)
		# StringReplaceTestRunner = unittest.TextTestRunner()
		# StringReplaceTestRunner.run(StringReplaceTestSuite)

		#运行全部用例套件方式1
		# StringReplaceTestSuite = unittest.makeSuite(StringReplaceTestCase,'test')
		# StringReplaceTestRunner = unittest.TextTestRunner(verbosity=2) #details console print
		# StringReplaceTestRunner.run(StringReplaceTestSuite)

		#运行全部用例套件方式2-skip
		StringReplaceTestSuite = unittest.makeSuite(StringReplaceTestCase,'test')
		#StringStripTestSuite = unittest.makeSuite(StringStripTestCase, 'test')
		StringReplaceTestRunner = unittest.TextTestRunner(verbosity=2)
		StringReplaceTestRunner.run(StringReplaceTestSuite)
