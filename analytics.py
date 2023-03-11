import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


from krwordrank.word import KRWordRank
from konlpy.tag import *
from matplotlib import rc
from collections import Counter
import numpy as np
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
import matplotlib.font_manager as fm


class ConvertDataFrame:
    """
    입력받은 object를 dataframe 형태로 변환합니다
    """

    def convert(column_data: list, original_data: object):
        """
        입력받은 값을 dataframe 형태로 변환합니다

        input:
            column_data(list): dataframe에서 header가 될 목록
            original_data(object): 변환할 원본 데이터 오브젝트


        return:
            dataframe(DataFrame): 입력받은 값을 dataframe화 한 object
        """
        dataframe = pd.DataFrame(data=original_data, columns=column_data)
        return dataframe


class Report:
    pass


STOPWORKDS = ["네", "완료", "혹시"]


class WordAnalytics:
    """
    단어를 통해 시각화하는 클래스이며 wordCloud를 통해 시각화를 checkFrequency를 통해 단어의 빈도를 확인합니다
    """

    def __init__(self) -> None:
        self.wordrank_extractor = KRWordRank(
            min_count=3,  # 단어의 최소 출현 빈도수 (그래프 생성 시)
            max_length=15,  # 단어의 최대 길이
            verbose=True,
        )
        self.okt_obj = Okt()

    def extractKrwordrank(self, dataframe: pd.DataFrame, text_filed_name: str):
        """
        Krwordrank 모듈을 통해 단어의 빈도수를 확인합니다
        해당 모듈에 사용되어진 알고리즘으로인해 형태소분석을 통한 단어의 원형을 기준으로 빈도를 삼는것이아님으로
        값의 형태가 달라질 수 있습니다

        input:
            dataframe: 빈도를 확인할 dataframe object

        returns:

        """
        texts = dataframe[text_filed_name].values.tolist()
        keywords, rank, graph = self.wordrank_extractor.extract(texts)

        for word, r in sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:30]:
            print("%8s:\t%.4f" % (word, r))

    def extractKonlpy(self, dataframe: pd.DataFrame, text_filed_name: str):
        return_words_frequency = {}

        nouns = self.okt_obj.nouns(dataframe.to_string(columns=[text_filed_name]))
        # counter를 통한 전체 단어 빈도 집계
        all_words_frequency = Counter(nouns)

        # 단어의 길이가 띄어쓰기를 제외하고 1개인 단어 제외, 빈도의 갯수가 5이하인항목 제외
        for key, value in all_words_frequency.items():
            if len(key.strip()) > 1 and value > 5:
                return_words_frequency[key] = value

        # 정렬
        print_value = sorted(
            return_words_frequency.items(), key=lambda x: x[1], reverse=True
        )
        # 출력 및 리턴
        print(print_value)
        return return_words_frequency

    def showWordCloud(frequency_words: dict):
        wc = WordCloud(width=1000, height=1000, scale=3.0, max_font_size=250)
        gen = wc.generate_from_frequencies(frequency_words)

        MAC_PATH = "/System/Library/Fonts/Supplementa/Nanum Gothic.ttf"

        font = fm.FontProperties(fname=MAC_PATH, size=9)
        plt.rcParams["font.family"] = "AppleGothic"
        print(mpl.rcParams["font.family"])

        # plt.rc("font", family="AppleGothic")
        mpl.rcParams["axes.unicode_minus"] = False

        plt.figure()
        # plt.imshow(gen)
        # plt.imshow(gen)

    def showBarGraph(frequency_words: dict):
        plt.rcParams["font.family"] = "AppleGothic"
        tuple_data = sorted(frequency_words.items(), key=lambda x: x[1], reverse=True)
        column_data = ["words", "count"]
        df = ConvertDataFrame.convert(column_data, tuple_data)

        plt.bar(range(df["count"]), df["count"])
        ax = plt.subplot()
        ax.set_xticklabels(df["words"], rotation=50)

        plt.show()
