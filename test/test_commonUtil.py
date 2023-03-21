import sys

sys.path.append("/Users/cucuridas/Desktop/analyitcs_chat_data")

from src.commonUtil import Common


if __name__ == "__main__":
    path = "/Users/cucuridas/Desktop/analyitcs_chat_data"

    # Test function - makeDir
    Common.makeDir(path)

    # Test function - getDirPath
    Common.getDirPath()

    # Test function - excludeSort
    test_obj = {"key1": 544, "key2": 123, "key3": 1232, "key4": 1233, "key5": 1}
    stop_words = ["key3"]
    value = Common.excludeSort(test_obj, stop_words)
    dict_value = Common.excludeSort(test_obj, stop_words, to_dict=True)
    print(value)
    print(dict_value)
