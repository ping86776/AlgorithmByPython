import json
import random
# 给定一个json字符串，把指定key的value替换成给定数字。
json_txt = """
{
  "header":{
    "funcNo": "IF010002",
    "opStation": "11.11.1.1",
    "appId": "aaaaaa",
    "deviceId": "kk",
    "ver":"wx-1.0",
    "channel": "4"
  },
  "payload": {
    "mobileTel": "13817120001"
  }
}
"""
date_json = json.loads(json_txt)
print(date_json)
print("*" * 100)
# 遍历json文件所有的key对应的value
# 替换的数字
data = [1,2,3,4,5]


def json_txt(dic_json):
    if isinstance(dic_json, dict):  # 判断是否是字典类型isinstance 返回True false
        for key in dic_json:
            if isinstance(dic_json[key], dict):  # 如果dic_json[key]依旧是字典类型
                print(dic_json[key])
                for value in dic_json[key]:
                    # print(dic_json[key][value])
                    dic_json[key][value] = data[random.randint(0, 4)]
                    # print(dic_json)
            else:
                break
        return dic_json

res = json_txt(date_json)
print("替换后 :", str(res))