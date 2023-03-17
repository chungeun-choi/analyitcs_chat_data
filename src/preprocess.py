import re
import os


class Find:
    """
    전처리하기위한 원본 데이터를 찾습니다
    """

    def __init__(self, file_path: str):
        self.file_path: str = file_path
        self.FindFile()

    def FindFile(self):
        """
        객체 생성 후 입력 받는 파일 위치의 파일 리스트를 찾습니다

        Returns:
            file_list(list[str]) : 파일 위치의 파일 리스트
        """

        self.file_list = os.listdir(self.file_path)
        return self.file_list


class Preprocess(Find):
    """
    해당 클래스 정규표현식을 통해 zoom meeting chating 데이터를 파싱하는 클래스입니다
    """

    def __init__(self, file_path: str):
        super().__init__(file_path)
        self.split_pattern = r"\d{2}:\d{2}:\d{2}"
        self.parse_pattern_mac = r"(?P<timeStamp>\d{2}:\d{2}:\d{2}) 시작 (?P<userName>.*?) (?P<target>[송신자|수신자]+) (?P<targetRange>\w+):(?P<userChatData>[\W|\w]+)"
        self.parse_pattern_win = r"(?P<timeStamp>\d{2}:\d{2}:\d{2}) (?P<userName>.*?) (?P<target>[송신자|수신자]+) (?P<targetRange>\w+):(?P<userChatData>[\W|\w]+)"
        self.file_data = None

    def load_file(self, file: str):
        """
        파일을 읽어와 원하는 형태의 리스트 데이터로 적재합니다

        input :
            file_path(str): 읽어올 파일의 위치

        return :
            self.filed_data(list[str]): 특정 기준으로 잘려져 나온 list 데이터

        """
        if Preprocess.check_file_type(file):
            absolute_path = "{}/{}".format(self.file_path, file)
            with open(absolute_path, "r") as f:
                if self.file_data == None:
                    self.file_data = self.split_data(f.read())
                else:
                    self.file_data = self.file_data + self.split_data(f.read())

            return self.file_data

    def check_file_type(file):
        if file.split(".")[1] == "txt":
            return True
        else:
            return False

    def split_data(self, file_data: str):
        """
        읽어온 데이터를 timestamp 단위로 자릅니다

        input :
            file_data: str

        return :
            outputs: list[str]
        """
        split_indices = [m.start(0) for m in re.finditer(self.split_pattern, file_data)]
        outputs = [
            file_data[i:j].strip()
            for i, j in zip(split_indices, split_indices[1:] + [None])
        ]
        return outputs

    def parse(self, original_data: str):
        """
        입력받은 데이터를 regex를 통해 파싱하여 필요데이터를 찾습니다

        input:
            original_data(str): 파싱할 원본 데이터

        return:
            parse_data(tuple(str)): regex에 의해서 파싱한 데이터들의 집합(tuple)
        """
        parse_obj = re.match(self.parse_pattern_mac, original_data)
        if parse_obj == None:
            parse_obj = re.match(self.parse_pattern_win, original_data)
        parse_data = parse_obj.groups()
        return parse_data

    def preprocessing(self):
        """
        파일 데이터를 읽어와 정규표현식을 통해 데이터 전처리 작업을 진행합니다


        return:
            preprocessing_data(list(tupe(str))): 전처리가되어 파싱된 데이터들의 집합 리스트를 return 합니다
        """
        for file in self.file_list:
            self.load_file(file)
        preprocessing_data = list(map(self.parse, self.file_data))

        return preprocessing_data
