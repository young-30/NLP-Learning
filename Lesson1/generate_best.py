from gen_sentence import *
from gen_model import *


def generate_best(number, gram_rule, gram_model):
    rules = split_rules(gram_rule, equal_split='=>', or_split='|')
    sentences = dict()
    for i in range(number):
        phrase = generate(rules, 'sentence')
        #打分前去除标点符号
        pure_phrase = phrase.replace(',','').replace('!','')
        sentences[phrase] = gram_model(pure_phrase)

    print(sentences)
    # 对生成的"sentence：得分"字典进行排序
    sentences = sorted(sentences.items(), key=lambda x: x[1], reverse=True)

    # 返回分数最高的句子
    return sentences[0][0]


def main():
    best_senten = generate_best(5, teacher, two_gram_model)
    print(best_senten)


if __name__ == '__main__':
    main()