import random

def is_variable(pat):
     return pat.startswith('?') and all(s.isalpha() for s in pat[1:])


def pat_match(pattern, saying):
    if not pattern or not saying: return []
    
    if is_variable(pattern[0]):
        return [(pattern[0], saying[0])] + pat_match(pattern[1:], saying[1:])
    else:
        if pattern[0] != saying[0]: return []
        else:
            return pat_match(pattern[1:], saying[1:])


def pat_to_dict(patterns):
    return {k: v for k, v in patterns}


def subsitite(rule, parsed_rules):
    if not rule: return []
    
    return [parsed_rules.get(rule[0], rule[0])] + subsitite(rule[1:], parsed_rules)


defined_patterns = {
    "I need ?X": ["Image you will get ?X soon", "Why do you need ?X ?"], 
    "My ?X told me something": ["Talk about more about your ?X", "How do you think about your ?X ?"]
}


def get_response(saying, rules=defined_patterns):
    """" please implement the code, to get the response as followings:
    
    >>> get_response('I need iPhone') 
    >>> Image you will get iPhone soon
    >>> get_response("My mother told me something")
    >>> Talk about more about your monther.
    """
    for rule in rules.keys():
    	pat_list = pat_match(rule.split(), saying.split())   #生成模式对
    	if pat_list:  #成功匹配
    		pat_dict = pat_to_dict(pat_list)    #生成模式字典
    		num = random.randint(0, len(rules[rule])-1)   #随机生成索引
    		sentence = " ".join(subsitite(rules[rule][num].split(), pat_dict))  #生成对话
    		return sentence
    	else:
            print(123)
            continue

    	

def main():
    pattern = 'I want a ?X'.split()
    saying = "I want holiday".split()
    print(pat_match("?X greater than ?Y".split(), "3 greater than 2".split()))

    john_pat = pat_match('?P needs ?X'.split(), "John needs vacation".split())
    sneten = subsitite("Why does ?P need ?X ?".split(), pat_to_dict(john_pat))
    print(" ".join(sneten))

   
    sentence = get_response('My mother told me something')
    print(sentence)

main()