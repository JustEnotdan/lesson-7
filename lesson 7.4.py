import os

ch = {}
a100 = 0
a1000 = 0
a10000 = 0

folder = r'C:\Users\Daniil\PycharmProjects\pythonProject\venv\lesson 7'
files = [item for item in os.listdir(folder)]

for i in files:
    if os.stat(i).st_size <= 100:
        a100 += 1
    elif os.stat(i).st_size > 100 and os.stat(i).st_size <= 1000:
        a1000 += 1
    elif os.stat(i).st_size > 1000 and os.stat(i).st_size <= 10000:
        a10000 += 1
    a = {"100": a100}
    ch.update(a)
    a = {"1000": a1000}
    ch.update(a)
    a = {"10000": a10000}
    ch.update(a)

print(ch)
