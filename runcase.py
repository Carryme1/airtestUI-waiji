import os
import unittest
import sys
# result = os.path.join(os.path.dirname(__file__), "result/")
casepath = os.path.join(os.path.dirname(__file__), "case")


def caseList():
    # 定义单元测试容器
    suite = unittest.TestSuite()
    # 定搜索用例文件的方法
    discover = unittest.defaultTestLoader.discover(casepath, pattern='test_*.py', top_level_dir=None)
    # 将discover方法筛选出来的用例，循环添加到测试套件中,打印出的用例信息会递增
    suite.addTests(discover)
    return suite

def creatSuite(pathlist):
    # 定义单元测试容器
    suite = unittest.TestSuite()
    for i in pathlist:
        suite.addTest(unittest.TestLoader().loadTestsFromName(i))
    return suite

if __name__=="__main__":
    suite=caseList()
    runner=unittest.TextTestRunner()
    runner.run(suite)