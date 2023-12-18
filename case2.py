
json_dict = {'any': [
    {'all': [{'rule_type': 'abnormal_quantifiable_rule', 'entity': '收缩压', 'operator': '≥', 'value': 160, 'unit': 'mmHg'},
             {'rule_type': 'abnormal_quantifiable_rule', 'entity': '收缩压', 'operator': '≤', 'value': 179, 'unit': 'mmHg'}]},
    {'all': [{"any":[{} ,{}]}]}
    ]
}


[
    {'all': [{'rule_type': 'abnormal_quantifiable_rule', 'entity': '收缩压', 'operator': '≥', 'value': 160, 'unit': 'mmHg'},
             {'rule_type': 'abnormal_quantifiable_rule', 'entity': '收缩压', 'operator': '≤', 'value': 179, 'unit': 'mmHg'}]}]


[{'rule_type': 'abnormal_quantifiable_rule', 'entity': '收缩压', 'operator': '≥', 'value': 160, 'unit': 'mmHg'},
             {'rule_type': 'abnormal_quantifiable_rule', 'entity': '收缩压', 'operator': '≤', 'value': 179, 'unit': 'mmHg'}]



[{"any":[{} ,{}]}]

json_dict1={'any': [{'rule_type': 'abnormal_quantifiable_rule', 'entity': '随机血糖', 'operator': '≥', 'value': 11.1, 'unit': 'mmol/L'}, {'rule_type': 'abnormal_quantifiable_rule', 'entity': '空腹血糖', 'operator': '≥', 'value': 7, 'unit': 'mmol/L'}, {'rule_type': 'abnormal_quantifiable_rule', 'entity': '2小时血糖', 'operator': '≥', 'value': 11.1, 'unit': 'mmol/L'}]}
json_dict2={'all': [{'rule_type': 'abnormal_text_rule', 'entity': '弥漫性肝脏密度降低', 'operator': 'has'}, {'rule_type': 'abnormal_quantifiable_rule', 'entity': '肝/脾CT比值', 'operator': '≤', 'value': 1}, {'rule_type': 'abnormal_quantifiable_rule', 'entity': '肝/脾CT比值', 'operator': '>', 'value': 0.7}]}
json_dict7={'all': [{'rule_type': 'abnormal_quantifiable_rule', 'entity': '血白细胞计数', 'operator': '>', 'value': 15, 'unit': '×10^9/L'}, {'rule_type': 'abnormal_quantifiable_rule', 'entity': '中性粒细胞百分比', 'operator': '>', 'value': 90, 'unit': '%'}, {'any': [{'rule_type': 'abnormal_text_rule', 'entity': '肝脏超声包含液性回声暗区', 'operator': 'has'}, {'rule_type': 'abnormal_text_rule', 'entity': '肝脏超声包含脓肿内液平面', 'operator': 'has'}]}]}
json_dict11={'any': [{'all': [{'rule_type': 'abnormal_quantifiable_rule', 'entity': '收缩压', 'operator': '≥', 'value': 160, 'unit': 'mmHg'}, {'rule_type': 'abnormal_quantifiable_rule', 'entity': '收缩压', 'operator': '≤', 'value': 179, 'unit': 'mmHg'}]}, {'all': [{'rule_type': 'abnormal_quantifiable_rule', 'entity': '舒张压', 'operator': '≥', 'value': 100, 'unit': 'mmHg'}, {'rule_type': 'abnormal_quantifiable_rule', 'entity': '舒张压', 'operator': '≤', 'value': 109, 'unit': 'mmHg'}]}]}
json_dict3={'all': [{'rule_type': 'abnormal_quantifiable_rule', 'entity': '弥漫性肝脏密度降低', 'operator': 'is', 'value': True}, {'rule_type': 'abnormal_quantifiable_rule', 'entity': '肝/脾CT比值', 'operator': '≤', 'value': 0.5}]}
json_dict16={'partial': {'at_least': 3, 'rules': [{'rule_type': 'abnormal_quantifiable_rule', 'entity': '体重指数', 'operator': '≥', 'value': 25}, {'any': [{'rule_type': 'abnormal_quantifiable_rule', 'entity': '空腹血糖', 'operator': '≥', 'value': 6.1, 'unit': 'mmol/L'}, {'rule_type': 'abnormal_quantifiable_rule', 'entity': '2小时血糖', 'operator': '≥', 'value': 7.8, 'unit': 'mmol/L'}, {'rule_type': 'abnormal_text_rule', 'entity': '糖尿病'}]}, {'any': [{'rule_type': 'abnormal_quantifiable_rule', 'entity': '收缩压', 'operator': '≥', 'value': 140, 'unit': 'mmHg'}, {'rule_type': 'abnormal_quantifiable_rule', 'entity': '舒张压', 'operator': '≥', 'value': 90, 'unit': 'mmHg'}, {'rule_type': 'abnormal_text_rule', 'entity': '高血压'}]}, {'any': [{'rule_type': 'abnormal_quantifiable_rule', 'entity': '甘油三酯', 'operator': '≥', 'value': 1.7, 'unit': 'mmol/L'}, {'all': [{'rule_type': 'normal_quantifiable_rule', 'entity': '性别', 'operator': 'is', 'value': '男'}, {'rule_type': 'abnormal_quantifiable_rule', 'entity': '高密度脂蛋白', 'operator': '<', 'value': 0.9, 'unit': 'mmol/L'}]}, {'all': [{'rule_type': 'normal_quantifiable_rule', 'entity': '性别', 'operator': 'is', 'value': '女'}, {'rule_type': 'abnormal_quantifiable_rule', 'entity': '高密度脂蛋白', 'operator': '<', 'value': 1, 'unit': 'mmol/L'}]}]}]}}
json_dict13={'all': [{'any': [{'rule_type': 'abnormal_text_rule', 'entity': '乳腺增生性疾病类别', 'operator': 'is', 'value': '1类'}, {'rule_type': 'abnormal_text_rule', 'entity': '乳腺增生性疾病类别', 'operator': 'is', 'value': '2类'}, {'rule_type': 'abnormal_text_rule', 'entity': '乳腺增生性疾病类别', 'operator': 'is', 'value': '3类'}, {'rule_type': 'abnormal_text_rule', 'entity': '乳腺增生性疾病类别', 'operator': 'is', 'value': '4类'}], 'rule_type': 'abnormal_text_rule', 'entity': '乳腺增生性疾病边界清楚'}]}


