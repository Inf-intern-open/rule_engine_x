import rule_detail

def positive_cases(json_dict):
    return rule_detail.delet(rule_detail.change_value_positive(rule_detail.handle_rule_detail(json_dict)))

def negative_cases(json_dict):
    return rule_detail.delet(rule_detail.change_value_negative(rule_detail.handle_rule_detail(json_dict)))

# print(positive_cases({"all": [{"rule_type": "abnormal_text_rule", "entity": "各种类型室上性心动过速"}, {"rule_type": "abnormal_quantifiable_rule", "entity": "心室率", "operator": "≥", "value": 200, "unit": "次/min"}]}))
#
# print(negative_cases({"all": [{"rule_type": "abnormal_text_rule", "entity": "各种类型室上性心动过速"}, {"rule_type": "abnormal_quantifiable_rule", "entity": "心室率", "operator": "≥", "value": 200, "unit": "次/min"}]}))


