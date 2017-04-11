def helloWorld():
    print("Hello, World!")

def ticTac():
    x = '   |  |  '
    y = '\n --------'
    print(x,y)
    print(x,y)
    print(x)
    
def superTicTac():
    text = """\
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
  |  |  H  |  |  H  |  |  \
"""
    print (text)

def fizz():
    licznik = 0
    for i in range(1,1002):
        if i % 3 == 0 or i % 5 == 0:
            licznik += i
    return licznik

def collatz(n):
    licznik = 1
    while n > 1:
        if n%2 == 0:
            n /=2
        else:
            n =3*n +1
        licznik +=1
    return licznik

def converter ():
    tempFar =float(input("Temperatura F? "))
    celsjusz= (tempFar-32)/1.8
    print (celsjusz ,"stopni Celsjusza")

def lists():
    s = [0] * 3
    s[0] += 1
    print(s)
    
    s = [''] * 3
    s[0] += 'a'
    print(s)
    
    s = [[]] * 3
    s[0] += [1]
    print(s)

def lists2():
    s = [0] * 3
    s[0] += 1
    print(s)
    
    s = [''] * 3
    s[0] += 'a'
    print(s)
    
    s = [[]] * 3
    s[0] = s[0] + [1]
    print(s)


def gcd(x, y):
     while y:
        x, y = y, x % y
     return x

def flip_dict(d):
    out = {}
    for key, value in d.items():
        if value not in out:
            out[value] = []
        out[value].append(key)
    return out

def comprehensions_read():
    [x for x in [1, 2, 3, 4]]
    [n - 2 for n in range(10)]
    [k % 10 for k in range(41) if k % 3 == 0]
    [s.lower() for s in ['PythOn', 'iS', 'cOoL'] if s[0] < s[-1]]

    arr = [[3,2,1], ['a','b','c'], [('do',), ['re'], 'mi']]
    print([el.append(el[0] * 4) for el in arr])
    print(arr)

    print([letter for letter in "pYthON" if letter.isupper()])
    print({len(w) for w in ["its", "the", "remix", "to", "ignition"]})

def comprehensions_write():
    print("2*x +1")
    lista = [0, 1, 2, 3]
    print (lista)
    print([2 * x + 1 for x in lista])\
             
    print( "\n" )
    print("Podzielniki 3")
    lista = [3, 5, 9, 8]
    print (lista)
    print([x % 3 == 0 for x in lista])
    
    print( "\n" )
    print("Zaczyna się na TA")
    lista = ["TA_sam", "TA_guido", "student_poohbear", "student_htiek"]
    print (lista)
    print([nazwa[3:] for nazwa in lista if nazwa.startswith('TA_')])

    print( "\n" )
    print("Duże pierwsze litery")
    lista = ['apple', 'orange', 'pear']
    print (lista)
    print([owoc[0].upper() for owoc in lista])

    print( "\n" )
    print("Jeżeli jest litera 'p'")
    lista = ['apple', 'orange', 'pear']
    print (lista)
    print([owoc for owoc in lista if 'p' in owoc])

    print( "\n" )
    print("Owoc z jego długością krotka")
    lista = ['apple', 'orange', 'pear']
    print (lista)
    print([(owoc, len(owoc)) for owoc in lista])

    print( "\n" )
    print("Owoc z jego długością (słownik)")
    lista = ['apple', 'orange', 'pear']
    print (lista)
    print({owoc:len(owoc) for owoc in lista})

    

  
