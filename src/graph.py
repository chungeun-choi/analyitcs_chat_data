import matplotlib.pyplot as plt
from pandas import DataFrame
from src.commonUtil import Common


WORKING_DIR = Common.getDirPath()


class Graph:
    def __init__(self) -> None:
        self.plt = plt
        plt.rcParams["font.family"] = "AppleGothic"

    def makeGraph(
        self,
        dataframe: DataFrame,
        type: str,
    ):
        if type == "bar":
            fig = dataframe.plot(kind=type, x="words", fontsize=8, figsize=(10, 10)).get_figure()
        else:
            labels = dataframe["words"].to_list()
            explode = [0.1] * len(labels)
            fig = dataframe.plot(
                kind=type,
                y="count",
                labels=labels,
                fontsize=8,
                figsize=(10, 10),
                autopct="%.1f%%",
                explode=explode,
            ).get_figure()

        report_path = Common.makeDir(WORKING_DIR)
        self.saveGraph(fig, report_path, type)

    def saveGraph(self, graph: object, path: str, type: str):
        """
        graph 객체를 입력받아 pdf 파일형태로 저장합니다

        Args:
            graph (object): Dataframe을 통해 생성한 그래프 객체
            path (str): 파일의 저장 위치
        """
        graph.savefig(path + "/{type}.pdf".format(type))

    def saveImage(image: object, path: str):
        image.to_file(path + "/wordCloud.png")
