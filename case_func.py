
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




from typing import List

def get_subset(rules: List[dict]) -> List[dict]:
    pass

def handle_rule(rule:dict):
    pass

def handle_any(rules: List[dict]): # [{} ,{}]
    sub_rules = get_subset(rules) # [{} ,{}],      [{}]
    result = handle_all(sub_rules)
    return result

def handle_all(rules: List[dict]): #  # [{} ,{}]
    result = []
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

def handle_rule_detail(rule_detail:dict):
    if 'all' in rule_detail:
        res_list = handle_all(rule_detail['all'])
    elif 'any' in rule_detail:
        res_list = handle_any(rule_detail['any'])
