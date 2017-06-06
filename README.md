```

# AI2-2017
String1.py

===== RESTART: C:\Users\student.INFORMATYKA\Documents\Python\String1.py =====
donuts
 OK  got: 'Number of donuts: 4' expected: 'Number of donuts: 4'
 OK  got: 'Number of donuts: 9' expected: 'Number of donuts: 9'
 OK  got: 'Number of donuts: many' expected: 'Number of donuts: many'
 OK  got: 'Number of donuts: many' expected: 'Number of donuts: many'
both_ends
 OK  got: 'spng' expected: 'spng'
 OK  got: 'Helo' expected: 'Helo'
 OK  got: '' expected: ''
 OK  got: 'xyyz' expected: 'xyyz'
fix_start
 OK  got: 'ba**le' expected: 'ba**le'
 OK  got: 'a*rdv*rk' expected: 'a*rdv*rk'
 OK  got: 'goo*le' expected: 'goo*le'
 OK  got: 'donut' expected: 'donut'
mix_up
 OK  got: 'pox mid' expected: 'pox mid'
 OK  got: 'dig donner' expected: 'dig donner'
 OK  got: 'spash gnort' expected: 'spash gnort'
 OK  got: 'fizzy perm' expected: 'fizzy perm'
>>> 

String2.py

===== RESTART: C:\Users\student.INFORMATYKA\Documents\Python\String2.py =====
verbing
 OK  got: 'hailing' expected: 'hailing'
 OK  got: 'swimingly' expected: 'swimingly'
 OK  got: 'do' expected: 'do'
not_bad
 OK  got: 'This movie is good' expected: 'This movie is good'
 OK  got: 'This dinner is good!' expected: 'This dinner is good!'
 OK  got: 'This tea is not hot' expected: 'This tea is not hot'
 OK  got: "It's bad yet not" expected: "It's bad yet not"
front_back
 OK  got: 'abxcdy' expected: 'abxcdy'
 OK  got: 'abcxydez' expected: 'abcxydez'
 OK  got: 'KitDontenut' expected: 'KitDontenut'
>>> 

List1.py

====== RESTART: C:\Users\student.INFORMATYKA\Documents\Python\list1.py ======
match_ends
 OK  got: 3 expected: 3
 OK  got: 2 expected: 2
 OK  got: 1 expected: 1
front_x
 OK  got: ['xaa', 'xzz', 'axx', 'bbb', 'ccc'] expected: ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
 OK  got: ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'] expected: ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
 OK  got: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'] expected: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
sort_last
 OK  got: [(2, 1), (3, 2), (1, 3)] expected: [(2, 1), (3, 2), (1, 3)]
 OK  got: [(3, 1), (1, 2), (2, 3)] expected: [(3, 1), (1, 2), (2, 3)]
 OK  got: [(2, 2), (1, 3), (3, 4, 5), (1, 7)] expected: [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
>>> 

List2.py

====== RESTART: C:\Users\student.INFORMATYKA\Documents\Python\list2.py ======
remove_adjacent
 OK  got: [1, 2, 3] expected: [1, 2, 3]
 OK  got: [2, 3] expected: [2, 3]
 OK  got: [] expected: []
linear_merge
  OK  got: ['aa', 'bb', 'cc', 'xx', 'zz'] expected: ['aa', 'bb', 'cc', 'xx', 'zz']
  OK  got: ['aa', 'bb', 'cc', 'xx', 'zz'] expected: ['aa', 'bb', 'cc', 'xx', 'zz']
  OK  got: ['aa', 'aa', 'aa', 'bb', 'bb'] expected: ['aa', 'aa', 'aa', 'bb', 'bb']
>>> 


Lab1.py i Lab2.py (Początkowe zadania pokrywają się)

Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: C:/Users/student.INFORMATYKA/Desktop/testy.py ===========
>>> helloWorld()
Hello, World!
>>> ticTac()
   |  |   
 --------
   |  |   
 --------
   |  |  
>>> superTicTac()
  |  |  H  |  |  H  |  |
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |
========+========+========
  |  |  H  |  |  H  |  |
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |
========+========+========
  |  |  H  |  |  H  |  |
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
>>> fizz()
234168
>>> collatz(13)
10
>>> converter()
Temperatura F? 212
100.0 stopni Celsjusza
>>> lists()
[1, 0, 0]
['a', '', '']
[[1], [1], [1]]
>>> lists2()
[1, 0, 0]
['a', '', '']
[[1], [], []]
>>> gcd(8,32)
8
>>> flip_dict({"CA": "US", "NY": "US", "ON": "CA"})
{'CA': ['ON'], 'US': ['CA', 'NY']}
>>> comprehensions_read()
[None, None, None]
[[3, 2, 1, 12], ['a', 'b', 'c', 'aaaa'], [('do',), ['re'], 'mi', ('do', 'do', 'do', 'do')]]
['Y', 'O', 'N']
{8, 2, 3, 5}
>>> comprehensions_write()
2*x +1
[0, 1, 2, 3]
[1, 3, 5, 7]


Podzielniki 3
[3, 5, 9, 8]
[True, False, True, False]


Zaczyna się na TA
['TA_sam', 'TA_guido', 'student_poohbear', 'student_htiek']
['sam', 'guido']


Duże pierwsze litery
['apple', 'orange', 'pear']
['A', 'O', 'P']


Jeżeli jest litera 'p'
['apple', 'orange', 'pear']
['apple', 'pear']


Owoc z jego długością krotka
['apple', 'orange', 'pear']
[('apple', 5), ('orange', 6), ('pear', 4)]


Owoc z jego długością (słownik)
['apple', 'orange', 'pear']
{'apple': 5, 'pear': 4, 'orange': 6}
>>> 

Lab3.py

>>> print_two(1,2)
Arguments: 1 and 2

>>> print_two_test()
Arguments: 4 and 1
Arguments: 4 and 1
Arguments: 4 and 1
>>> 

>>> keyword_args(a=4)
a: 4
b: 1
c: X
d: None
>>> 

>>> print_keyword_args()
a: 5
b: 1
c: X
d: None
a: 5
b: 1
c: X
d: None
a: 5
b: 8
c: X
d: None
a: 5
b: 2
c: 4
d: None
a: 5
b: 0
c: 1
d: None
a: 5
b: 2
c: 4
d: 8
a: 1
b: 1
c: 7
d: None
a: 5
b: 2
c: []
d: 5
a: 1
b: 1
c: 7
d: None

>>> variadic()
Positional: ()
Keyword: {}

>>> print_variadic()
Positional: (2, 3, 5, 7)
Keyword: {}
Positional: (1, 1)
Keyword: {'n': 1}
Positional: ()
Keyword: {}
Positional: ()
Keyword: {'cs': 'Computer Science', 'pd': 'Product Design'}
Positional: (5, 8)
Keyword: {'k': 1, 'swap': 2}
Positional: (8, 3, 4, 5)
Keyword: {'k': 1, 'a': 5, 'b': 'x'}
Positional: (8, 3, 4, 5)
Keyword: {'k': 1, 'a': 5, 'b': 'x'}
Positional: (3, 4, 5, 8, 4, 1)
Keyword: {'k': 1, 'a': 5, 'b': 'x'}
Positional: ({'a': 5, 'b': 'x'}, 'a', 'b')
Keyword: {'a': 5, 'b': 'x'}

>>> all_together(x=1,y=2)
x: 1
y: 2
z: 1
nums: ()
indent: True
spaces: 4
options: {}

>>> print_all_together()
x: 2
y: 5
z: 7
nums: (8,)
indent: False
spaces: 4
options: {}
x: 2
y: 5
z: 7
nums: (6,)
indent: None
spaces: 4
options: {}
x: {'x': 0, 'y': 1}
y: 0
z: 1
nums: (2, 3, 4, 5, 6, 7, 8, 9)
indent: True
spaces: 4
options: {}
x: [1, 2]
y: {3: 4}
z: 1
nums: ()
indent: True
spaces: 4
options: {}
x: 8
y: 9
z: 10
nums: (2, 4, 6)
indent: True
spaces: 0
options: {'a': [4, 5], 'b': 'x'}
x: 8
y: 9
z: 2
nums: (4, 6, 'z')
indent: True
spaces: 0
options: {'a': [4, 5], 'b': 'x'}

>>> speak_excitedly("Przykładowy tekst")
'Przykładowy tekst!'

>>> average(1,2,3,4,5)
3.0

>>> test_make_table()
=========================
| first_name  |     Sam |
| last_name   | Redmond |
| shirt_color |    pink |
=========================
==================================
|            song |    Style     |
| artist_fullname | Taylor $wift |
|           album |     1989     |
==================================
