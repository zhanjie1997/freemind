import requests
import time
import json


# a={
#         "source_code": "CN002721-221201-0002",
#         "cat_id": 612,
#         "cat_id_original":612,
#         "ServerCode":"LM1145",
#         "SignBody":"SZYKD11",
#         "AirlineCode":"58",
#         "AirportCodeStart":"CGO",
#         "AirportCodeEnd":"ORD"
#     }

# print(a)
# print(a['source_code'])

# def demo1(n):
#     b = []
#     m = 'CESHI-221202-0'
#     for i in range(n):
#         a = {
#         "source_code": "CESHI-221202-00",
#         "cat_id": 29345,
#         "cat_id_original":29345,
#         "ServerCode":"CT0162",
#         "SignBody":"HLGYL",
#         "AirlineCode":"00",
#         "AirportCodeStart":"HKG",
#         "AirportCodeEnd":"AMS"
#     }
#
#         a['source_code'] = m + str(i)
#         b.append(a)
#     c = json.dumps(b, ensure_ascii=False)
#     print(c)

# def demo2(n):
#     b = []
#     m = 'CESHI-221202-0'
#     for i in range(n):
#         a = {
#         "source_code":"CESHI-221201-0286",
#         "cat_id":"29345"
#         }
#
#         a['source_code'] = m + str(i)
#         b.append(a)
#     c = json.dumps(b, ensure_ascii=False)
#     print(c)

import requests
import time
import json


# a={
#         "source_code": "CN002721-221201-0002",
#         "cat_id": 612,
#         "cat_id_original":612,
#         "ServerCode":"LM1145",
#         "SignBody":"SZYKD11",
#         "AirlineCode":"58",
#         "AirportCodeStart":"CGO",
#         "AirportCodeEnd":"ORD"
#     }

# print(a)
# print(a['source_code'])

# def demo1(n):
#     b = []
#     m = 'CESHI-221202-0'
#     for i in range(n):
#         a = {
#         "source_code": "CESHI-221202-00",
#         "cat_id": 29345,
#         "cat_id_original":29345,
#         "ServerCode":"CT0162",
#         "SignBody":"HLGYL",
#         "AirlineCode":"00",
#         "AirportCodeStart":"HKG",
#         "AirportCodeEnd":"AMS"
#     }
#
#         a['source_code'] = m + str(i)
#         b.append(a)
#     c = json.dumps(b, ensure_ascii=False)
#     print(c)

# def demo3(n):
#     b = []
#     # m = 'CESHI-221202-0'
#     for i in range(n):
#         a =  { "waybill_code":"100-20230414100500377", "weight":"5", "Country":"US", "system_source":"101", "unit_code":"KG", "Fk_type":"N", "cost_type":"QG" }
#
#         # a['source_code'] = m + str(i)
#         b.append(a)
#     c = json.dumps(b, ensure_ascii=False)
#     print(c)


def demo4(n):
    b = []
    numbers = 0
    for i in range(n):
        a =  { "waybill_code":"YT20230426121049-090", "weight":"5", "Country":"US", "system_source":"101", "unit_code":"KG", "Fk_type":"N", "cost_type":"PS" }

        # a['waybill_code'] = m[numbers]
        b.append(a)
        # numbers = numbers + 1
    c = json.dumps(b, ensure_ascii=False)
    print(c)

file_size=input("请输入想要生成文件的大小：(单位MB)")
class MakeDir:
    def __init__(self):
        self.file_path="D:\Documents\Desktop\文件/"
        self.file_name="文件大小"+file_size+"MB"
        new_file_size = file_size.strip()
        file_size_list = new_file_size.split(".")
        self.file_size_list = file_size_list
    def fileSize_making(self):
        #输入的文件大小去除首尾空格后切割，如果列表中只有一个数字说明是整数，否则就是小数
        if len(self.file_size_list) == 1:
            self.int_size_mb()
            print("文件大小{}MB,已存入地址{}".format(file_size,self.file_path))
        else:
            self.int_size_mb()
            self.float_size_mb()
            print("文件大小{}MB,已存入地址{}".format(file_size,self.file_path))
    def int_size_mb(self):
        #整数部分用写入文件w方式
        with open(self.file_path+self.file_name,"w") as file:
            #b-kb-mb文件大小转化
            for i in range(int(self.file_size_list[0])):
                for j in range(1024):
                    file.write("01"*512)
    def float_size_mb(self):
        #小数部分用追加写入a方法
        with open(self.file_path+self.file_name,"a") as file:
            #获取小数（单位mb）
            float_size_mb=float(file_size)-int(self.file_size_list[0])
            for i in range(1024):
                file.write("1"*int(1024*float_size_mb))
#调用生成文件
# MakeDir().fileSize_making()


if __name__ == '__main__':
    # n=501
    # demo1(n)
    # demo2(n)
    # demo2(n)
    # demo4(n)
    MakeDir().fileSize_making()