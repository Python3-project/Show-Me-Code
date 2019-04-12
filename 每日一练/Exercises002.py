#!/usr/bin/python3
#-*- coding:utf-8 -*-
# Author YANGYUANJIU

import random

"""
第 0002 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
"""

def gen_code(length=8):
    """
    :param length:
    :return: rand_str
    将0-9，a-z,A-Z保存到list中，用random.sample从List中选取length位字符

    """
    code_list =[]

    for i in range(10):
        code_list.append(str(i))
    for i in range(65,91):
        code_list.append(chr(i))
    for i in range(97,123):
        code_list.append(chr(i))
    # for i in range(0x4e00,0x9fa5):
    #     code_list.append(chr(i))

    myslist = random.sample(code_list,length)
    veri_code = ''.join(myslist)
    return veri_code

if __name__ == '__main__':
    length=int(input('请输入您需要的随机字符长度：'))
    num = int(input('请输入您需要的随机字符数量：'))
    for i in range(num):
        #print('i:{i}'.format(i=i))
        print('{list}\n'.format(list=gen_code(length)))
