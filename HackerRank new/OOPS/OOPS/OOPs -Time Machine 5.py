class Time:
    def __init__(self):
        self.h = int(input())
        self.m = int(input())
        self.s = int(input())


jethro = Time()
jairo = Time()

sec = jethro.s+jairo.s
min = jethro.m+jairo.m
har = jethro.h+jairo.h

if sec >= 60:
    min = min+(sec//60)
    sec = sec % 60

if min >= 60:
    har = har+(min//60)
    min = min % 60


print(f"Time after add:{har}:{min}:{sec}")
