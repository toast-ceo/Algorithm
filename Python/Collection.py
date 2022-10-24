# Collection

# List, Set, Tuple, Dictionary

# List, Tuple: 중복이 있고 순서도 있음
# Set: 중복이 없고 순서도 없음

l = [3, 2, 1, 3, 2, 1]
s = {3, 2, 1, 3, 2, 1}
t = (3, 2, 1, 3, 2, 1)

## index로 접근

l[0]
#### s[0]

# List, Set: 변경 가능 (unhashable)
# Tuple: 변경 불가능 (hashable)

## index로 할당

l[0] = 9
#### s[0] = 9

# 요소 추가

l.append(4)
s.add(4)

## remove 함수는 값으로 요소 제거

l.remove(1)
s.remove(1)

## del 키워드는 인덱스로 요소 제거

del l[0]
#### del s[0]

## pop 함수는 요소를 리턴하며 제거

### list 에서 pop 함수는 마지막 요소를 리턴하며 제거

l.pop()
l.pop(0)

### set 에서 pop 함수는 첫 번째 요소를 리턴하며 제거

s.pop()

## insert 함수는 index로 요소 추가
l.insert(1, 100)

# List, Tuple: unhashable 객체도 요소가 될 수 있음
# Set: hashable 객체만 요소가 될 수 있음

l = [ [1, 2, 3], {1, 2, 3}, (1, 2, 3) ]
t = ( [1, 2, 3], {1, 2, 3}, (1, 2, 3) )
#### s  = { [1, 2, 3] }
#### s = { {1, 2, 3} }
s = { (1, 2, 3) }

# Dictionary (Key-Value coding)
# Key: hashable
# Value: unhashable

d = { 1: '1', '2': 2 }

d[1] = '100'

#### d[[1]] = 3
#### d[{1}] = 3
d[(1, 2)] = 3

d[(1, 2)] = { 3 }

# frozenset

fs = frozenset([1, 2, 3])
d[fs] = 5


# Set

a = { 1, 2, 3 }
b = { 3, 4, 5 }

a & b
a | b

a.intersection_update(b)
a.update(b)


# Comprehension

l = [x * x for x in [1, 2, 3]]
s = {x * x for x in [1, 2, 3]}
s = { x: y for x in [1, 2] for y in {1, 2} }


# Generator

g = ( x * x for x in [1, 2, 3] )
next(g)
next(g)
next(g)
#### next(g)

## yield 키워드를 사용하는 모든 함수는 generator
## 모든 generator는 lazy factory

def test_generator():
    'A'
    yield 'a'
    'B'
    yield 'b'

g = test_generator()
next(g)
next(g)
#### next(g)

def test_generator():
    l = [1, 2]
    yield from l

g = test_generator()
next(g)
next(g)
#### next(g)

g = test_generator()
for x in g:
    x


# Iterable, Iterator
# 모든 generator는 iterator

l = [1, 2] # iterable
type(l)

g = iter(l) # iterator
type(g)

next(g)
next(g)
#### next(g)


# infinite sequence

from itertools import cycle, islice

c = cycle(['a', 'b'])
next(c)
next(c)
next(c)

c = cycle(['a', 'b', 'c'])
l = islice(c, 1, 6)

for x in l:
    x


# range
r = range(1, 10, 2)
list(r)

i = iter(r)
next(i)


# iterable, iterator 클래스 구현

# 피보나치 수
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# 피보나치 수의 7번 째 값을 가져오라!
# 정답 = 13

# __ 내장된 특수한 함수와 변수
# __iter__, __next__ 함수를 오버라이딩하면
# iterable 한 객체를 생성하는 클래스가 됨

class fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    # iterable
    def __iter__(self):
        return self

    # iterator
    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

f = fib()
list(islice(f, 6, 7))[0]


# _, __의 의미

for _ in range(3):
    'hello'

a, _, b, _ = (1, 2, 3, 4)

## _, weak private

# #### func.py
# def _f():
#     pass

# #### test.py
# from func import *
# _f() # 함수를 찾을 수 없음

# import func
# func._f() # 성공


# __, name mangling
# python은 private 접근 제한자가 없음
# 외부에서 사용하는 것을, 또는 오버라이딩 하는 것을 어렵게 만듬

class Test:
    def __init__(self):
        self.a = 1
        self.__b = 3

t = Test()
t.a
#### t.__b
t._Test__b


# zip

z = zip([1, 2, 3], [4, 5, 6])
list(z)


# reversed

r = reversed([1, 2, 3])
for x in r:
    x


# enumerate

e = enumerate([10, 20, 30])
for i, x in e:
    i, x


# 연산자 오버라이딩

class Test:
    l = range(1, 10, 2)
    
    def __init__(self, v):
        self.v = v
    
    # __mul__, __truediv__, __mod__
    def __add__(self, other):
        return self.v + other.v
    
    def __sub__(self, other):
        return self.v - other.v
    
    # eq - equal (=)
    # ne - not equal (!=) 
    # lt - little (<)
    # gt - greater (>)
    # le - little or equal (<=)
    # ge - greater or equal (>=)
    def __lt__(self, other):
        return self.v < other.v

    def __eq__(self, other):
        return self.v == other.v
      
    # __contains__, __len__
    def __getitem__(self, index):
        return self.l[index]
    
    # 객체를 설명하는 문자열 리턴 (가공)
    def __str__(self):
        return '파이썬 공부합시다.'
    
    # representation
    # 객체를 표현하는 문자열 리턴
    def __repr__(self):
        return '프로그래밍 공부합시다.'

t1 = Test(5)
t2 = Test(5)

t1[1]
str(t1)

t1.v
t2.v

t1.v + t2.v
t1 + t2
t1 - t2
t1 < t2
t1 > t2
t1 == t2