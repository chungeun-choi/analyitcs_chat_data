import os


class Common:
    def makeDir(directory_path: str):
        dir_name = "/report"
        absolute_path = directory_path +  dir_name
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
