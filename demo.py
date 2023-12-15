from jsonpath import jsonpath
import json
import random
for i in range(2):

    s = "[{'all': [{'rule_type': 'abnormal_quantifiable_rule', 'entity': '血白细胞计数', 'operator': '>', 'value': 15, 'unit': '×10^9/L'}, {'rule_type': 'abnormal_quantifiable_rule', 'entity': '中性粒细胞百分比', 'operator': '>', 'value': 90, 'unit': '%'}, {'any': [{'rule_type': 'abnormal_text_rule', 'entity': '肝脏超声包含液性回声暗区', 'operator': 'has'}, {'rule_type': 'abnormal_text_rule', 'entity': '肝脏超声包含脓肿内液平面', 'operator': 'has'}]}]}]"
    s = s.replace("'", '"')
    s = json.loads(s)

    s1="[{'any': [{'all': [{'rule_type': 'abnormal_quantifiable_rule', 'entity': '收缩压', 'operator': '≥', 'value': 160, 'unit': 'mmHg'}, {'rule_type': 'abnormal_quantifiable_rule', 'entity': '收缩压', 'operator': '≤', 'value': 179, 'unit': 'mmHg'}]}, {'all': [{'rule_type': 'abnormal_quantifiable_rule', 'entity': '舒张压', 'operator': '≥', 'value': 100, 'unit': 'mmHg'}, {'rule_type': 'abnormal_quantifiable_rule', 'entity': '舒张压', 'operator': '≤', 'value': 109, 'unit': 'mmHg'}]}]},{'any':1}]"
        # ijson=str(ijson)
    s1 = s1.replace("'", '"')
    s1 = json.loads(s1)
    # print(s1)
    # print(jsonpath(s1, '$..any'))


    # print(jsonpath(s1, '$..all'))

    def get_subset4(mylist):
        output = [[]]
        for num in mylist:
            output += [curr + [num] for curr in output]
        output = [ele for ele in output if ele != []]
        num_random = random.randint(0, len(output)-1)
        terminal_random_output=output[num_random]
        return terminal_random_output

    def handle_all_rule(a):
        a=jsonpath(a, '$..all')
        return a
    b1=handle_all_rule(s)
    # print(b1)


    def handle_any_rule(a):
        a=jsonpath(a, '$..any')
        a=handle_all_rule(a)
        return a

    def handle_any_rule_1(a):
        a=jsonpath(a, '$..any')
        # a=handle_all_rule(a)
        return a

    b1_1=handle_any_rule_1(b1)
    # print(b1_1)

    # print(handle_any_rule(s1))

    def handle_any(mylsit):   #-> List[Entity]
        return get_subset4(mylsit)
        # call handle_any()
        # call handle_all()
        # call handle_atomic_rule()
        pass

    def handle_all(a1):
        l_all=[]
        for i in a1:
            for j in i:

                if 'any' not in j.keys():
                    try:
                        if j['value'] != None:
                            if j['operator'] == '>' or j['operator'] == '≥':
                                j['value'] = random.randint(j['value'] + 1, 200)
                            else:
                                j['value'] = random.randint(0, j['value'] - 1)
                    except Exception as e:
                        pass
                    l_all.append(j)
        return l_all
    def handle_all_1(a1):
        l_all=[]
        for i in a1:
            for j in i:
                if 'any' not in j.keys():
                    try:
                        if j['value'] != None:
                            if j['entity'] == '收缩压' :
                                j['value'] = random.randint(j['value'] , 179)
                            # else:
                            #     j['value'] = random.randint(0, j['value'] - 1)
                            if j['entity'] == '舒张压':
                                j['value'] = random.randint(j['value'], 109)
                            # else:
                            #     j['value'] = random.randint(0, j['value'] - 1)
                    except Exception as e:
                        pass
                    l_all.append(j)
        return l_all


    # print(handle_any(handle_any_rule(s1)))
    a1=handle_any(handle_any_rule(s1))
    # print(len(handle_all(a1)))
    def delet(l):
        l_1 = []
        for i in l:
            del i['rule_type']
            del i['operator']
            l_1.append(i)
        return [l_1]
    b1_11=handle_all(b1)
    b1_12=handle_any(b1_1)
    for i in b1_12:
        for j in i :
            b1_11.append(j)
    l_sec=delet(b1_11)
    # print(l_sec)
    # print(handle_all(a1))
    l_fir=delet(handle_all_1(a1))
    # print(l_fir[0][1])
    for i in l_fir:
        for j in i:
            if '收缩压' in j.values():
                del l_fir[0][1]
            if '收缩压' in j.values() and '舒张压' in j.values():
                del l_fir[0][3]
            if '舒张压' in j.values():
                del l_fir[0][1]
                # print(j)
    # l_sec=
    # l_last=l_fir+l_sec
    # print(l_last)
    l_last=[]
    for i in l_sec:
        for j in i:
            l_last.append(j)
    for i in l_fir:
        for j in i:
            l_last.append(j)
    # l_last=l_fir+l_sec
    # print(l_sec)


    def list_tran_json(list):
        str_json = json.dumps(list, ensure_ascii=False, indent=2)
        return str_json


    print(list_tran_json(l_last))

