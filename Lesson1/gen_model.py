import jieba
from collections import Counter


# 清洗、生成数据
def gen_data():
    corpus = 'D:/AI/NLP课程/作业/Lesson1/train.txt'
    with open(corpus, 'r', encoding='utf8') as f:
        FILE = f.read()
    FILE = FILE.split('\n')

    file_content = str()
    for i in range(len(FILE)-1):
        # 过滤掉非中文字符
        file_extract = FILE[i].split(" ")[4].replace('？','\n')
        file_content += file_extract
        # 返回最终的分词结果
    return list(jieba.cut(file_content))


# 生成2_gram模型
def two_gram_model(sentence):
    all_tokens = gen_data()
    short_tokens = list(jieba.cut(sentence))

    probability = 1

    # 生成两个counter
    one_gram_counts = gen_count(all_tokens, 1)
    two_gram_counts = gen_count(all_tokens, 2)

    #计算sentence概率
    for i in range(len(short_tokens) - 1):
        word = short_tokens[i]
        next_word = short_tokens[i + 1]

        _two_gram_c = get_gram_count(word + next_word, two_gram_counts)
        _one_gram_c = get_gram_count(next_word, one_gram_counts)
        pro = _two_gram_c / _one_gram_c

        probability *= pro

    return probability


# 生成分词后的counter，根据参数选择一个词或两个词的
def gen_count(jieba_data, count_nums):
    if count_nums == 1:
        words_count = Counter(jieba_data)
        return words_count
    else:
        _2_gram_words = [jieba_data[i] + jieba_data[i+1] for i in range(len(jieba_data)-1)]
        _2_gram_word_conts = Counter(_2_gram_words)
        return _2_gram_word_conts


# 分词的counts数
def get_gram_count(word, wc):
    if word in wc:
        return wc[word]
    else:
        return wc.most_common()[-1][-1]


def main():
    # gen_data()
    pro = two_gram_model("法律要求是这样")
    print("%.20f" % pro)


if __name__ == '__main__':
    main()