import json
import random
from typing import List
import os
def load_json(str):
    str = str.replace("'", '"')
    dic = json.loads(str)
    return dic

def get_subset4(mylist):
    output = [[]]
    for num in mylist:
        output += [curr + [num] for curr in output]
    output = [ele for ele in output if ele != []]
    num_random = random.randint(0, len(output) - 1)
    terminal_random_output = output[num_random]
    return terminal_random_output

def get_subset(rules: List[dict]) -> List[dict]:
    return get_subset4(rules)

def handle_rule(rule:dict):
    return rule

def handle_any(rules: List[dict]): # [{} ,{}]
    sub_rules = get_subset(rules) # [{} ,{}],      [{}]

    result = handle_all(sub_rules)

    return result

def handle_all(rules: List[dict]): #  # [{} ,{}]
    result = []
    # print(rules)
    try:
        for rule in rules: # {}
            if 'all' in rule:
                res_list = handle_all(rule['all'])
                result.extend(res_list)
            elif 'any' in rule:
                res_list = handle_any(rule['any']) # [{} ,{}]
                result.extend(res_list)
            else:
                res = handle_rule(rule)
                result.append(res)
    except Exception as e:
        pass
    return result

def handle_rule_detail(rule_detail:dict):
    if 'all' in rule_detail:
        res_list = handle_all(rule_detail['all'])
        # print(res_list)
    elif 'any' in rule_detail:
        # print(0)
        res_list = handle_any(rule_detail['any'])
    # print(res_list)
    return res_list

def count_occurrences(mylist, value):
    count = 0
    for i in mylist:
        for j in i.values():
            if j == value:
                count += 1
    return count

def change_value(mylist):
    a, b = 0, 0
    for item in mylist:
        if count_occurrences(mylist, item['entity']) == 2:
            try:
                if item['operator']=='>' or item['operator']=='≥':
                    a=item['value']
                else:
                    b=item['value']
            except Exception as e:
                pass
            item['value'] = random.uniform(b,500)
        else:
            try:
                if item['rule_type']=='abnormal_quantifiable_rule':
                    if item['operator']=='>' or item['operator']=='≥':
                        item['value'] = random.uniform(-10, item['value'])
                    else:

                        item['value'] = random.uniform(item['value'], 500)
                if item['rule_type'] == 'abnormal_quantifiable_rule':
                    continue
            except Exception as e:
                pass

    return mylist

def delet(mylist):
    for item in mylist:
        if count_occurrences(mylist, item['entity']) == 2:
            mylist.remove(item)
    try:
        for elment in mylist:
            del elment['rule_type']
            del elment['operator']
    except Exception as e:
        pass
    return mylist

# def rule_detail_partial(rule_detail:dict):
#     detail=rule_detail['partial']['rules']
#     return detail
# handle_rule_detail(json_dict)

import pandas as pd
df=pd.read_excel('C:/Users/ThinkPad/AppData/Local/Temp/Rar$DIa12632.49208/诊断规则.xlsx')
res_l=[]
c=0
for i in df['规则明细json']:
    i=load_json(i)
    try:
        res_l.append(delet(change_value(handle_rule_detail(i))))
    except Exception as e:
        pass
    with open(os.path.join('./', 'negative_case.jsonl'), 'w', encoding='utf-8') as jsonl_file:
        for item in res_l:
            json.dump(item, jsonl_file, ensure_ascii=False)
            jsonl_file.write('\n')  # 添加换行符，分隔每个 JSON 对象
    print(c)
    c+=1






