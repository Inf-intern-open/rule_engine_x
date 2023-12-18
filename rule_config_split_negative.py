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
            if item['rule_type'] == 'abnormal_quantifiable_rule':
                try:
                    if item['operator']=='>' or item['operator']=='≥':
                        a=item['value']
                    else:
                        b=item['value']
                except Exception as e:
                    pass
                # print(a, b)
                item['value'] = random.uniform(b,500)

        else:
            try:
                if item['rule_type']=='abnormal_quantifiable_rule':
                    if item['operator']=='>' or item['operator']=='≥':
                        item['value'] = random.uniform(-10, item['value'])

                    else:
                        item['value'] = random.uniform(item['value'], 500)
                if item['rule_type'] == 'abnormal_text_rule':
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

l=[]
with open('C:/Users/ThinkPad/Desktop/rule_config_split_1.jsonl', 'r', encoding="utf-8") as f:

    for line in f:
        dic={}
        data = json.loads(line)
        if 'grade' in data:
            dic['grade']=data['grade']
        dic['data']=delet(change_value(handle_rule_detail(data['rule_detail'])))
        l.append(dic)
        print(dic)
with open(os.path.join('./', 'rule_config_split_negative_case.jsonl'), 'w', encoding='utf-8') as jsonl_file:
    for item in l:
        json.dump(item, jsonl_file, ensure_ascii=False)
        jsonl_file.write('\n')  # 添加换行符




