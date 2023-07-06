import os
from html.parser import HTMLParser


def analyse_mm_file(mm_file, file_txt):
    if os.path.isfile(mm_file):
        num = 1  # 记录行号的标记
        point = 0  # 记录叶子节点的标记 1 是根节点
        mark_node = 0  # 记录节点信息标记
        mark_note = 0  # 记录备注信息标记
        flow = ""  # 记录流程信息
        point_str = ""
        with open(mm_file) as f:
            lines = f.readlines()
            for line in lines:
                line = line.rstrip('\n')
                # print(line)
                if mark_node == 1 or mark_note == 1:
                    with open("temp.html", mode="a", encoding="UTF-8") as f:
                        if line.rfind('<richcontent TYPE="NODE"><html>') != -1 or \
                                line.rfind('<richcontent TYPE="NOTE"><html>') != -1:
                            f.write("<html>\n")
                            num += 1
                        elif line.rfind('</html>') != -1:
                            f.write("</html>\n")
                            num += 1
                        elif line.rfind('</richcontent>') != -1:
                            num += 1
                        elif line.rfind('</node>') != -1:
                            point -= 1
                            if mark_node == 1: mark_node = 2
                            if mark_note == 1: mark_note = 2
                            num += 1
                        else:
                            f.write(line + "\n")
                            num += 1
                    continue
                if mark_node == 2 or mark_note == 2:
                    data = analyse_html("./temp.html")
                    # print("data = ", data)
                    os.remove("./temp.html")
                    if mark_node == 2:
                        # 操作 node 节点信息
                        for i in range(len(data)):
                            result = data[i].replace('\n', '')
                            print(result)
                    if mark_note == 2:
                        # 操作 note 备注信息
                        for i in range(len(data)):
                            result = data[i].replace('\n', '')
                            # print(result)
                    if mark_node != 0: mark_node = 0
                    if mark_note != 0: mark_note = 0
                if line.rfind('<map version="1.0.1">') == 0 and num == 1:
                    num += 1
                if line.rfind('</map>') == 0:
                    print("解析文件完成！共解析 {} 行。".format(num))
                elif line.rfind('</node>') == 0:
                    point -= 1
                    num += 1
                elif line.rfind('<node ') == 0:
                    point += 1
                    '''
                    if len(flow) == 0:
                        flow = "{}".format(point)
                    else:
                        if point == int(flow.split("_")[len(flow.split("_")) - 1]):
                            pass
                        else:
                            if point < int(flow.split("_")[len(flow.split("_")) - 1]):
                                flow = flow.split(str(point))[0] + str(point)
                            else:
                                flow = "{}_{}".format(flow, point)
                    print("总体的线性流程：", flow)'''
                    # print("总体的线性流程：", point)
                    print(point)
                    with open(file_txt, "a+") as ff:
                        if line.rfind('" TEXT="') != -1 and line[-2:] == '">':
                            start_num = line.rfind('" TEXT="') + 8
                            # print("start num = ", start_num)
                            get_value = get_chinese(line[start_num: len(line) - 2])
                            print(get_value)
                            ff.write(str(point) + "/#/" + get_value + "**")
                        elif line.rfind('" TEXT="') != -1 and line[-2:] == '/>':
                            point -= 1
                            start_num = line.rfind('" TEXT="') + 8
                            # print("start num = ", start_num)
                            get_value = get_chinese(line[start_num: len(line) - 3])
                            print(get_value)
                            ff.write(str(point + 1) + "/#/" + get_value + "/*/")
                        if line.rfind('" TEXT="') == -1:
                            mark_node = 1  # 存在 HTML 网页
                        num += 1
                elif line.rfind('<richcontent TYPE="NOTE"><html>') == 0:
                    with open("temp.html", mode="a", encoding="UTF-8") as f:
                        f.write('<html>\n')
                    mark_note = 1  # 存在备注信息
                elif line.rfind('<icon ') == 0:
                    # print(line)
                    num += 1
                elif line.rfind('<arrowlink ') == 0:  # 箭头指向，可以实现关联
                    # print(line)
                    num += 1
                elif line.rfind('<hook ') == 0:
                    # print(line)
                    num += 1
                elif line.rfind('<text>') == 0:
                    # point = point + 1
                    # print(line)
                    num += 1
                elif line.rfind('</hook>') == 0:
                    # print(line)
                    num += 1
                elif line.rfind('<cloud/>') == 0:
                    # print(line)
                    num += 1
                elif line.rfind('<font ') == 0:
                    # print(line)
                    num += 1
                elif line.rfind('<edge ') == 0:
                    # print(line)
                    num += 1
                else:
                    num += 1

    else:
        print("系统中没有找到没有FreeMind文件。{}".format(mm_file))
        exit()


def analyse_html(file_path):
    with open(file=file_path, mode="r", encoding="UTF-8") as f:
        page = f.read()
    html_parser = HP()
    html_parser.feed(page)
    html_parser.close()
    return html_parser.data


def get_chinese(line):
    get_word = ""
    array = line.split("&#x")
    flag = True
    if line.find("&#x") != -1:
        for i in range(len(array)):  # 遍历数组
            if len(array[i]) == 0 and flag:  # 第一个值为空时，继续循环
                flag = False
                continue

            if array[i][4:5] == ";":  # 解析Unicode字符
                unicode = "\\u" + array[i][:4]
                get_word = get_word + unicode.encode('latin-1').decode('unicode_escape') + array[i][5:]
            elif array[i][:2] == "a;":  # 换行转义
                get_word = get_word + "\n" + array[i][2:]
            else:
                get_word = get_word + array[i]

        return get_word
    else:
        return line.replace('&amp;', '&')


class HP(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.tag_text = False
        self.data = []

    def handle_starttag(self, tag, attr):
        if tag == 'p' or tag == 'li':
            self.tag_text = True
        if tag == 'img' and self._attr(attr, 'src'):
            self.data.append("img:{}".format(self._attr(attr, 'src')))

    def handle_endtag(self, tag):
        if tag == 'p' or tag == 'li':
            self.tag_text = False

    def handle_data(self, data):
        if self.tag_text:
            self.data.append(get_chinese(data))

    def _attr(self, attr_list, attr_name):
        for attr in attr_list:
            if attr[0] == attr_name:
                return attr[1]
        return None


if __name__ == "__main__":
    file = "F:\\GitCode\\python_testcase\\test_testcase\\新建思维导图.mm"
    file_txt = "F:\\GitCode\\python_testcase\\yif_utils\\free_mind_data.txt"
    with open(file_txt, "w") as fa:
        fa.truncate()
    analyse_mm_file(file, file_txt)
