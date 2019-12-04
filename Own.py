# 熟悉功能用
import lines as lines
from textblob import TextBlob
# b = TextBlob("Simple is better than complex.")
# print(b.tags,b.noun_phrases,b.words,b.sentiment)
# b = TextBlob("bonjour")
# print(b.detect_language())
# c = TextBlob("Simple es mejor que complejo")
# print(c.translate(to="en"))

# Let's begin!
from textblob import TextBlob
from wordcloud import WordCloud
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import  rcParams

text = open("result.txt",encoding='utf-8',errors='ignore')        #防止编码问题不能运行'gbk' codec can't decode byte 0xbf in position 2: illegal multibyte sequence

text = ' '.join(text)           #list合并转为str，其中''里面如果为空，则拼接的字符串是无缝连接的，如果有空格，则拼接出的字符串以空格连接
# text = text.replace("<br />","")              #首先清除爬取的评论中的各种网页符号和多余的信息
# text = text.replace("&#34","")
replace_list = ["br />", "&#34",'{"text": ["', '"]}', '\"', "\\", "<"]   #注释反斜杠要打两个，即\\
for each in replace_list:
    text = text.replace(each, "")               #此三行代替前两行，都是删除换行符，如果要删的符号过多，此法更方便
# print(text)
blob = TextBlob(text)

# 情感分析
# allsentences = blob.sentiment       #全体的情感分析结果
# print("总体情况是：" , allsentences, "\n以下为每一句的分析：")

# 逐条情感分析
# text = text.split("\n")                         #以回车为分隔符分割各条评论，注意，分割完自动就把字符串转为列表形式了
#
# pos = 0
# neg = 0
# neu = 0
#
# for i in range(len(text)):
#     text[i] = ''.join(text[i])                  #再转回字符串形式
#     blob = TextBlob(text[i])
#     print(blob.sentiment)                       #每句做情感分析，输出
#     score = blob.sentiment.polarity
#     if score > 0.05:
#         print("积极")
#         pos += 1
#     elif score < -0.03:
#         print("消极")
#         neg += 1
#     else:
#         print("中立")
#         neu += 1
#
# 多余程序，练习用
# # 第一句的情感分析
# # first = blob.sentences[0].sentiment
# # print(first)
# # # 第二句的情感分析
# # second = blob.sentences[1].sentiment
# # print(second)

# 提取高频词汇
text = "It's an interesting concept but the execution doesn't really work and it's a long story to get through for " \
       "what is an unsatisfactory ending. How in the world did this interesting book average 4+ stars? My apologies," \
       " but I can't tell you because I apparently read something completely different from everyone else! I don't " \
       "like the book. It's one of the most interesting book I have ever read! The book is different from other one."

tags = blob.tags
# tags = TextBlob(text).tags                #测试用，和前面text一起
# print(tags[0][1])
get_tags_JJ = []
get_tags_NN = []
get_tags_VB = []
for i in range(len(tags)):                  #遍历所有标签，找出想要的分类
    if tags[i][1] == "JJ":
        get_tags_JJ.append(tags[i][0])
    elif tags[i][1] == "NN":
        get_tags_NN.append(tags[i][0])
    elif tags[i][1] == "VB":
        get_tags_VB.append(tags[i][0])
# print(get_tags_JJ,get_tags_NN)
tags_JJ_list = list(set(get_tags_JJ))       #把找出的标签先转为集合去重，再重新列表化，方便和原列表对比
tags_NN_list = list(set(get_tags_NN))
tags_VB_list = list(set(get_tags_VB))

JJ_num = {}
NN_num = {}
VB_num = {}
def tags_frequency(get_tags, tags_list):    #记录词频，对比去重后的新列表和原列表，如果相同，在计数字典中value+1，最后返回字典
    tags_dir = {}
    for i in range(len(tags_list)):
        tags_dir[tags_list[i]] = 0
        for j in range(len(get_tags)):
            if tags_list[i] == get_tags[j]:
                tags_dir[tags_list[i]] += 1
    return tags_dir
JJ_num = tags_frequency(get_tags_JJ, tags_JJ_list)
# print(JJ_num)
JJ = sorted(JJ_num.items(), key=lambda x: x[1], reverse = True)[:5]     #根据字典中值大小进行排序，利用 sorted 函数的 key 参数：sorted(iterable, key=None, reverse=False)，x[1]表示根据value排序
NN_num = tags_frequency(get_tags_NN, tags_NN_list)
NN = sorted(NN_num.items(), key=lambda x: x[1], reverse = True)[:5]     #且只输出词频最大的前五个词[:5]，输出结果是列表形式
VB_num = tags_frequency(get_tags_VB, tags_VB_list)
VB = sorted(VB_num.items(), key=lambda x: x[1], reverse = True)[:5]
print(JJ, NN, VB)




# 画图
# # fig = plt.figure(2)
# # rects = plt.bar(x = (0.2,1), height = (1,0.5), width= 0.2, align="center", yerr = 0.0001, color = ("b","green"))    #两个柱状图写在一个变量里
# rects1 = plt.bar(x = (0.5), height = (pos), width= 0.2, align="center", yerr = 0.0001, color = ("b"), label =("Pos"))
# rects2 = plt.bar(x = (1), height = (neu), width= 0.2, align="center", yerr = 0.0001, color = ("green"), label =("Neu"))
# rects3 = plt.bar(x = (1.5), height = (neg), width= 0.2, align="center", yerr = 0.0001, color = ("y"), label =("Neg"))
# plt.title("Result")
# plt.legend()
# def autolabel(rects):
#     for rect in rects:
#         height = rect.get_height()
#         plt.text(rect.get_x()+rect.get_width()/2.-0.025,1.01*height, "%s"%float(height))    #柱状图上方字体位置
# autolabel(rects1)
# autolabel(rects2)
# autolabel(rects3)
# plt.xticks((0.5,1,1.5),("Positive","Neutral","Negative"))
# plt.show()

# 生成词云
def getWordCloud(text_str, picture_name):       # 调用专门的函数
    wordcloud = WordCloud(background_color="white",width=1980, height=1080, margin=2, random_state=0).generate(text_str)
    wordcloud.to_file(picture_name)

def allwords(list):                    # 在原来高频词形成的列表中，只把词汇提出，而不要频率值，以生成词云用
    newstr = []
    for i in range(len(list)):
        newstr.append(list[i][0])
    allwords = ' '.join(newstr)        # 一个个单词拉出来形成一个新列表后，转成字符串，并用空格连接，以生成词云用
    return allwords

allwords = allwords(JJ) + allwords(NN) + allwords(VB)
getWordCloud(allwords, "new.jpg")
