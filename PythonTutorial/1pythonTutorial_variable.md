### python基础教程--变量
>变量用于存储可能发生变化的数据，例如您在游戏中的得分。 变量可以有不同的 数据类型。数据类型包含整数，浮点数，字符串和布尔值。

#### 变量名称
* 应该描述它们包含的内容，以便您的代码更容易被理解
* 必须以一个字母开头，而非数字
* 不能包含任何空格
* 不能与 Python 关键字相同，例如 True、if 或者 while
* 区分大小写：score 是与 Score 不同的变量

#### 分配数字变量
在程序开始时，使用= 符号将变量设置为其初始值：
``` python
count = 0
```

####  更改数字变量
您可以通过加、减、乘和除来修改数字变量：
``` python
# 数字变量相加
score = 2
score = score+ 5
print('score当前的值:'+score)
 
# 数字变量相减
score = 7
score = score-5
print('score当前的值:'+score)

# 数字变量相乘
score = 2
score = score*5
print('score当前的值:'+score)

# 数字变量相除
score = 10
score =score/2
print('score当前的值:'+score)

```

#### 分配字符串
> 一组单词或符号称为字符串。 在字符串的内容周围加上引号：
``` python
name = 'hello word!'
print(name)

```
可以在字符串前后使用单引号'或双引号"，但要保持一致。 我们在示例中使用单引号是因为它们更容易输入，而且双引号可能会被误认成两个单引号。

#### 布尔变量
布尔变量只有两个值： True (真) 或 False (假)。 它们对于向您的程序添加控制很有用：
``` python
running = True
if running == True:
    print('程序正在运行')
    running = False
else:
    print('程序没有运行')
    running = True

#再次判断当前程序执行的状态
if running == True:
    print('程序正在运行')
    running = False
else:
    print('程序没有运行')
    running = True
 
```
本例使用了一个名为running的布尔变量。 该变量的值在程序运行时更改。  
请注意， True 和 False 必须以大写字母开头。


