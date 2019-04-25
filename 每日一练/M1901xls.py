#!/usr/bin/python3
#-*- coding:utf-8 -*-
# Author YANGYUANJIU

import xlwt
import xlrd
from xlutils.copy import copy
import re
def read_M1901_ARM_COM_LOG():
    NUMERIC_SORT = []
    STRING_SORT = []
    BITFIELD = []
    FP_EMULATION = []
    FOURIER = []
    IDEA = []
    HUFFMAN = []
    LU_DECOMPOSITION = []
    testdatas = {'NUMERIC_SORT': NUMERIC_SORT,
                'STRING_SORT': STRING_SORT,
                'BITFIELD': BITFIELD,
                'FP_EMULATION': FP_EMULATION,
                'FOURIER': FOURIER,
                'IDEA': IDEA,
                'HUFFMAN': HUFFMAN,
                'LU_DECOMPOSITION': LU_DECOMPOSITION
                }
    f = open('M1901零下20摄氏度性能测试_0.log', 'r')
    for line in f:
        red_log_line = f.readline()
        searchObj = re.search(r'NUMERIC SORT', red_log_line, re.M | re.I)
        if searchObj:
            data = re.findall('[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?', red_log_line)
            testdatas['NUMERIC_SORT'].append(data[0][0])

        searchObj = re.search(r'STRING SORT', red_log_line, re.M | re.I)
        if searchObj:
            data = re.findall('[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?', red_log_line)
            testdatas['STRING_SORT'].append(data[0][0])

        searchObj = re.search(r'BITFIELD', red_log_line, re.M | re.I)
        if searchObj:
            data = re.findall('[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?', red_log_line)
            testdatas['BITFIELD'].append(data[0][0])

        searchObj = re.search(r'FP EMULATION', red_log_line, re.M | re.I)
        if searchObj:
            data = re.findall('[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?', red_log_line)
            testdatas['FP_EMULATION'].append(data[0][0])

        searchObj = re.search(r'FOURIER', red_log_line, re.M | re.I)
        if searchObj:
            data = re.findall('[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?', red_log_line)
            testdatas['FOURIER'].append(data[0][0])

        searchObj = re.search(r'IDEA', red_log_line, re.M | re.I)
        if searchObj:
            data = re.findall('[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?', red_log_line)
            testdatas['IDEA'].append(data[0][0])

        searchObj = re.search(r'HUFFMAN', red_log_line, re.M | re.I)
        if searchObj:
            data = re.findall('[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?', red_log_line)
            testdatas['HUFFMAN'].append(data[0][0])

        searchObj = re.search(r'LU DECOMPOSITION', red_log_line, re.M | re.I)
        if searchObj:
            data = re.findall('[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?', red_log_line)
            testdatas['LU_DECOMPOSITION'].append(data[0][0])
    f.close()
    return testdatas

# #只能写不能读
stus = ['NUMERIC SORT', 'STRING SORT', 'BITFIELD', 'FP EMULATION','FOURIER','IDEA','HUFFMAN','LU DECOMPOSITION']
book = xlwt.Workbook()#新建一个excel
sheet = book.add_sheet('CPU性能测试-20℃')#添加一个sheet页
row = 0#控制行
col = 0#控制列
for stu in stus:
    sheet.write(row, col, stu)
    col+=1
book.save('M1901性能测试.xls')#保存到当前目录下

#xlutils:修改excel
book1 = xlrd.open_workbook('M1901性能测试.xls')
sheet_r = book1.sheet_by_index(0)#根据顺序获取sheet
#sheet2_r = book1.sheet_by_name('CPU性能测试-20℃')#根据sheet页名字获取sheet
# print("col={col}".format(col=sheet_r.ncols))#获取excel里面有多少列
# print("row={row}".format(row=sheet_r.nrows))#获取excel里面有多少行

row=sheet_r.nrows
col=sheet_r.ncols

book2 = copy(book1)#拷贝一份原来的excel
# print(dir(book2))
sheet = book2.get_sheet(0)#获取第几个sheet页，book2现在的是xlutils里的方法，不是xlrd的
testdatas=read_M1901_ARM_COM_LOG()
print()
j=0
tmp_row=row
for i in testdatas:
    for s in testdatas[i]:
        sheet.write(tmp_row,j,float(s))
        tmp_row+=1
    tmp_row = row
    j+=1

book2.save('M1901性能测试.xls')
