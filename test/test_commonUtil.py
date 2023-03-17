import sys

sys.path.append("/Users/cucuridas/Desktop/analyitcs_chat_data")

from src.commonUtil import Common


if __name__ == "__main__":
    path = "/Users/cucuridas/Desktop/analyitcs_chat_data"

    # Test function - makeDir
    Common.makeDir(path)

    # Test function - getDirPath
    Common.getDirPath()
