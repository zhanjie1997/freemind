import xlwt
import xlrd
from xlutils.copy import copy

# writebook = xlwt.Workbook()                #打开excel
# test= writebook.add_sheet('test',cell_overwrite_ok=True)
# first_row = ["用例目录",	"用例名称",	"需求ID",	"前置条件",	"用例步骤",	"预期结果",	"用例类型",	"用例状态",	"用例等级",	"创建人"]
# k = 0
# for content in first_row:
#     test.write(0,k,content)
#     k +=1
# file_result = "./testcate_excle/dts_国内转运管理系统_测试用例20200508.xlsx"
# file_txt = "F:\\python_project\\yif_utils\\free_mind_data.txt"
# file_moduel = "./testcate_excle/dts_国内转运管理系统_测试用例.xlsx"
file_txt = "F:\\GitCode\\python_testcase\\yif_utils\\free_mind_data.txt"


def txt_to_excel(file_txt, file_moduel, file_result):
    '''

    :param file_moduel: 模板文件
    :param file_result: 产出文件测试用例文件
    :return:
    '''
    oldWb = xlrd.open_workbook(file_moduel)  # 先打开已存在的表
    newWb = copy(oldWb)
    test = newWb.get_sheet(0)
    read_excel = xlrd.open_workbook(file_moduel)
    table = read_excel.sheet_by_index(0)
    with open(file_txt, "r") as ff:
        data = ff.read()  # 打开读取mm转换后的txt文件
        # print(data,type(data))
        testcase = data.split("/*/")  # 分割去除多余的符号
        print(testcase)
        # print(testcase,len(testcase)-1)
        forward_data = []
        excel_name = ""
        for i in range(len(testcase) - 1):
            print(testcase[i])
            step = testcase[i].split("**")  # 分割去除多余的符号,把一条用例取出
            print(step, int(step[-1][0]))
            if int(step[-1].split("/#/")[0]) == len(step):
                print(step[-1], len(step))
                forward_data = step
                # excel_name = step[0].split("/#/")[1]   #把一条用例每个节点内容取出
                print("新step", step, excel_name)
                print("forward_data1", forward_data)
                newstep = step
                content_A = ""
                content_B = ""
                content_D = ""
                for j in range(len(newstep)):
                    content = newstep[j].split("/#/")[1]  # 把一条用例每个节点内容取出
                    flag_num = content[0].upper()  # ABCDEFGHIJK不区分大小写    #取节点头字母
                    if "分组" in newstep[j] or flag_num == "A":
                        # print(i,0,step[j])
                        if content_A == "":
                            content_A = content[1:]
                        else:
                            content_A = content_A + "-" + content[1:]
                            print("content_A", content_A)
                    elif "用例名称" in newstep[j] or flag_num == "B":
                        # print(i,0,step[j])
                        if content_B == "":
                            content_B = content[1:]
                        else:
                            content_B = content_B + "-" + content[1:]
                            print("content_B", content_B)
                    elif "被测需求编号" in newstep[j] or flag_num == "C":
                        # print(i,0,step[j])
                        test.write(i + 1, 2, content[1:])
                    elif "前置步骤" in newstep[j] or flag_num == "D":
                        # print(i,0,step[j])
                        content_D = content[1:]
                        test.write(i + 1, 3, content[1:])
                    elif "测试步骤" in newstep[j] or flag_num == "E":
                        # print(i,0,step[j])
                        test.write(i + 1, 4, content[1:])
                    elif "预期结果" in newstep[j] or flag_num == "F":
                        # print(i,0,step[j])
                        test.write(i + 1, 5, content[1:])
                    elif "用例类型" in newstep[j] or flag_num == "G":
                        # print(i,0,step[j])
                        test.write(i + 1, 6, content[1:])
                    elif "用例状态" in newstep[j] or flag_num == "H":
                        # print(i,0,step[j])
                        test.write(i + 1, 7, content[1:])
                    elif "用例等级" in newstep[j] or flag_num == "I":
                        # print(i,0,step[j])
                        test.write(i + 1, 8, content[1:])
                    elif "创建人" in newstep[j] or flag_num == "J":
                        # print(i, 0, step[j])
                        test.write(i + 1, 9, content[1:])
                    else:
                        # print(i, j, step[j])
                        pass
                        # test.write(i + 1, j, content[1:])

                test.write(i + 1, 0, content_A)
                test.write(i + 1, 1, content_B)
                content_D = "进入" + content_A + "页面" + content_D
                test.write(i + 1, 3, content_D)
            elif int(step[-1].split("/#/")[0]) != len(step):
                if int(step[0].split("/#/")[0]) <= len(forward_data) + 1:
                    forward_data = forward_data[0:int(step[0].split("/#/")[0]) - 1]
                    # print("forward_data",forward_data)
                    newstep = forward_data + step
                    forward_data = forward_data + step
                    print("新step", newstep)
                    content_A = ""
                    content_B = ""
                    content_D = ""
                    for j in range(len(newstep)):
                        content = newstep[j].split("/#/")[1]
                        try:
                            flag_num = content[0]
                        except Exception as e:
                            print(e)
                            continue
                        if "用例目录" in newstep[j] or flag_num == "A":
                            # print(i,0,step[j])
                            if content_A == "":
                                content_A = content[1:]
                            else:
                                content_A = content_A + "-" + content[1:]
                                print("content_A", content_A)
                        elif "用例名称" in newstep[j] or flag_num == "B":
                            # print(i,0,step[j])
                            print(newstep[j])
                            print(content)
                            if content_B == "":
                                content_B = content[1:]
                            else:
                                content_B = content_B + "-" + content[1:]
                                print("content_B", content_B)
                        elif "需求ID" in newstep[j] or flag_num == "C":
                            # print(i,0,step[j])
                            test.write(i + 1, 2, content[1:])
                        elif "前置条件" in newstep[j] or flag_num == "D":
                            # print(i,0,step[j])
                            content_D = content[1:]
                            test.write(i + 1, 3, content[1:])
                        elif "用例步骤" in newstep[j] or flag_num == "E":
                            # print(i,0,step[j])
                            test.write(i + 1, 4, content[1:])
                        elif "预期结果" in newstep[j] or flag_num == "F":
                            # print(i,0,step[j])
                            test.write(i + 1, 5, content[1:])
                        elif "用例类型" in newstep[j] or flag_num == "G":
                            # print(i,0,step[j])
                            test.write(i + 1, 6, content[1:])
                        elif "用例状态" in newstep[j] or flag_num == "H":
                            # print(i,0,step[j])
                            test.write(i + 1, 7, content[1:])
                        elif "用例等级" in newstep[j] or flag_num == "I":
                            # print(i,0,step[j])
                            test.write(i + 1, 8, content[1:])
                        elif "创建人" in newstep[j] or flag_num == "J":
                            # print(i, 0, step[j])
                            test.write(i + 1, 9, content[1:])
                        else:
                            # print(i, j, step[j])
                            pass
                            # test.write(i+1,j, content[1:])
                    test.write(i + 1, 0, content_A)
                    test.write(i + 1, 1, content_B)
                    content_D = "进入" + content_A + "页面" + content_D
                    test.write(i + 1, 3, content_D)
    newWb.save(file_result)


# txt_to_excel(file_txt, file_moduel, file_result)
