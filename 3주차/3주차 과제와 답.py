#3주차 과제

#Q1. movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다.
#   "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
#   movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']

#A1. movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
#    movie_rank.insert(1, "슈퍼맨")
#    print(movie_rank)

#Q2. movie_rank 리스트에서 '럭키'를 삭제하라.
#   movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']

#A2. movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
#    del movie_rank[3]
#    print(movie_rank)

#Q3. 숫자 1 만 저장된 튜플을 생성하라.

#A3. 아래와 같이 괄호와 함께 하나의 정숫값을 저장하면 튜플이 정의 될 것같지만 그렇지 않습니다. type()을 출력해보면 파이썬은 튜플이 아닌 정수로 인식합니다.
#       my_tuple = (1)
#type (my_tuple) =>int 
#하나의 데이터가 저장되는 경우, 아래와 같이 쉼표를 입력해만 합니다.
#my_tuple = (1, )


#Q4. 변수 t에는 ('a', 'b', 'c') 값이 저장되어 있는 튜플이다.
#    변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.

#A4. t = ('A', 'b', 'c')

#Q5. 다음 튜플을 리스트로 변환하라.
#    interest = ('삼성전자', 'LG전자', 'SK Hynix')

#A5. data = list(interest)

#Q6. 다음 리스트를 튜플로 변경하라.
#    interest = ['삼성전자', 'LG전자', 'SK Hynix']

#A6. data = tuple(interest)







