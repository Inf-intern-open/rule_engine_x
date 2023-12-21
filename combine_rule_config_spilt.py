from itertools import combinations
import pandas as pd
import classify
import json
import os
import rule_detail
l1=[]
l1_res=[]
with open('C:/Users/ThinkPad/Desktop/rule_config_split_1.jsonl', 'r', encoding="utf-8") as f:
    for line in f:
        dic={}
        data = json.loads(line)
        if 'grade' in data:
            dic['grade']=data['grade']
        dic['rule_detail']=data['rule_detail']
        l1.append(dic)
    x=0
    for num in range(10,1,-1):
        for element in combinations(l1, num):
            dic_res = {}
            l_combinelist_diadnosis = []
            l_combinelist_result = []
            print(element)
            print(0)
            l_temp=[]
            for dict in element:
                print(dict)
                try:
                    key=classify.positive_cases(dict['rule_detail'])
                    l_combinelist_result += key

                except Exception as e:
                    pass
            print('****************************')
            print(l_combinelist_result)

            print('****************************')
            for mylist in l_combinelist_result:
                if rule_detail.count_occurrences(l_combinelist_result,mylist['entity']) >= 2:
                    l_combinelist_result.remove(mylist)
            for mylist in l_combinelist_result:
                if rule_detail.count_occurrences(l_combinelist_result, mylist['entity']) >= 2:
                    l_combinelist_result.remove(mylist)
            for mylist in l_combinelist_result:
                if rule_detail.count_occurrences(l_combinelist_result, mylist['entity']) >= 2:
                    l_combinelist_result.remove(mylist)


            dic_res['data']=l_combinelist_result
            l1_res.append(dic_res)
            print('#############################')
            print(dic_res)
            print('#############################')
            x+=1
            print('x',x)
            if x==4000:
                break
        if x == 4000:
            break

with open(os.path.join('./', 'combine_rule_config_split_positive_case.jsonl'), 'w', encoding='utf-8') as jsonl_file:
    for item in l1_res:
        json.dump(item, jsonl_file, ensure_ascii=False)
        jsonl_file.write('\n')

l2 = []
l2_res = []
with open('C:/Users/ThinkPad/Downloads/diagnosis_rules_json.jsonl', 'r', encoding="utf-8") as f:
    for line in f:
        dic = {}
        data = json.loads(line)
        if 'grade' in data:
            dic['grade']=data['grade']
        dic['rule_detail']=data['rule_detail']
        l2.append(dic)
    print(len(l2))
    y = 0
    for num in range( 10,1,-1):
        for element in combinations(l2, num):
            dic_res = {}
            l_combinelist_diadnosis = []
            l_combinelist_result = []
            # print(element)
            # print(0)
            for dict in element:
                print(dict)
                try:
                    # l_combinelist_diadnosis.append(dict['diagnosis'])
                    l_combinelist_result += classify.negative_cases(dict['rule_detail'])
                except Exception as e:
                    pass
            print('@@@@@@@',l_combinelist_result)
            for mylist in l_combinelist_result:
                if rule_detail.count_occurrences(l_combinelist_result,mylist['entity']) >= 2:
                    print(mylist['entity'])
                    l_combinelist_result.remove(mylist)
                    print(mylist)
            for mylist in l_combinelist_result:
                if rule_detail.count_occurrences(l_combinelist_result,mylist['entity']) >= 2:
                    print(mylist['entity'])
                    l_combinelist_result.remove(mylist)
                    print(mylist)


            print(l_combinelist_result)
            # print('****************************')
            # print(l_combinelist_result)
            # print(l_combinelist_diadnosis)
            # print('****************************')
            # for mylist in l_combinelist_result:
            #     if rule_detail.count_occurrences(l_combinelist_result,mylist['entity']) >= 2:
            #         print('chongfu',mylist['entity'])
            #         break
            #     break
            # dic_res['diagnosis'] = l_combinelist_diadnosis
            dic_res['data'] = l_combinelist_result
            l2_res.append(dic_res)
            # print('#############################')
            # print(dic_res)
            # print('#############################')
            y+=1
            print('y',y)
            if y==400:
                break
        if y == 400:
            break

with open(os.path.join('./', 'combine_rule_config_split_negative_case.jsonl'), 'w',
          encoding='utf-8') as jsonl_file:
    for item in l2_res:
        json.dump(item, jsonl_file, ensure_ascii=False)
        jsonl_file.write('\n')



    # with open(os.path.join('./', 'combine_diagnosis_rules_json_negative_case.jsonl'), 'w',
    #           encoding='utf-8') as jsonl_file:
    #     for item in l1_res:
    #         json.dump(item, jsonl_file, ensure_ascii=False)
    #         jsonl_file.write('\n')

















