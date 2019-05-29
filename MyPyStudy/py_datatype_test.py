#一 整数、浮点数、字符串、布尔类型、空值

a = 1
b = 2

c = 1.234
d = 4.3

print(a,b,c,d)

e = 'i\'m ok'
f = '''你好
i am fine
'''
g = """在京东一周了
感觉还好
"""

print(e)
print(f)
print(g)

print('\\t\\')
print(r'\\t\\')
#\t\
#\\t\\

t = True
f = False

print(t or f,t and f,not t,not f)

null = None

print(null)

# 二 变量

x = 123
y = x
x = 456
print(x,y,x+y)

# 三 list tuple

## list
p=['oracle','mysql','db2']
l = []
l.append('Python')
l.append('Java')
print(l,l.__len__())
l[1] = 'scala'
print(l,l.__len__())
l.pop()
print(l,l.__len__())
l.pop(-1)
print(l,l.__len__())
l.append(p)
l.append('SQL Server')
print(l,l.__len__())
# [['oracle', 'mysql', 'db2'], 'SQL Server'] 2

## tuple

