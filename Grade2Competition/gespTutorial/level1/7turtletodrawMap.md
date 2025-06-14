
GESP考级Python一级中的Turtle绘图教程是一个引导初学者使用Python的Turtle模块进行图形绘制的教学过程。  
Turtle模块是一个简单而强大的绘图库，非常适合初学者用来学习编程基础。

### 一、Turtle模块简介

**Turtle库介绍**：Turtle（海龟绘图）是Python中的一个标准库，用于绘制图形和进行简单的图形编程。通过想象屏幕上有一只小海龟，它会根据我们的指令在屏幕上行走，它走过的痕迹就是我们所绘制的图形。
**历史背景**：Turtle模块最初由Wally Feurzeig, Seymour Papert和Cynthia Solomon等在1967年使用Logo编程语言开发而成。后来，随着Python语言的兴起，Turtle模块被重写为Python内置的一个模块。

### 二、Turtle模块的基本操作

#### 1. 导入Turtle模块

在Python程序中，首先需要导入Turtle模块。这可以通过在程序的最开始部分添加`import turtle`语句来实现。

```python
import turtle
```

#### 2. 设置画布

可以使用`turtle.setup(width, height)`来设置画布的宽度和高度。如果不需要设置特定大小，可以省略这两个参数。

```python
turtle.setup(800, 600)
```

#### 3. 控制画笔

Turtle模块提供了多种控制画笔的方法，包括设置画笔颜色、线条宽度和移动速度等。

- 设置画笔颜色：`turtle.pencolor(color)`
- 设置线条宽度：`turtle.width(width)`
- 设置移动速度：`turtle.speed(speed)`，其中speed的取值范围是0（最快）到10（最慢），也可以设置为None表示不使用动画效果。

```python
turtle.pencolor('blue')
turtle.width(5)
turtle.speed(1)
```

#### 4. 控制Turtle移动

- 前进：`turtle.forward(distance)`或`turtle.fd(distance)`
- 后退：`turtle.backward(distance)`或`turtle.bk(distance)`
- 左转：`turtle.left(angle)`
- 右转：`turtle.right(angle)`
- 转向绝对角度：`turtle.setheading(angle)`

```python
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
```

#### 5. 抬起和放下画笔

- 抬起画笔：`turtle.up()`或`turtle.pu()`，这样移动Turtle时不会绘制线条。
- 放下画笔：`turtle.down()`或`turtle.pd()`，恢复绘制线条的功能。

```python
turtle.up()
turtle.forward(50)
turtle.down()
turtle.forward(50)
```

### 三、绘制基本图形

#### 1. 绘制正方形

```python

import turtle


turtle.color('blue') # 设置画笔颜色
turtle.pensize(4)    # 设置画笔宽度
turtle.speed(1)      # 设置绘制速度
for _ in range(4):   # 绘制正方形
    turtle.forward(100) # 向前移动100个像素
    turtle.right(90)  # 向右转90度
turtle.hideturtle()  # 隐藏turtle图标
turtle.done()  # 完成绘图，保持窗口开启
```

#### 2. 绘制圆形

```python
import turtle
turtle.color('blue') # 设置画笔颜色
turtle.pensize(4)    # 设置画笔宽度
turtle.speed(1)      # 设置绘制速度
turtle.circle(100)  # 绘制半径为100的圆
turtle.hideturtle()
turtle.done()
```

#### 3. 绘制三角形

```python
##画三角形
import turtle
turtle.color('blue') # 设置画笔颜色
turtle.pensize(4)    # 设置画笔宽度
turtle.speed(1)      # 设置绘制速度
for i in range(3):   # 绘制三角形
    turtle.forward(100) # 向前移动100个像素
    turtle.right(120)   # 向右转120度
```

#### 4. 绘制五角星

```python
import turtle
turtle.color('blue') # 设置画笔颜色
turtle.pensize(4)    # 设置画笔宽度
turtle.speed(1)      # 设置绘制速度
for i in range(5):   # 绘制五角星
    turtle.forward(100)  # 向前移动100个像素
    turtle.right(144)   # 向右转144度
```

### 四、高级操作(扩展知识可以了解一下)

- **填充颜色**：使用`turtle.begin_fill()`和`turtle.end_fill()`来填充图形。

``` python
import turtle
#填充一个三角形 蓝颜色
turtle.color('blue') # 设置画笔颜色
turtle.begin_fill()  # 开始填充
for i in range(3):   # 绘制三角形
    turtle.forward(100) # 向前移动100个像素
    turtle.right(120)   # 向右转120度
turtle.end_fill()    # 结束填充
```

- **绘制文字**：使用`turtle.write(text, font=("font-name", font-size, "font-type"))`来在画布上绘制文字。

```python
import turtle
turtle.color('blue') # 设置画笔颜色
# 写文字'helloworld'
turtle.write('helloworld', font=('Arial', 16, 'normal'))
```

通过以上教程，考生可以掌握Turtle模块的基本操作，并能够在GESP Python一级考试中运用这些技能来绘制简单的图形。
