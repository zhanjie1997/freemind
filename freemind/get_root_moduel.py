a = "1234567877877678785676767676766665678786786767767777756777667656656634563456787878787878566756678867777776567234556675677788767887891011119107565667677567675665645677878787867756788910111212101178886566654567766665667678677677734"
b = "12345678/7/78/7/7/678/78/567/67/67/67/67/6/6/6/6/5678/78/678/67/67/7/67/7/7/7/7/567/7/7/6/67/6/56/6/56/6/345/"
c = "1234567877877678785676767676766789"
flag = 0
data_string = ""
list_data = []
for i in range(len(c)):
    #print(a[i])
    if i == 0:
        data_string = a[i]
    elif i == len(c)-1:
        if int(a[i])>int(a[i-1]):
            data_string += a[i]
            list_data.append(data_string)
        else:
            data_string = a[i]
            list_data.append(data_string)
    else:
        num_now = int(a[i])
        num_before = int(a[i-1])
        num_after =int(a[i+1])
        if num_before<=num_now<num_after:
            data_string += a[i]
        elif (num_now>=num_after):
            data_string += a[i]
            list_data.append(data_string)
            data_string = ""
        else:
            data_string =a[i]
        if  flag<num_now:
            flag = num_now
print(list_data)
def get_tree(data):
    flag = 0
    data_string = ""
    list_data = []
    for i in range(len(data)):
        # print(a[i])
        if i == 0:
            data_string = a[i]
        else:
            num_now = int(a[i])
            num_before = int(a[i - 1])
            if num_now > num_before:
                data_string += a[i]
            else:
                if data_string == "":
                    data_string = a[i]
                    list_data.append(data_string)
                else:
                    list_data.append(data_string)
                print(data_string)
                data_string = ""
            if flag < num_now:
                flag = num_now

