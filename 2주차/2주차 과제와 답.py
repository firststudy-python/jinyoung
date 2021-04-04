#2주차 과제입니다.

#1. letters의 문자열에서 첫번째와 세번째 문자를 출력하세요.
    #예: letters='python'
    #콘솔출력 결과: p t

#답  letters='python'
#    print(letters[0], letters[2])


#2. 자동차 번호가 다음과 같을 때 뒤 네자리만 출력하세요.
    #license_plate = "24가 2210"
    #출력결과:2210

#답 license_plate = "24가 2210"
#   print(license_plate[-4:])


#3. 아래의 전화번호에서 하이푼 "-"을 제거하고 출력하세요.
    #phone_number = "010-1111-2222"
    #출력결과: 010 1111 2222

#답 phone_number = "010-1111-2222"
#   phone_number1 = phone_number.replace("-", " ")
#   print(phone_number1)


#4. url에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
    # url = "http://sharebook.kr"
    #출력결과: kr

#답 url = "http://sharebook.kr"
#   url_split = url.split('.')
#   print(url_split[-1])

#5. 아래 문자열에서 소문자 a를 대문자 A로 변경하세요.
    #string = 'abcdfe2a354a32a'
    #출력결과: Abcdfe2A354A32A

#답 string = 'abcdfe2a354a32a'
#   string = string.replace('a', 'A')
#   print(string)


#6. %formatting을 이용하여 다음의 결과가 나오도록 출력해보세요.
    #name1 = "김민수" 
    #age1 = 10
    #name2 = "이철희"
    #age2 = 13

    #출력결과: 이름: 김민수 나이: 10
    #          이름: 이철희 나이: 13


#답 name1 = "김민수" 
#   age1 = 10
#   name2 = "이철희"
#   age2 = 13
#   print("이름: %s 나이: %d" % (name1, age1))
#   print("이름: %s 나이: %d" % (name2, age2))


#7. 6번의 문제를 format() 메소드를 사용해 출력해보세요.

#답 print("이름: {} 나이: {}".format(name1, age1))
#   print("이름: {} 나이: {}".format(name2, age2))








    

