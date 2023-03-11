import sys

sys.path.append("/Users/cucuridas/Desktop/wanted_chat")

from analytics import *
from preprocess import Preprocess
import pandas as pd

FILEDINFO = ["time_stamp", "user_name", "target", "target_range", "user_chat_data"]

if __name__ == "__main__":
    mokup_obj = Preprocess().preprocessing(
        "/Users/cucuridas/Desktop/wanted_chat/data/meeting_saved_chat 복사본.txt"
    )

    # Test function - convert
    test_obj = ConvertDataFrame.convert(FILEDINFO, mokup_obj)
    # print(test_obj)
    assert isinstance(test_obj, pd.DataFrame)

    # Test function - checkFrequency
    # test_obj2 = WordAnalytics()
    # test_obj2.extractKrwordrank(test_obj, "user_chat_data")

    # Test function - extractNouns
    test_obj3 = WordAnalytics().extractKonlpy(test_obj, "user_chat_data")

    # Test function - showWordCloud
    # WordAnalytics.showWordCloud(test_obj3)

    # Test function - showBarGraph
    WordAnalytics.showBarGraph(test_obj3)
