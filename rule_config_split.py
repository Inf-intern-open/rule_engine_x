import pandas as pd
import classify
import json
import os


l1=[]
with open('C:/Users/ThinkPad/Desktop/rule_config_split_1.jsonl', 'r', encoding="utf-8") as f:
    for line in f:
        dic={}
        data = json.loads(line)
        if 'grade' in data:
            dic['grade']=data['grade']
        dic['data']=classify.positive_cases(data['rule_detail'])
        l1.append(dic)
        # print(dic)
with open(os.path.join('./', 'rule_config_split_positive_case.jsonl'), 'w', encoding='utf-8') as jsonl_file:
    for item in l1:
        json.dump(item, jsonl_file, ensure_ascii=False)
        jsonl_file.write('\n')  # 添加换行符

l2=[]
with open('C:/Users/ThinkPad/Desktop/rule_config_split_1.jsonl', 'r', encoding="utf-8") as f:
    for line in f:
        dic={}
        data = json.loads(line)
        if 'grade' in data:
            dic['grade']=data['grade']
        dic['data']=classify.positive_cases(data['rule_detail'])
        l2.append(dic)
        # print(dic)
with open(os.path.join('./', 'rule_config_split_negative_case.jsonl'), 'w', encoding='utf-8') as jsonl_file:
    for item in l2:
        json.dump(item, jsonl_file, ensure_ascii=False)
        jsonl_file.write('\n')  # 添加换行符


