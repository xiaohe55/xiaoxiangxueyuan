# -*- coding:utf-8 -*-
num1 = int(input('请输入第一个数字：'))
operator = input('请输入运算符：')
num2 = int(input('请输入第二个数字：'))


if operator=="+":
    result = num1+num2
    print("计算结果： {}".format(result))
elif operator == "-":
    result = num1 - num2
    print("计算结果： {}".format(result))
elif operator == "%":
    result = num1 % num2
    print("计算结果： {}".format(result))
elif operator == "*":
    result = num1 * num2
    print("计算结果： {}".format(result))
elif operator == "/":
    result = num1 / num2
    print("计算结果： {}".format(result))
elif operator == "//":
    result = num1 // num2
    print("计算结果： {}".format(result))
else:
    print("正在开发")