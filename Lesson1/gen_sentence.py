import random

teacher = """
sentence => say_hi , date 是 weekday , 我们开始上第 number 节 class 课!
say_hi => 大家好 | 同学们好 | 同学老师们好
date => 今天 | 昨天 | 明天
weekday => 星期一 | 星期二 | 星期三 | 星期四
number => number number_detail | number_detail
number_detail => 1 | 2 | 3 | 4 | 5 
class => 保险 | 安全 | 基金
"""


def split_rules(pre_rules, equal_split='=', or_split='|'):
    rules = {}

    for line in pre_rules.split('\n'):
        # split时第一行和末尾行为空
        if not line:
            continue

        stmt, expr = line.split(equal_split)
        expr = expr.split(or_split)
        # print(stmt, expr)

        rules[stmt.strip()] = expr

    return rules


def generate(grammer_rule, target):
    if target in grammer_rule:
        condidates = grammer_rule[target]
        condidate = random.choice(condidates)
        return "".join(generate(grammer_rule, target=c.strip()) for c in condidate.split())
    else:
        return target


def main():
    rules = split_rules(teacher, equal_split='=>', or_split='|')
    print(generate(rules, 'sentence'))


if __name__ == '__main__':
    main()