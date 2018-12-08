import json
import jieba


def extract_job_req():
    job_set = set()
    with open('files/jobs_all.txt', 'r') as f:
        jobs = f.readlines()
    job_reqs = [json.loads(job) for job in jobs]
    for i in job_reqs:
        temp = i['card'].replace('\\n', '').replace('<br/>', '').replace('\\t', '').strip()
        job_set.add(temp)
    print(len(job_set))
    with open('files/jobs_req.txt', 'w') as f:
        for i in job_set:
            f.write(i)
            f.write('\n')

filter_words=['岗位职责',
              ]

from wordcloud import WordCloud

if __name__ == '__main__':

    with open('files/jobs_req.txt', 'r') as f:
        text = ''.join(f.readlines())
        stopwords = {}.fromkeys(f.read().split("\n"))


        # jieba.load_userdict("./utils/jieba_user_dict.txt")


        segs = jieba.cut(text)
        mytext_list = []
        # 文本清洗
        for seg in segs:
            if seg not in stopwords and seg != " " and len(seg) != 1:
                mytext_list.append(seg.replace(" ", ""))
        cloud_text = ",".join(mytext_list)
        print(cloud_text)

        # wc = WordCloud(
        #     background_color="white",  # 背景颜色
        #     max_words=200,  # 显示最大词数
        #     font_path="./font/wb.ttf",  # 使用字体
        #     min_font_size=15,
        #     max_font_size=50,
        #     width=400  # 图幅宽度
        # )
        wc = WordCloud()
        wordcloud = wc.generate(cloud_text)
        # wc.to_file("pic.png")

        import matplotlib.pyplot as plt

        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")

        # max_font_size设定生成词云中的文字最大大小
        # width,height,margin可以设置图片属性
        # generate 可以对全部文本进行自动分词,但是他对中文支持不好
        wordcloud = WordCloud(max_font_size=80,width=1000,height=600).generate(text)
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()
