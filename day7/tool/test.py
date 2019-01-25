# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/1/25 22:00
@file: test.py
@function:
'''
from business import *

model3.test1()
model3.test2()
model3.test3()
# model1不能引用，因为business下的init文件设置了只能引用model3
# model1.project_info()
