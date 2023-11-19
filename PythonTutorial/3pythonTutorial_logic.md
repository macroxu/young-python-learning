### python基础教程--逻辑
>在代码中作出决定。计算机使用逻辑和选择来控制不同情况下发生的事情。

#### if, elif, else  

``` python
#根据分数的不同，打印不同的结果。
score = 69 
if score > 90:
    print('优秀')
elif score > 80:
    print('良好')
elif score > 60:
    print('及格')
else:
    print('不及格')
 
```
   
>Python 使用缩进来告诉计算机在每种情况下应该执行哪些指令，类似于它使用缩进来显示哪些行的语句属于一个循环的方式。

#### 比较运算符
如果数字等于、小于、大于或不等于某物，您可以通过比较数字以使不同的事情发生。
``` python
number = 5
if number <= 5:
    display.scroll('number数字小于等于5')
```

>请记住单个等号的作用是分配变量的值：
>number = 5  
>但当测试值时，“is equals to”（等于）运算符使用两个等号：
>if number == 5:

#### 逻辑运算符
您可以使用and (与)、or (或)和not (非)来构建更复杂的条件 。
``` python
age=8
if age > 5 and age < 10:
    print('年龄大于5岁，小于10岁')
```
 
#### 嵌套 if
您可以将 if 语句放在彼此内部。 这被称为“嵌套”。

``` python
score = 86
 
if score > 85:
    if score < 90:
        print('成绩优秀 B+')
```

#### 条件布尔值
布尔变量只能有两个值： True（真) 或 False (假)
您可以在 if 语句中使用布尔变量来编写易于阅读和理解的代码。

``` python
running = True
if running:
    print('程序正在运行')
else:
    print('程序没有运行')
```

#### 使用逻辑来中断
您可以跳出循环，具体方式是使用条件语句和break

``` python
# 当发现command 字符串为gameover时，跳出循环
command = 'gameover'
while True:
    if command == 'gameover':
        break
    else:
        print('程序正在运行')
```
