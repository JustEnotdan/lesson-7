import os

names = ['settings', 'mainapp', 'adminapp', 'authapp']
for i in names:
    a = os.path.join('my_project', i)
    if not os.path.exists(a):
        os.makedirs(a)
