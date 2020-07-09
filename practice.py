# print('Hello'+'World')

#문자열은 리스트처럼 인덱스 사용 가능.

#문자열 슬라이싱 -> b = a[x:y]

# a = 'Hello'
# b = a.split('l')
# c = a.replace('e','E')

# d = '안녕하세요\n'
# print(d)
# print('포맷팅 {}, {}'.format({d},b))
# print(f'포매팅 {b}')

#bool 자료형
# if(0) :
#     print('true')
# else :
#     print('false')

# 리스트
# a = [1,'Hi',[1,2,3]]

# for i in a :
#     print(type(i))

#     if(type(i)=='<class \'int\'>') :
#         print(i)

#  딕셔너러ㅣ
# a = {'name' : '천희국', 'address' : '광주'}

# print(a['name'])
# print(a['address'])
# print(a.keys())
# print(a.values())
# print(a.items())

# if 문

# x = [i**2 for i in range(1, 11)]

# print(x)

# check = input('1 or others : ')

# if (check) :
#     print('true')
# else :
#     print('false')

# 함수 
# def 함수명(인자) :
#     지역변수 = 값
#     return 지역변수

# 클래스
# class Pet :
#     def __init__(self,name, age) : #생성자
#         self.name = name
#         self.age = age
#         print('Pet 등록 완료!')
    
#     def eat(self, food) :
#         print(f'{food}을(를) 먹습니다.')
    

# dog = Pet('멍멍이',3)

# print(dog.name)
# print(dog.age)

# dog.eat('밥')

# class Dog(Pet) :
#     pass

# dog1 = Dog('바둑이',2)
# print(dog1.name)
# print(dog1.age)
# dog1.eat('밥')


# class Rectangle :
    
#     def __init__(self, h, v) :
#         self.h = h
#         self.v = v
    
#     def R_area(self) :
#         R_area = self.h*self.v
#         return R_area

#     def R_round(self) :
#         R_round = (self.h+self.v)*2
#         return R_round

# a = Rectangle(5,4)
# print(a.R_area(), a.R_round())

# # -------------------------------------- 

# class Animals() :

#     def __init__(self,name,animal) :
#         self.name = name
#         self.animal = animal
#         print('동물 생성!')


# class Cat(Animals) :

#        def sounds(self) :
#         print('야옹!')

# class Dog(Animals) :

#        def sounds(self) :
#         print('왈왈!')

# cat1 = Cat('고양이','고양이')
# cat1.sounds()

# dog1 = Dog('강이지','강아지')
# dog1.sounds()

# def fivonacci(n) :

#     global fi_list

#     if n == 0 :
#         fi_list[0] += 1
#         return 0
#     elif (n == 1) :
#         fi_list[1] += 1
#         return 1
#     else :
#         return fivonacci(n-1) + fivonacci(n-2)


# fi_list = [0,0]

# # n = int(input("n의 값을 입력하세요 : "))

# for i in range(1,11) :
#     fi_list = [0,0]
#     print(f'값 : {fivonacci(i)}\n0의 개수 : {fi_list[0]}\n1의 개수 : {fi_list[1]}')
#     print('')


#for range input
#모래시계 별 출력

# n = 5
# m = (n*2)-1

# # print('*'*i)
# for i in range(0,n,1) :
#     print(' '*i, end='')
#     j = m-(2*i)
#     print('*'*j)

# for i in range(n-1,-1,-1) :
    
#     j = m-(2*i)
#     if(j==1) :
#         continue
#     print(' '*i, end='')
#     print('*'*j)

# 3번 문제
text = '''
<div class="basicList_info_area__17Xyo">
    <div class="basicList_title__3P9Q7">
        <a href="https://adcr.naver.com/adcr?x=dGuv3Yn2btkv071HS0a2cP///w==kILthdCb5qBu2MuFkWS611uPOTsos2EtlhewKBh0962Tc4MJLa1pPrltk7e65InzI6YTE/AncB5KWFqnGf47ol3FtuJlDDH/HEtxWOv30PjQyh7jLytBlmWPZv85G1RZh0xcFoKRbYLeHpppS73HfkjAcvxePU51yOObls8Yoy3Z7C7yPJKBDVhiHYat7I7qWYWA0EnVOyXB3AQn2hOlIvZtw6snYm1LjBK9h/yZd/RRXmFqqBEiIYYAGAH+d53AH1WSJEbKGCWteZ97fLLsVRJtPKu7utvOffK6lr5rvjtGAVip18WDVQQa7PcjiyPK1EisLeqPA506NIyq8Zzac/qdAoTIWgvpwSmonmPGG9wHf63XpDZDJkpf5bnmva0WZQqIqbrcrm/Bm8kZmyKUFHCFEfxUN6feCBQD8SO/h0U2IFbYZyjFRoZaAVwoYasx/RP4x31sWK3HpWoDOxpHnHugPR+uRTL8LaUi9KBwwEYPHaCHV+PgfQY0OknL/0JMnfSlmpjJWpwONko83stPJlbgFL1Tw97+RIDbfabESogosOuS532zmZSseqDPacIBk58vkEq60UYKSfTrjlN5IQ0JGLtk3QPNCkw3Il0fvNZRkl+xPw3qGhXGVEYoqqg33GWTZfg0zDIPmaxc5zr36e58XwMAxYza8NJCveLaci2R/q8yOd9R6vCzDQTed+qYIhV3lDocopYpLdwDsm136NA==" target="_blank" class="basicList_link__1MaTN" rel="noopener" data-nclick="N=a:lst*B.title,i:17840594493,r:3" title="한성컴퓨터 TFG AX9466">
            한성컴퓨터 TFG AX9466
        </a>
    </div>
</div>
<div class="basicList_price_area__1UXXR">
    <strong class="basicList_price__2r23_">
        <span>
            <span class="price_num__2WUXn">839,000원</span>
        </span>
    </strong>
</div>
<div class="basicList_desc__2-tko">
    <div class="basicList_detail_box__3ta3h">
        <a href="#" class="basicList_detail__27Krk" data-nclick="N=a:lst*B.modelvalue">
            CPU : 코어i5-9400F
        </a>
        <a href="#" class="basicList_detail__27Krk" data-nclick="N=a:lst*B.modelvalue">
            램용량 : 8GB
        </a>
        <a href="#" class="basicList_detail__27Krk" data-nclick="N=a:lst*B.modelvalue">
            SSD용량 : 256GB
        </a>
        <a href="#" class="basicList_detail__27Krk" data-nclick="N=a:lst*B.modelvalue">
            그래픽 : 지포스GTX1660
        </a>
    </div>
</div>
<div class="basicList_etc_box__1Jzg6">
    <span class="basicList_etc__2uAYO">
        등록일 <!-- -->2019.03.
    </span>
</div>
'''

# text = text.find()


# print(text.find('9466'))
print(text.find('램용량'))

name = text[1005:1021]
price = text[1228:1236]
desc = []
desc.append(text[1463:1479])
desc.append(text[1593:1602])
print(name)
print(price)
print(desc)