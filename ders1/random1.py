import random as rnd

print(rnd.random()) # random fonksiyonu 0 ile 1 arası 
print(rnd.randint(50,100)) # bir aralıktan tam sayı ve

oyuSecenekleri = ["taş","kağıt","makas"]
print(rnd.choice(oyuSecenekleri))

print(dir(rnd))
help(rnd.shuffle)