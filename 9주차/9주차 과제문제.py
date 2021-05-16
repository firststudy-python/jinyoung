#1번문제

아래의 에러가 발생하는 이유에 대해 설명하라.

hello()
def hello():
    print("Hi")

    
실행 예)

NameError: name 'hello' is not defined



#2.
함수의 호출 결과를 예측하라.

def 함수(a, b) :
    print(a + b)

----
함수(3, 4)
함수(7, 8)


#3.
아래와 같은 에러가 발생하는 원인을 설명하라.

def 함수(문자열) :
    print(문자열)
함수()
TypeError: 함수() missing 1 required positional argument: '문자열'


#4.
아래 코드의 실행 결과를 예측하라.

def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)


#5.
아래 코드의 실행 결과를 예측하라.

def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)
