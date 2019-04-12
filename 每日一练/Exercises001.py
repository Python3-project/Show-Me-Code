#!/usr/bin/python3
#-*- coding:utf-8 -*-
# Author YANGYUANJIU

"""
第0001练习题
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果
"""

#首先，导入必要的库
from PIL import Image,ImageDraw,ImageFont
import random
import time


def put_num_upright(pic,num):
    im = Image.open(pic) #打开pic文件
    draw = ImageDraw.Draw(im) #创建draw对象
    x,y = im.size #获取尺寸
    #print("{pic},长：{x},高：{y}".format(pic=pic,x=x,y=y))
    font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 40)# 字体设置
    draw.text([200, 100], text=num, fill=(255, 0, 0), font=font)
    im.save('pic_get_{name}.png'.format(name=num),'png') #保存修改后的图片，路径没要求则是PY所在的文件夹内
if __name__ == '__main__':
    pic = '微信截图_20190412160145.png' #图片路径，默认py文件所在位置
    for i in range(1000):
        localtime = time.localtime(time.time())
        str1 = str(localtime[0]) + str(localtime[1]) + str(localtime[2]) + str(localtime[3]) + str(localtime[4]) + str(localtime[5])
        put_num_upright(pic, str1)
        #time.sleep(1)
        print("共保存{num}张图片,正在保存第{cnt}张，还剩{ends}张".format(num=1000,cnt=i,ends=1000-i-1))
