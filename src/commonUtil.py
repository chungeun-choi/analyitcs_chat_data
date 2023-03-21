import os


class Common:
    def makeDir(directory_path: str):
        dir_name = "/report"
        absolute_path = directory_path + dir_name
        if os.path.isdir(absolute_path):
            print("Dir is exits")
            return absolute_path
        else:
            os.mkdir(absolute_path)
            print("Create dir, Succcesss")
            return absolute_path

    def getDirPath():
        python_file_path = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(python_file_path)
        return parent_directory

    def excludeSort(data: dict, stopwords: list, to_dict: bool = False):
        exclude_sort_value = [
            (word, score)
            for word, score in sorted(data.items(), key=lambda x: -x[1])
            if not (word in stopwords)
        ]
        if to_dict:
            return dict(exclude_sort_value)

        return exclude_sort_value
