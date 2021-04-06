#2장 연습문제
#1번
korean=80
english=75
math=55
mean=(korean+english+math)/3
print(mean)

#2번
number=12
if (number %2 ==0):
    print("짝수입니다.")

else:
    print("홀수입니다.")

#3번문제
pin="881120-1068234"
birth=pin[0:6]
a="19"
print(a+birth)

#4번문제
pin="881120-1068234"
print(pin[7])

#5번문제
a="a:b:c:d"
b=a.replace(":","#")
print(b)

#6번문제
a=[1, 3, 5, 4, 2]
b=[1, 3, 5, 4, 2]
b.reverse()
a.sort()
a.reverse()
print(a)

#7번
a=['Life', 'is', 'too', 'short']
string=" ".join(a)
print(string)

#8번
a=(1,2,3)
b=(4,)
print(a+b)

#9번 3번
#10번
a={'A':90, 'B':80, 'C':70}
b=[1,2,3]
print(b.pop(1))
print(a.pop("B"))
print(a)

#11번
a=[1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
b=set(a)
b=list(b)
print(b)

#12번 
a = b = [1, 2, 3]

print(b)

c=[1, 2, 3]
d=[1, 2, 3]

print(d)









    
