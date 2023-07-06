import sys
import os
import time
import datetime

sys.path.append(".")
from freemind.freemind_to_testcase import analyse_mm_file
from freemind.txt_to_excel import txt_to_excel

'''
freemind 转成txt          
'''
path = r"D:\Documents\Desktop\ME"
title = os.listdir(path)
for i in range(len(title)):
    file = path + "\\" + title[i][:-3] + ".mm"
    path_N = os.path.getmtime(file)  # 获取文件最后修改时间
    if str(datetime.date.fromtimestamp(path_N)) == str(time.strftime("%Y-%m-%d")):  # 取文件日期与当前日期对比
        file_txt = r"D:\Documents\Desktop\test_zhan\yif_utils\freemind\free_mind_data.txt"
        with open(file_txt, "w", encoding='utf-8') as fa:
            fa.truncate()
        analyse_mm_file(file, file_txt)
        '''
        txt 转成 测试用例
        '''
        file_result = title[i][:-3] + ".xlsx"
        file_txt = r"D:\Documents\Desktop\test_zhan\yif_utils\freemind\free_mind_data.txt"
        file_moduel = r"D:\Documents\Desktop\test_zhan\yif_utils\freemind\testcate_excle\dts_国内转运管理系统_测试用例.xlsx"
        print(file_moduel)
        txt_to_excel(file_txt, file_moduel, file_result)

