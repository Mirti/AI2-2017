import operator
import functools

def test_lambda():
  print((lambda val: val ** 2)(5)) 
  print((lambda x, y: x * y)(3, 8)) 
  print((lambda s: s.strip().lower()[:2])('  PyTHon'))  

def test_map():
    print(list(map(int, ('10110', '0xCAFE', '42'), (2, 16, 10))))
    print(list(map(int, ['12', '-2', '0'])))
    print(list( map(len, ['hello', 'world'])))
    print(list(map(lambda x: x[::-1], ['hello', 'world'])))
    print(list(map(lambda n: (n, n ** 2, n ** 3), range(2, 6))))
    print(list(map(lambda l, r: l * r, range(2, 5), range(3, 9, 2))))

def test_filter():
    print(list((filter(lambda x: int(x) >= 0, ['12', '-2', '0']))))
    print(list( filter(lambda x: x == 'world', ['hello', 'world'])))
    print(list( filter(lambda x: x[0] == 'S', ['Stanford', 'Cal', 'UCLA'])))
    print(list(filter(lambda n: n % 3 == 0 or n % 5 == 0, range(20))))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(*args):
    return functools.reduce(lambda x, y: x * y / gcd(x, y), args)


def test_operator():
    print(operator.add(1,2))
    print(operator.mul(3, 10))
    print(operator.pow(2, 3))
    print(operator.itemgetter(1)([1, 2, 3]))

def fact(n):
    return functools.reduce(operator.mul, range(1,n+1))

def test_ord():
    words = ['pear', 'cabbage', 'apple', 'bananas']
    print(min(words))  
    words.sort(key=lambda s: s[-1])  
    print(words) 
    print(max(words, key=len))
    print(min(words, key=lambda s: s[1::2]))

def alpha_score(upper_letters):
    """Computers the alphanumeric sum of letters in a string.
    Prerequisite: upper_letters is composed entirely of capital letters.
    """
    return sum(map(lambda l: 1 + ord(l) - ord('A'), upper_letters))

alpha_score('ABC')  # => 6 = 1 ('A') + 2 ('B') + 3 ('C')

def two_best(words):
    words.sort(key=lambda word: alpha_score(filter(str.isupper, word)), reverse=True)
    return words[:2]

def test_two_best():
    print(two_best(['hEllO', 'wOrLD', 'i', 'aM', 'PyThOn']))


def float_Control(score):
    if score == 1:
        return "Winner"
    elif score == -1:
        return "Loser"
    else:
        return "Tied"

def replace_Return(*args):
  echo = lambda arg: arg  # In practice, you should never bind lambdas to local names
  cond_fn = lambda x: (x==1 and echo("one")) \
                 or (x==2 and echo("two")) \
                 or (echo("other"))

def replace_Loop(lst,func):
  map(func,lst)


def iterator_Consumption():
  it = iter(range(100))
  print(67 in it)  # => True
  print(next(it))  # => 68
  (37 in it)  # => Error
  (next(it))  # => StopIteration
  
