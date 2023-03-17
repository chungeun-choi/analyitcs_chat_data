import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
print(path)
sys.path.append(path)

from preprocess import Preprocess

FILEPATH = path + "/data/meeting_saved_chat 복사본.txt"


if __name__ == "__main__":
    obj = Preprocess(path + "data")

    ## Test function1 - load_file
    test_fucntion = obj.load_file(FILEPATH)
    # print(test_fucntion)
    assert isinstance(test_fucntion, list)

    ## Test function2 - preprocessing
    test_function2 = obj.preprocessing()
    print(test_function2)
    assert isinstance(test_function2, list)
