import sys
import os


PATH = "/Users/cucuridas/Desktop/wanted_chat/"
sys.path.append(PATH)


from preprocess import Preprocess

FILENAME = "meeting_saved_chat_0306.txt"


if __name__ == "__main__":
    obj1 = Preprocess(PATH + "data")
    ## Test function1 - load_file
    test_fucntion = obj1.load_file(FILENAME)
    # print(test_fucntion)
    assert isinstance(test_fucntion, list)

    ## Test function2 - preprocessing
    obj2 = Preprocess(PATH + "data")
    test_function2 = obj2.preprocessing()
    print(len(test_function2))
    assert isinstance(test_function2, list)
