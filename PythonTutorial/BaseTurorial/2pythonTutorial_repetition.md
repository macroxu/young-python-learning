### python基础教程--循环
>循环重复部分代码。 使用循环也可以称为“iteration”（迭代）或“repetition”（重复）。

#### 缩进
Python 使用缩进来显示循环内部和外部的指令。 例如，下面的代码将打印三次“循环执行的代码”，然后打印“和循环无关的代码”：
``` python
for i in range(3):  
    print('循环执行的代码')

print('和循环无关的代码')
```

#### While 循环：无限的循环
无限或“永远”循环，保持一个程序运行。
``` python
while True:
    print('执行代码')

```

#### While 循环：条件
“for”循环是计数控制的循环。 它们重复一段代码固定的次数。
``` python
for i in range(3):  
    print('第' +str(i)+'执行')

```

####  嵌套循环
你可以将循环放入循环中。 这被称为“嵌套”。
``` python
for y in range(5):
    for x in range(5):
        print('班级:'+str(x)+'， 学号:'+str(y))

```

####   跳出循环
您可以使用 逻辑 和 break 来跳出循环。
``` python
# 循环 hello 字符串 当发现字符为l时，跳出循环
for letter in 'hello':
    if letter == 'l':
        break
    print(letter)
    sleep(1000)
```