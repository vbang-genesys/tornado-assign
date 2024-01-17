import time

def coro():
    file = "vidooshkumarbang"
    time.sleep(5)

    while True:
        key = (yield)
        if key in file:
            print("there")
        else:
            print("not there")

coroutine = coro()
print("init")
next(coroutine)
print("next")
coroutine.send("vidoosh")
coroutine.send("bang")
coroutine.send("vbang")