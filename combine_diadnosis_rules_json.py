from itertools import combinations
import pandas as pd
import classify
import json
import os
import rule_detail
l1=[]
l1_res=[]
with open('C:/Users/ThinkPad/Downloads/diagnosis_rules_json.jsonl', 'r', encoding="utf-8") as f:
    for line in f:
        dic={}
        data = json.loads(line)
        dic['diagnosis']=data['diagnosis']
        dic['rule_detail']=data['rule_detail']
        l1.append(dic)

    for num in range(28,len(l1)):
        print(len(l1))
        for element in combinations(l1, num):
            dic_res = {}
            l_combinelist_diadnosis = []
            l_combinelist_result = []
            print(element)
            print(0)
            for dict in element:
                print(dict)
                try:
                    l_combinelist_diadnosis.append(dict['diagnosis'])
                    l_combinelist_result+=classify.positive_cases(dict['rule_detail'])
                except Exception as e:
                    pass
            print('****************************')
            print(l_combinelist_result)
            print(l_combinelist_diadnosis)
            print('****************************')
            # for mylist in l_combinelist_result:
            #     print(mylist)
            #     if 'value' in mylist:
            #         if rule_detail.count_occurrences(l_combinelist_result,mylist['entity']) >= 2:
            #             break
            #         break
            for mylist in l_combinelist_result:
                if rule_detail.count_occurrences(l_combinelist_result,mylist['entity']) >= 2:
                    l_combinelist_result.remove(mylist)
            for mylist in l_combinelist_result:
                if rule_detail.count_occurrences(l_combinelist_result, mylist['entity']) >= 2:
                    l_combinelist_result.remove(mylist)
            for mylist in l_combinelist_result:
                if rule_detail.count_occurrences(l_combinelist_result, mylist['entity']) >= 2:
                    l_combinelist_result.remove(mylist)
            dic_res['diagnosis']=l_combinelist_diadnosis
            dic_res['data']=l_combinelist_result
            l1_res.append(dic_res)
            print('#############################')
            print(dic_res)
            print('#############################')

with open(os.path.join('./', 'combine_diagnosis_rules_json_positive_case.jsonl'), 'w', encoding='utf-8') as jsonl_file:
    for item in l1_res:
        json.dump(item, jsonl_file, ensure_ascii=False)
        jsonl_file.write('\n')

l2 = []
l2_res = []
with open('C:/Users/ThinkPad/Downloads/diagnosis_rules_json.jsonl', 'r', encoding="utf-8") as f:
    for line in f:
        dic = {}
        data = json.loads(line)
        dic['diagnosis'] = data['diagnosis']
        dic['rule_detail'] = data['rule_detail']
        l2.append(dic)

    for num in range(28, len(l2)):
        print(len(l2))
        for element in combinations(l2, num):
            dic_res = {}
            l_combinelist_diadnosis = []
            l_combinelist_result = []
            # print(element)
            # print(0)
            for dict in element:
                # print(dict)
                try:
                    l_combinelist_diadnosis.append(dict['diagnosis'])
                    l_combinelist_result += classify.negative_cases(dict['rule_detail'])
                except Exception as e:
                    pass
            # print('****************************')
            # print(l_combinelist_result)
            # print(l_combinelist_diadnosis)
            # print('****************************')
            #     for mylist in l_combinelist_result:
            #         if 'value' in mylist:
            #             if rule_detail.count_occurrences(l_combinelist_result, mylist['entity']) >= 2:
            #                 break
            #             break
            for mylist in l_combinelist_result:
                if rule_detail.count_occurrences(l_combinelist_result, mylist['entity']) >= 2:
                    l_combinelist_result.remove(mylist)
            for mylist in l_combinelist_result:
                if rule_detail.count_occurrences(l_combinelist_result, mylist['entity']) >= 2:
                    l_combinelist_result.remove(mylist)
            for mylist in l_combinelist_result:
                if rule_detail.count_occurrences(l_combinelist_result, mylist['entity']) >= 2:
                    l_combinelist_result.remove(mylist)
            dic_res['diagnosis'] = l_combinelist_diadnosis
            dic_res['data'] = l_combinelist_result
            l2_res.append(dic_res)
            # print('#############################')
            # print(dic_res)
            # print('#############################')

with open(os.path.join('./', 'combine_diagnosis_rules_json_negative_case.jsonl'), 'w',
          encoding='utf-8') as jsonl_file:
    for item in l2_res:
        json.dump(item, jsonl_file, ensure_ascii=False)
        jsonl_file.write('\n')



    # with open(os.path.join('./', 'combine_diagnosis_rules_json_negative_case.jsonl'), 'w',
    #           encoding='utf-8') as jsonl_file:
    #     for item in l1_res:
    #         json.dump(item, jsonl_file, ensure_ascii=False)
    #         jsonl_file.write('\n')

















