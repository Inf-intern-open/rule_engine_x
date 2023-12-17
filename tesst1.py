import json
import random
import sys
json_dict = {'any': [
    {'all': [{'rule_type': 'abnormal_quantifiable_rule', 'entity': '收缩压', 'operator': '≥', 'value': 160, 'unit': 'mmHg'},
             {'rule_type': 'abnormal_quantifiable_rule', 'entity': '收缩压', 'operator': '≤', 'value': 179, 'unit': 'mmHg'}]},
    {'all': [{"any":[{} ,{}]}]}
    ]
}

s = "{'all': [{'rule_type': 'abnormal_quantifiable_rule', 'entity': '血白细胞计数', 'operator': '>', 'value': 15, 'unit': '×10^9/L'}, {'rule_type': 'abnormal_quantifiable_rule', 'entity': '中性粒细胞百分比', 'operator': '>', 'value': 90, 'unit': '%'}, {'any': [{'rule_type': 'abnormal_text_rule', 'entity': '肝脏超声包含液性回声暗区', 'operator': 'has'}, {'rule_type': 'abnormal_text_rule', 'entity': '肝脏超声包含脓肿内液平面', 'operator': 'has'}]}]}"
s = s.replace("'", '"')
s = json.loads(s)

print(s['all'])
print(random.uniform(1,sys.maxsize))
count=0
a=[{'entity': '收缩压', 'value': 213.3232816252255, 'unit': 'mmHg'}, {'entity': '收缩压', 'value': 17.788220009703018, 'unit': 'mmHg'}, {'entity': '舒张压', 'value': 193.4164464275947, 'unit': 'mmHg'}, {'entity': '舒张压', 'value': 19.600639654528667, 'unit': 'mmHg'}]
for i in a:
    for j in i.values():
        if j== '收缩压':
            count += 1
print(count)
def count_occurrences(mylist, value):
    count = 0
    for i in mylist:
        for j in i.values():
            if j == value:
                count += 1
    return count


l= [{'entity': '舒张压', 'value': 5.618820169828297, 'unit': 'mmHg'}, {'entity': '舒张压', 'value': 100.15658358822496, 'unit': 'mmHg'}]
for i in l:
    if count_occurrences(l, i['entity']) == 2:
        l.remove(i)

print(l)

m={'all': [{'rule_type': 'abnormal_quantifiable_rule', 'entity': '弥漫性肝脏密度降低', 'operator': 'is', 'value': True}, {'rule_type': 'abnormal_quantifiable_rule', 'entity': '肝/脾CT比值', 'operator': '≤', 'value': 0.5}]}
# m = m.replace("'", '"')
# m = json.loads(m)
print(m)