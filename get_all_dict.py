#global dict_all
dict_all = []
yes = 0
no = 1
flag = 1
def get_all_dict(dict_data):
    if type(dict_data) == dict:
        dict_all.append(dict_data)
        for key in dict_data.keys():
            #print(key)
            get_all_dict(dict_data[key])
            pass
    elif type(dict_data) == list:
        for data in dict_data:
            #print(data)
            get_all_dict(data)
        pass
    else:
        #print("结果:",dict_all,len(dict_all))
        return dict_all
def cmp_dict(dict_sun,dict_father):
    if big_dict(dict_sun,dict_father):
        dict_sun, dict_father = dict_father,dict_sun
    if type(dict_sun) == dict and type(dict_father) == dict:
        sun_key = list(dict_sun.keys())
        father_key = list(dict_father.keys())
        #print(sun_key,father_key)
        sun_key_copy = sun_key[:]
        for key1 in father_key:
            for key2 in sun_key:
                if key1 == key2:
                    sun_key.remove(key1)
        if sun_key == []:
            print("字典key一致",sun_key_copy)
            for value in sun_key_copy:
                re_flag = cmp_dict(dict_sun[value],dict_father[value])
                if re_flag == yes:
                    return re_flag
        else:
            print("字典key值不一致")
            flag = yes
            return flag
    elif type(dict_sun) == list and type(dict_father) == list:
        #print(dict_father,dict_sun)
        if len(dict_father) == len(dict_sun):
            for data in dict_father:
                for data_sun in dict_sun:
                    if data_sun == data:
                        dict_sun.remove(data)
            if dict_sun == []:
                print(dict_sun)
                print("列表数据一致")
            else:
                print("dict_father:",dict_sun)
                print("列表数据不一致")
                flag = yes
                return flag
        else:
            print("列表元素数量不一致",len(dict_father) ,len(dict_sun))
            flag = yes
            return flag
    elif type(dict_sun) == str and type(dict_father) == str:
        if dict_sun == dict_father:
            print("字符一致",dict_father,dict_sun)
        else:
            print("字符不一致")
            flag = yes
            return flag
    elif type(dict_sun) == int and type(dict_father) == int:
        if dict_sun == dict_father:
            print("整型一致")
        else:
            print("整型不一致",dict_father,dict_sun)
            flag = yes
            return flag
    elif type(dict_sun) == float and type(dict_father) == float:
        if dict_sun == dict_father:
            print("浮点型一致")
        else:
            print("浮点型不一致",dict_father,dict_sun)
            flag = yes
            return flag
    elif type(dict_sun) == bool and type(dict_father) == bool:
        if dict_sun == dict_father:
            print("布尔值一致")
        else:
            print("布尔值不一致",dict_father,dict_sun)
            flag = yes
            return flag
    else:
        print("类型不一致")
        flag = yes
        return flag
def big_dict(data,data2):
    one = len(str(data))
    two = len(str(data2))
    if one >= two:
        return 1
    else:
        return 0
all = {
    'car':{
        'color':['red','yellow','black',{
                    'color':['red','yellow','black'],
                    'money':11111,
                    'pailaing':'2.5L'
                }],
        'money':11111,
        'pailaing':'2.5L',
        'name':'BMW'
    },
    'car1':{
        'color':['red','yellow','black'],
        'money':True,
        'pailaing':'2.5L',
        'country':'china',
        'car1:car2':{
                    'color':['red','yellow','black'],
                    'money':11111,
                    'pailaing':'2.5L'
                }
    },
    'car2':{
        'color':['red','yellow','black'],
        'money':2222,
        'pailaing':'2.5L'
    }
}
sun =  {
    'car1':{
        'color':['red','yellow','black'],
        'money':True,
        'pailaing':'2.5L',
        'country':'china',
}}
def if_in_dict(one,all):
    get_all_dict(all)
    #print(dict_all)
    print(" 子字典",one,'\n',"父字典",all)
    for di in dict_all:
        print("第", dict_all.index(di) + 1,"次循环", one,'\n', di)
        y = cmp_dict(one, di)
        #print(y)
        if y is None:
            #print("存在包含关系", one, di)
            return 1
        else:
            print("不存在包含关系", one, di)
have = if_in_dict(sun,all)
if have:
    print("存在")
else:
    print("不存在")
print(type(False))