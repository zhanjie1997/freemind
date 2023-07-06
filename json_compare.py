# coding: utf-8
# author: Rainy Chan
# from types import NoneType
import json


class JCompare:
    def __init__(self, print_before=True):
        self.res = None
        self.ignore_list_seq = None
        self.print_before = print_before

    @staticmethod
    def tuple_append(t, i):
        return tuple(list(t) + [i])

    @staticmethod
    def to_unicode_if_string(strlike):
        if type(strlike) == str:
            try:
                return strlike.decode('utf-8')
            except:
                return strlike.decode('gbk')
        else:
            return strlike

    @staticmethod
    def modify_a_key(dic, from_key, to_key):
        assert not any([type(to_key) == type(exist_key) and to_key == exist_key for exist_key in
                        dic.keys()]), 'cannot change the key due to key conflicts'
        # 不能使用in，否则无法适配unicode和str
        dic[to_key] = dic.pop(from_key)

    def turn_dict_keys_to_unicode(self, dic):
        keys = dic.keys()
        for key in keys:  # a.keys() returns a constant, so this is safe that ak won't change
            if type(key) == str:
                # self.modify_a_key(dic, key, self.to_unicode_if_string(key))
                pass
            else:
                assert type(key) == "unicode", 'key {} must be string or unicode in dict {}'.format(key, dic)

    def set_false(self):
        self.res = False

    def different_type(self, a, b, root):
        self.set_false()
        print("different type at {}".format(root))
        print("a: " + repr(a))
        print("b: " + repr(b))

    def different_value(self, a, b, root):
        self.set_false()
        print("different value at {}".format(root))
        print("a: " + repr(a))
        print("b: " + repr(b))

    def different_length(self, a, b, root):
        self.set_false()
        print("different length of list at {}".format(root))
        print("len(a)={} : ".format(len(a)) + repr(a))
        print("len(b)={} : ".format(len(b)) + repr(b))

    def list_item_not_found(self, ele, which, root):
        self.set_false()
        print("list {} at {}".format(which, root))
        print("has element that another list hasn't :")
        print(repr(ele))

    def list_freq_not_match(self, root, aplace, bplace, ele, counta, countb):
        self.set_false()
        print("list at {}, index {}, has different frequency from b at index {}]".format(root, aplace, bplace))
        print("element is {}".format(ele))
        print("count of list a: {}".format(counta))
        print("count of list b: {}".format(countb))

    def dict_key_not_found(self, keys, which, root):
        self.set_false()
        print("dict {} at {}".format(which, root))
        print("has key(s) that another dict hasn't :")
        print(keys)

    def list_comp(self, a, b, root, printdiff):
        if len(a) != len(b):
            if not printdiff: return False
            self.different_length(a, b, root)
            return

        if not self.ignore_list_seq:
            for i in range(min(len(a), len(b))):
                buff = self.tuple_append(root, i)
                if self.common_comp(a[i], b[i], buff, printdiff) == False:
                    return False
        else:
            counts_a = [[0, None] for _ in range(len(a))]
            counts_b = [[0, None] for _ in range(len(a))]
            neet_to_compare_number = True

            for i in range(len(a)):
                for j in range(len(a)):
                    if self.common_comp(a[i], b[j], printdiff=False):
                        counts_a[i][1] = j
                        counts_a[i][0] += 1
                    if self.common_comp(b[i], a[j], printdiff=False):
                        counts_b[i][1] = j
                        counts_b[i][0] += 1

                if not counts_a[i][0]:
                    if not printdiff: return False
                    neet_to_compare_number = False
                    buff = self.tuple_append(root, i)
                    self.list_item_not_found(a[i], "a", buff)

                if not counts_b[i][0]:
                    if not printdiff: return False
                    neet_to_compare_number = False
                    buff = self.tuple_append(root, i)
                    self.list_item_not_found(b[i], "b", buff)

            if neet_to_compare_number:
                for i in range(len(counts_a)):
                    counta, place = counts_a[i]
                    countb = counts_b[place][0]
                    if countb != counta and counts_b[place][1] == i:  # 后者用来去重，精简输出
                        if not printdiff: return False
                        self.list_freq_not_match(root, i, place, a[i], counta, countb)

        # 能走到这里说明比较无误
        if not printdiff: return True

    def dict_comp(self, a, b, root, printdiff):
        self.turn_dict_keys_to_unicode(a)
        self.turn_dict_keys_to_unicode(b)

        ak = a.keys()  # 再次刷新
        bk = b.keys()
        diffak = [x for x in ak if x not in bk]
        diffbk = [x for x in bk if x not in ak]
        if diffak:
            if not printdiff: return False
            self.dict_key_not_found(diffak, "a", root)
        if diffbk:
            if not printdiff: return False
            self.dict_key_not_found(diffbk, "b", root)
        samekeys = [x for x in ak if x in bk]

        for key in samekeys:
            buff = self.tuple_append(root, key)
            if self.common_comp(a[key], b[key], buff, printdiff) == False:
                return False

        if not printdiff: return True

    def common_comp(self, a, b, root=(), printdiff=True):
        a = self.to_unicode_if_string(a)
        b = self.to_unicode_if_string(b)

        if type(a) != type(b):
            if not printdiff: return False
            self.different_type(a, b, root)
            return

        if type(a) not in [dict, list]:

            if a != b:  # the real compare
                if not printdiff: return False
                self.different_value(a, b, root)
            elif not printdiff:
                return True
            return

        if type(a) == list:
            return self.list_comp(a, b, root, printdiff)

        if type(a) == dict:
            return self.dict_comp(a, b, root, printdiff)

        raise TypeError  # , "shouldn't be here"

    def escape(self, s):  # 清晰打印字典、列表中的中文，由UtilService.py内函数简化
        if r'\x' in s:
            s = s.decode('string-escape')
        if r'\u' in s:
            s = s.decode('unicode-escape')
        if type(s) == str:
            s = s.decode('utf-8')  # 服务器端，不用担心
        return s

    def compare(self, a, b, ignore_list_seq=True):  # the enternce
        flag = False
        c = d = None

        if type(a) in [str]:
            c = json.loads(a)  # 字典格式、列表格式的字符串，请自行使用eval
            flag = True
        if type(b) in [str]:
            d = json.loads(b)
            flag = True
        if flag:
            return self.compare(c, d, ignore_list_seq)

        try:
            json.dumps(a, ensure_ascii=False)
            json.dumps(b, ensure_ascii=False)
        except:
            raise TypeError  # , "unsupported types"

        self.res = True
        self.ignore_list_seq = ignore_list_seq

        if self.print_before:
            print("")  # self.escape("a is {}".format(a)))
            print("")  # self.escape("b is {}".format(b)))

        self.common_comp(a, b)
        return self.res


if __name__ == '__main__':
    def longline():
        print("-" * 120)


    cp = JCompare()

    a = {"姓名": "王大锤"}
    b = {u"姓名": u"王大锤"}
    print(cp.compare(a, b))

    longline()

    a = [[1, 2, 3], [4, 5, 6]]
    b = [[6, 5, 4], [3, 2, 1]]
    print(cp.compare(a, b))

    longline()

    a = {"a": 1, "b": 3, "c": False, "d": "ok"}
    b = {"a": 1, "b": 2, "c": "False", "e": "ok"}
    print(cp.compare(a, b))

    longline()

    a = {"a": [1, {"k": "ok"}]}
    b = {"a": [1, {"k": "error"}]}
    print(cp.compare(a, b))

    longline()

    print(cp.compare(a, b, ignore_list_seq=False))

    longline()

    a = {"rtn": 0, "msg": "ok"}
    b = {"rtn": 1, "msg": "用户名不存在"}
    print(cp.compare(a, b))

    longline()

    a = u'{"body":{"text":"你好"}}'
    b = '{"body":{"text":"你好啊"}}'
    print(cp.compare(a, b))

    longline()

    a = [1, 2, 2]
    b = [1, 1, 2]
    print(cp.compare(a, b))
