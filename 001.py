#01. 프린트문 출력
print(2020)
print(4+3)
print("Hello")
print('Hello')
print("3"+"A")

#03. 프린트문 출력
print(1)
print(2,end='')
print(3,end='')
print(5)
print(4,end='Finish')
print("This is My story for you")

#04
print(1,end='')
print(2,end='')
print(3,end='')
print(4,end='')
print(5)

#05
print("제",end=" ")
print("이름은",end=" ")
print("홍길동입니다",end=" ")

#06
print('E',end='F')

#07
a=2
b=3
c=a+b
print(c)
print(a,b)

#14
a=2
b=3
print((a+b)*2)

x=2.5
y=4
z=x*4+y
print(z)

k,l,m=1,2,1.5
print(k)
print(k+l)
print(k+l+m)
print(2*k)
print(2.0*k)
print(k-1.0)
print(k-1)
print(m-0.5)
print(l*m)
#22
name="Kevin"
work="IT company"
num1=5.3
num2=4.7517
print("I'm", name, "and work in", work)
print("I'm {} and work in {}".format(name,work))
print("This is {:8.2}, {:8.2}".format(num1,num2))
#23
country ="Korea"
population='50M'
print("{} has about {} people".format(country,population))
#27
x,y,z =14,3,5
print(x%y)
print(x//z)
print(x/z+y)
print(y**3+z)
print(x%z**2+y)

#30
a=3
b=7
c=b//a
print(a,b,c)

#34
a,b,c =1,3,5
print(float(a))
print(float(b-1))

#35
int_1=0
int_2=3
long_1=12345678
long_2=0x142
float_1=0.0
float_2=1.35
complex_1=1j
complex_1=1+3j
print(type(int_1))
print(type(complex_1))
print("1의 자료형은" , type(int_1))

#37
print(10,bin(10),oct(10),hex(10))
boolean_1=True
print(boolean_1)
boolean_2=False
print(boolean_2)
boolean_3=1 >0
print(boolean_3)

#52
num=13
if(num>1 & num <100):
    result1=True
else:
    result1=False
print('1초과 백미만인가?',result1)

#58
num=5
if(num==0):
    num=True
    print(num)

else:
    num=False
    print(False)

#59
num2=6
if(num2%2==0 & num2%3==0):
    num2=True
    print(num2)
else:
    num2=False
    print(num2)

#60
print('작은따옴표')
a='''작은따옴표
    세 개'''
b="""큰 따옴표
세개"""
print(a)
print(b)

#61
text1="item_1+\
item_2+\
item_3"
print(text1)
print("*"*40)
print("내이름은"+"tom")
first="내 이름은"
second="쌔ㅡ이다"
Third=first+second
print(Third)
name='chan'
print('이름은',name)
print("1234\n5\t6\n89\10")
a='가나\n다라\n마바\t사아'
print(a)
b='타\n파하'
print(b)

#69
print('국가:\t대한민국')
print('수도:\t서울')
#70
name="Julia"
age=21
h=162
w=55
major='cs'
print('My name is',name)
print('My age is',age)
print('My height is',h)
print('My weight is',w)

#74
string="python"
print(string[0])
print(string[1])
print(string[5])
print(string[-1])
print(string[-3])
print(string[-6])

#75
mystr="ORANGE"
A=1
B=5
C=-3
D=-6
print(mystr[ A ])
print(mystr[ B ])
print(mystr[ C ])
print(mystr[ D ])

#76
string="python"
print("*"*5 + "정방향" +"*"*5)
print(string[0:2])
print(string[4:5])
print(string[-3:-1])
print(string[-6:-5])

#77
mystr="GOOD NIGHT"
print(mystr[1:3])
print(mystr[5:])
print(mystr[-3:-1])
print(mystr[2:4])

#78
string="NCT Dream"
print(string.upper())
print(string.lower())
print(string.title())
print(len(string))
print()
print(string.count("i"))
print(string.endswith("k"))
print(string.startswith("N"))

#84
a=input()
print("입력한 숫자는:", a)

#85
print("사용자 기본 정보")
name=input("이름을 입력하셈")
age=input("나이 입력하셈")
print("당신의 이름은",name,"당신의 나이는",age)

#86
a=int(input())
b=int(input())
print(a*b)

#87
a=input("이름을 입력하세요")
b=input("키를 입력하세요")
c=int(input("몸무게를 입력하세요"))
print(a,"의 키는",b,", 몸무게는",c)

#88
a,b=input("두 수를 입력하세요").split()
a=int(a)
b=int(b)
print("합은",a+b)

#89
name=input("이름은?")
print(len(name))

#90
f=input("first number")
s=input("second number")
if(f>s):
    result_f=True
if(f<=s):
    result_f=False
print(result_f)

f=input("first number")
s=input("second number")
print(f<=s)

#91
f=input("first number")
s=input("second number")
l=input("third number")
print(f+s==l)

#92
year=int(input("년도를 입력하세요:"))
print(year,"년 지수의 나이는",year-2017+20)

#93
a,b,c,d=input("네 수를 입력하세요").split()
a=int(a);b=int(b);c=int(c);d=int(d)
mean=(a+b+c+d)/4
var=((a-mean)**2+(b-mean)**2+(c-mean)**2+(d-mean)**2)/4
print("평균:",mean)
print("분산:",var)

#94
a=input("문장을 입력해:")
b=a.split()
k=0
for i in b:
    k+=1
print(k)

#95
count=[1,2,3,4,5]
fruits=['apple','pear','peach','melon']
print(count)
print(fruits)
print(count[1:3])
print(fruits[2])

#96
colors=['red','orange','yellow','green','blue','purple']
print(colors)
print(colors[3])
colors[3]='black'
colors=colors+['white']
print(colors)

#97
colors=['red','white','blue']
print(colors)
print(colors.index('yellow'))
colors.append('purple')
print(colors)
colors.extend(['white','black'])
print(colors)
boolean = 'red' in colors
print(boolean)

#98
colors=['red','yellow','blue']
print(colors.sort())
colors=['red','yellow','blue']
colors.sort()
print(colors)

colors.reverse()
print(colors)

print(colors.pop())
print(colors)

del(colors[0])
print(colors)

print(colors.count('yellow'))

#99
numbers=[14.26,5,426.3,0.221]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))
print(numbers)


#102
mylist=[[1,2],'samsumg',2.5,'A']
print(mylist[1][2])
print(mylist[1:3])

#103
list=['Hyundai']
list.append('Benz')
list.append('Toyota')
print(list)
list2=list
list2.remove('Toyota')
print(list2)

#105
my_list=['A',[5,2],'music']
print(len(my_list))
print(my_list[1])
my_list[1].append(10)
print(my_list.pop())
print(sum(my_list[1]))
print(my_list)

#106
sports=['soccer']
sports=sports+['baseball']+['hockey']
print(sports)
sports.insert(1,'tennis')
print(sports)
sports.remove('soccer')
sports.append('soccer')
print(sports)
sports.remove('tennis')
sports.append('tennis')
print(sports)
print(sports.pop())
sports.reverse()
print(sports)