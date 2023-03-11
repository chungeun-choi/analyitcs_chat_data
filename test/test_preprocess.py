import sys

sys.path.append("/Users/cucuridas/Desktop/wanted_chat")

from preprocess import Preprocess

FILEPATH = "/Users/cucuridas/Desktop/wanted_chat/data/meeting_saved_chat 복사본.txt"


if __name__ == "__main__":
    obj = Preprocess()

    ## Test function1 - load_file
    test_fucntion = obj.load_file(FILEPATH)
    # print(test_fucntion)
    assert isinstance(test_fucntion, list)

    ## Test function2 - preprocessing
    test_function2 = obj.preprocessing(FILEPATH)
    print(test_function2)
    assert isinstance(test_function2, list)
