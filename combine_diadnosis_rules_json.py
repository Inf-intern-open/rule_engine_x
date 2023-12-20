from itertools import combinations
import pandas as pd
import classify
import json
import os

l1=[]
with open('C:/Users/ThinkPad/Downloads/diagnosis_rules_json.jsonl', 'r', encoding="utf-8") as f:
    for line in f:
        dic={}
        data = json.loads(line)
        dic['diagnosis']=data['diagnosis']
        dic['rule_detail']=data['rule_detail']
        l1.append(dic)

    for num in range(27,len(l1)):
        dic_res={}
        l_combinelist_diadnosis = []
        l_combinelist_result = []
        for element in combinations(l1, num):
            for dict in element:
                l_combinelist_diadnosis+=element['diagnosis']
                l_combinelist_result+=classify.positive_cases(element['rule_detail'])
            print(element)
        dic_res['diagnosis']=l_combinelist_result
        dic_res['rule_detail']=l_combinelist_result


# with open(os.path.join('./', 'diagnosis_rules_json_positive_case.jsonl'), 'w', encoding='utf-8') as jsonl_file:
#     for item in l1:
#         json.dump(item, jsonl_file, ensure_ascii=False)
#         jsonl_file.write('\n')
#
# l2=[]
# with open('C:/Users/ThinkPad/Downloads/diagnosis_rules_json.jsonl', 'r', encoding="utf-8") as f:
#     for line in f:
#         try:
#             dic={}
#             data = json.loads(line)
#             dic['diagnosis']=data['diagnosis']
#             dic['data']=classify.negative_cases(data['rule_detail'])
#             l2.append(dic)
#             # print(dic)
#         except Exception as e:
#             pass
# with open(os.path.join('./', 'diagnosis_rules_json_negative_case.jsonl'), 'w', encoding='utf-8') as jsonl_file:
#     for item in l2:
#         json.dump(item, jsonl_file, ensure_ascii=False)
#         jsonl_file.write('\n')


















