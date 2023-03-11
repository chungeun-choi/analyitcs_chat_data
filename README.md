# 채팅데이터를 활용한 데이터 분석

해당 프로젝트는 ‘wanted 프리온보딩 [데이터]’ 를 참여하면서 배운 내용을 복습하기 위한 프로젝트입니다 

사용되는 데이터는 온라인 강의가 끝난 뒤 zoom 채팅방에 남긴 데이터를 활용하여 단어를 활용한 데이터 분석을 진행 하였습니다

---

## 목표 :

챌린지 참여 내용에 대한 복습 및 채팅 내용을 통한 keyword 추출 작업

---

## 과정

```yaml
1. txt 데이터로 저장되어진 데이터에 대한 전처리 작업 진행
2. 전처리화된 데이터를 분석할 수 있는 object인 dataframe으로 변경
3. tokenizer를 통한 단어 추출 및 형태소 분석
4. 시각화 도구를 활용한 Keyword 확인 및 빈도 확인
```

**상세 과정**

1. txt 데이터로 저장되어진 데이터에 대한 전처리 작업 진행
    
    1) 데이터 자르기 
    
    timestamp를 기준으로 새로운 채팅 로그가 생성됨에 따라 timestamp를 기준으로 1차적으로 데이터를 잘라줍니다
    
    ![https://user-images.githubusercontent.com/65060314/224467285-b441e12a-9f3a-4b4f-a933-cb8d78847b69.png](https://user-images.githubusercontent.com/65060314/224467285-b441e12a-9f3a-4b4f-a933-cb8d78847b69.png)
    
    2) 필요 데이터 파싱
    
    채팅 로그의 형태는 아래와 같습니다
    
    ```yaml
    {시간 정보} {채팅 시작알림} {이름} {송수신자 정보} {해당 채팅의 범위} {채팅내용}
    ```
    
    따라서 정규 표현식은 아래와 같이 정의하여 데이터를 파싱하도록 합니다
    
    ```yaml
    r"(?P<timeStamp>\d{2}:\d{2}:\d{2}) 시작 (?P<userName>.*?) (?P<target>[송신자|수신자]+) (?P<targetRange>\w+):(?P<userChatData>[\W|\w]+)"
    ```
    
2. 전처리화된 데이터를 분석할 수 있는 object인 dataframe으로 변경
    
    pandas의 DataFrame 클래스를 통해 분석할 수 있는 형태로 object 변경을 해줍니다 객체 생성 시 파라미터로 column에 대한 정보와 interable한 형태의 데이터를 입력 받아 정의하게됩니다
    
    ![https://user-images.githubusercontent.com/65060314/224467487-7e35fb8f-e694-4426-b375-a11ee2034818.png](https://user-images.githubusercontent.com/65060314/224467487-7e35fb8f-e694-4426-b375-a11ee2034818.png)
    
    따라서 데이터의 형태를 바꿔주는 class를 만들어 관리 할 수 있도록 정의합니다
    
    ```yaml
    class ConvertDataFrame:
        """
        입력받은 object를 dataframe 형태로 변환합니다
        """
    
        def convert(column_data: list, original_data: object):
            """
            입력받은 값을 dataframe 형태로 변환합니다
    
            input:
                column_data(list): dataframe에서 header가 될 목록
                original_data(object): 변환할 원본 데이터 오브젝트
    
            return:
                dataframe(DataFrame): 입력받은 값을 dataframe화 한 object
            """
            dataframe = pd.DataFrame(data=original_data, columns=column_data)
            return dataframe
    ```
    
3. tokenizer를 통한 단어 추출 및 형태소 분석
    
    ‘wanted 프리온보딩[데이터]’ 온라인 강의에서 사용한 ‘Krwordrank’ 모듈은 띄어쓰기가 없는 일본어,중국어데이터를 분석하기위해 만들어진 툴로서 한글 형태소 분석에는 제한적인 부분이 존재함에 따라 ‘konlpy’를 통해 형태소 분석을 진행 하였습니다
    
    > konlpy는 자바를 사용하여 만들어진 패키지임에 따라 jdk 설치가 로컬 pc에 진행 되어져야합니다 
    error info: https://github.com/konlpy/konlpy/issues/353 참조하여 해결
    > 
    
    1) 명사만 추출
    
    단어의 빈도를 확인하기위해 명사만 추출하도록 진행하였습니다
    
    2) Collection.Counter 함수를 통해 빈도 확인
    
    python 기본 패키지인 Collection의 Counter 클래스를 통해 단어에 대한 빈도를 확인합니다
    
    3) 불필요 데이터 제거
    
    단어의 글자 수가 2개 이하인 경우 의미를 가지지못한 단어라 판단하여 제거하였습니다
    빈도 수가 5 이하인 데이터는 중요도가 떨어진다고 판단하여 제거하였습니다
    
    > 빈도 집계 후 글자의 길이에 따라 제거한 이유
    반복을 통해  모든 단어의 길이를 확인해서 제거하기보다는 빈도를 계산후 제거하는 것이 반복의 횟수를 줄일 수 있을것이라 판단하여 진행하였습니다
    > 
    
4. 시각화 도구를 활용한 Keyword 확인 및 빈도 확인