import datetime
import time


def convert_to_json(result, key_list):
    result_list = []
    for temp in range(len(result)):
        res_dic = {}
        for index in range(len(key_list)):
            res_dic[key_list[index]] = result[temp][index]
        result_list.append(res_dic)
    return result_list


def convert_to_data(timeStamp):
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
    return otherStyleTime


