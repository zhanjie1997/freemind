import xlwt

writebook = xlwt.Workbook()  # 打开excel
test = writebook.add_sheet('test', cell_overwrite_ok=True)
first_row = ["用例目录", "用例名称", "需求ID", "前置条件", "用例步骤", "预期结果", "用例类型", "用例状态", "用例等级", "创建人"]
k = 0
for content in first_row:
    test.write(0, k, content)
    k += 1
with open("free_mind_data.txt", "r") as ff:
    data = ff.read()
    # print(data,type(data))
    testcase = data.split("/*/")
    # print(testcase,len(testcase)-1)
    forward_data = []
    for i in range(len(testcase) - 1):
        step = testcase[i].split("**")
        # print("STEP:",step,int(step[-1][0]))
        if int(step[-1][0]) == len(step):
            forward_data = step
            print("新step", step)
            # print("forward_data1", forward_data)
        elif int(step[-1][0]) != len(step):
            if int(step[0][0]) <= len(forward_data) + 1:
                forward_data = forward_data[0:int(step[0][0]) - 1]
                # print("forward_data",forward_data)
                newstep = forward_data + step
                forward_data = forward_data + step
                print("新step", newstep)
                for j in range(len(newstep)):
                    if "用例目录" in newstep[j] or newstep[0] == "A":
                        # print(i,0,step[j])
                        test.write(i + 1, 0, newstep[j])
                    elif "用例名称" in newstep[j] or newstep[0] == "B":
                        # print(i,0,step[j])
                        test.write(i + 1, 1, newstep[j])
                    elif "需求ID" in newstep[j] or newstep[0] == "C":
                        # print(i,0,step[j])
                        test.write(i + 1, 2, newstep[j])
                    elif "前置条件" in newstep[j] or newstep[0] == "D":
                        # print(i,0,step[j])
                        test.write(i + 1, 3, newstep[j])
                    elif "用例步骤" in newstep[j] or newstep[0] == "E":
                        # print(i,0,step[j])
                        test.write(i + 1, 4, newstep[j])
                    elif "预期结果" in newstep[j] or newstep[0] == "F":
                        # print(i,0,step[j])
                        test.write(i + 1, 5, newstep[j])
                    elif "用例类型" in newstep[j] or newstep[0] == "G":
                        # print(i,0,step[j])
                        test.write(i + 1, 6, newstep[j])
                    elif "用例状态" in newstep[j] or newstep[0] == "H":
                        # print(i,0,step[j])
                        test.write(i + 1, 7, newstep[j])
                    elif "用例等级" in newstep[j] or newstep[0] == "I":
                        # print(i,0,step[j])
                        test.write(i + 1, 8, newstep[j])
                    elif "创建人" in newstep[j] or newstep[0] == "J":
                        # print(i, 0, step[j])
                        test.write(i + 1, 9, newstep[j])
                    else:
                        # print(i, j, step[j])
                        test.write(i + 1, j, newstep[j])

writebook.save('testdata.xls')
