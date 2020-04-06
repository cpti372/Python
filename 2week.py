#107
myTup=(1,2,3)
print(myTup)

myTup=('this is tuple',23.21,(1,2,3))
print(myTup)

myTup='소괄호 없이도 튜플',1.22,'을 만들수 잇음'
print(myTup)

memoryview

#108
my=('a','b','c','d')
print(my)
print(my[1])
Tu_1=(1,2,3)
print(Tu_1*2)
Tu_2=(10,20,[1,2,3])
Tu_2[2][1]=4
print(Tu_2)

#109
Tu_3=(1,2,3,4,5,6,7,8,9,10)
tot=0
for i in Tu_3:
    tot+=i
print(tot)

#110
myTup2=('kim','lee','oark','choid')
print(myTup2)
print(sorted(myTup2))
print(myTup2+('oh','i'))
print(myTup2)
print(type(myTup2))

#111
a=(10,20,30,20,30,40)
print(a.index(10),a.index(20),a.index(30))
print(a.count(20),a.count(30),a.count(40))
print(10 in a)
b=tuple(i for i in range(10) if i%2==0)
print(b)

#112
x={'a':10,'b':20,'c':30}
print('초기상태:',x)
x['d']=40
print('d추가:',x)
x['b']=40
print('b 수정:',x)
del(x['c'])
print(x)
x['a']=20
print(x)

#113
list1=[['a','b'],['c','d']]
print(dict(list1))
list2=['12','34','56']
print(dict(list2))

#114
ht={'chenle':178,'jisung':180}
print(ht.get('chenle'))
ht['jeno']=176
print(ht)
a=ht.pop('jeno') #키 값을 삭제 
print(a,ht)
ht['robin']=146
b=ht.popitem()
print(b,ht)

nht={'jaemin':175,'renjun':174}
ht.update(nht)#딕셔널 데이터를 더하여 갱신
print(ht)

print(ht.keys())#사전의 키들을 리턴 
print(ht.values())#사전의 값들을 리턴
print(ht.items())#키와 값을 리턴

#115
chenle={'ht':'178cm','age':21,'birth':'11월','group':'nctdream'}
print('chenle','is',chenle.get('ht'))
print('chenle belongs to',chenle.get('group'))

#116
chenle={'korean':100,'English':98,'math':98,'science':98}
average=(chenle['korean']+chenle['math'])
print(average)

#118
nct={'chenle':'vocal','js':'dance','mark':'leader'}
var=list(nct.keys())[0]
result=nct[var]
input('nct 이름:')
print('{}is {} player'.format(var,result))

#119
chengji={'won':50,'hoo':60,'su':100}
average=(sum(chengji.values())/len(chengji))
print(average)

#120
myset={1,2,3}
print(myset)
print(type(myset))
myset={'ice',1.2,(1,3,5)}
print(myset)
myset={1,2,3,2,3,2,2}
print(myset)

#121
a={1,2,3,5,6,8}
b={1,3,4,5,6,7}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))#두 셋의 비 공통요소 

#122
myset={1,3,5}
print(myset)
myset.add('A')
print(myset)
myset.update({1,3},[2,3]) 
print(myset)#{1,2,3,5,'A'}
print()
print(myset.pop())
print(myset)
myset={'apple','melon','strawberry','grape'}
print(myset)
print()
myset.discard('apple')
print(myset)
myset.remove('grape')
print(myset)

#123
A={10,20,70,90}
print({10,20,70,80,90}.issuperset(A)) #앞에게 두에 요소 하나라도 가지고 있니
print({20,30,50}<=A) #앞에꺼에 속한 요소가 뒤에꺼보다 작은지

#124
animals={'cat','dog'}
print('cat'in animals)
print('fish' in animals)
animals.add('fish')
print(len(animals))
animals.add('cat')
print(len(animals))

#125
myset=set([1,2,3,4,5])
print(myset)
myset.update({7,11,'Ferran'})
myset.remove(1)
print(myset)

#126
A={1,3,4,6}
B={2,3,5,6}
print(A^B)
print(A|B)
print((A^B)|(A&B))
print(A<={1,3,4,5,6})

#126
a={1,2,4,8,16}
b={1,2,15,3,10,5,6,30}
print(a&b)

#128
num=list((input().split(' ')))
for i in range(len(num)):
   num[i]=int(num[i])
max_num=max(num)
print(max_num)

#129
a=['aloha','b','cdfdfdfd','defee','edfdfdf','fffff','ggggg','hhh','e']
b=[]
for i in a:
    if(len(i)==5):
        b.append(i)
print(b)

#130
list1=['a','c','d','b','e']
print(list1)
l=sorted(list1)
print(list(reversed(l)))

#131
a={'math':76,'science':89,'eng':93}
b={'math':88,'science':87,'eng':100}
c={'math':86,'science':93,'eng':82}
av_1=(sum(a.values())/len(a))
av_2=(sum(b.values())/len(b))
av_3=(sum(c.values())/len(c))
print(av_1,int(av_2),av_3)

