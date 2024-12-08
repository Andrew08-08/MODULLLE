from def2 import hello
from def1 import good_word
print(hello('Nick'))
print(good_word('Sena'))

def alien(x):
    global p
    p = x + 1
    return p

p = 9
a = alien(99)
print(p)
print(a)