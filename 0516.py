"""
a = 1
def vartest(a):
    a = a +1
    return a

a=vartest(a)
print(a)

-------
a=1
a=a+1
print(a)
"""


#Q1.
"""
리스트에는 네 개의 정수가 저장돼 있다.
리스트 = [3, -20, -3, 44]
for문을 사용해서 리스트의 음수를 출력하라.
출력결과)
-20
-3
"""
#A
list1=[3,-20,-3,44]

"""
방법1) list를 이용
for i in list1:
    if (i<0):
        print(i)
"""

"""
방법2) range함수를 이용
for i in range(0,4):
    if(list1[i]<0):
        print(list1[i])
"""


#A
"""
리스트 = [3, -20, -3, 44]
 for 변수 in 리스트:
   if 변수 < 0:
     print(변수)
"""

#Q2.
"""
for문을 사용해서 3의 배수만을 출력하라.
리스트 = [3, 100, 23, 44]
출력결과)
3
"""
#나머지를 구하는 연산자: %
list2=[3,100,23,44]


"""방법1) 리스트를 이용
for i in list2:
    if(i%3 ==0):
        print(i)

"""
"""방법2)
for i in range(0,4):
    if(list2[i]%3==0):
        print(list2[i])
"""

#A.
"""
리스트 = [3, 100, 23, 44]
for 변수 in 리스트:
  if 변수 % 3 == 0:
    print(변수)
"""

#Q3.
"""
리스트에서 20 보다 작은 3의 배수를 출력하라
리스트 = [13, 21, 12, 14, 30, 18]
출력결과)
12
18
"""
"""
list3=[13, 21, 12, 14, 30, 18]
for i in list3:
  if (i < 20) and (i % 3 == 0):
    print(i)
"""

"""
for i in range(0,6):
    if (list3[i]<20) and (list3[i]%3==0):
        print(list3[i])
"""

#A.
"""
리스트 = [13, 21, 12, 14, 30, 18]
for 변수 in 리스트:
  if (변수 < 20) and (변수 % 3 == 0):
    print(변수)
"""

#Q4.
"""
리스트에서 세 글자 이상의 문자를 화면에 출력하라
리스트 = ["I", "study", "python", "language", "!"]
출력결과)
study
python
language
"""

list4=["I", "study", "python", "language", "!"]

"""
for i in list4:
    if ( len(i)>=3 ):
        print(i)
"""

"""
for i in range(0,5):
    if ( len(list4[i]) >= 3 ):
        print(list4[i])
"""



#A.
"""
리스트 = ["I", "study", "python", "language", "!"]
for 변수 in 리스트:
  if len(변수) >= 3:
    print(변수)
"""

#Q5.
"""
월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중
월드컵이 개최되는 연도를 출력하라.
2002
2006
2010
...
2042
2046
2050
"""

"""
for i in range(2002,2051,4):
    print(i)

"""

#A.
"""
for x in range(2002, 2051, 4) :
    print (x)
"""
