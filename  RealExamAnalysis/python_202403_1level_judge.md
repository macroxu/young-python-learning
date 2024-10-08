24年GESP 3月认证 Python一级真题解析(二判断题部分)  
**第 1 题** 第 1 题 小杨今年春节回奶奶家了，奶奶家的数字电视可以通过遥控器输入电视剧名称来找到想播放的电视剧，所以
可以推知里面有交互式程序在运行。（ ）  
答案：**对**  
**解析**：  
数字电视根据遥控器输入的电视剧名称来找到想播放的电视剧，说明里面有交互式程序在运行。所以答案是对的。

**第 2 题** 任何一个 for 循环都可以转化为等价的 while 循环。（ ）  
答案：**对**
**解析**：  
任何一个``for``循环都可以转化为等价的``while``循环。``for``循环是一种计数循环，``while``循环是一种条件循环，两者可以相互转化。

**第 3 题**
在Python代码中变量 n 被赋值为27，则 print(n // 10) 执行后输出的是 7 。( )  
答案：**错**  
**解析**：
在Python代码中变量 n 被赋值为27，则 print(n // 10) 执行后输出的是 2 。  
``n // 10`` 是整除运算，结果是2。

**第 4 题**  
Python语句 print(2,3,sep="#",end="&") 执行后输出的是 2#3& 。 ( )  
答案：**对**  
**解析**：  
Python语句``print(2,3,sep="#",end="&")``执行后输出的是``2#3&``。  
``sep="#"``表示输出的分隔符是``#``，``end="&"``表示输出的结尾是``&``。

**第 5 题**
在Python中， while 可能是死循环，而 for-in 循环不可能是死循环。（ ）
答案：**对**  
**解析**：  
在Python中，``while``循环可能是死循环，而``for-in``循环不可能是死循环。
``while``循环是一种条件循环，当条件满足时，循环继续执行；  
``for-in``循环是一种计数循环，循环次数是固定的。

**第 6 题** Python表达式 "10"*2 执行时将报错，因为 "10" 是字符串类型而 2 是整数类型，它们数据类型不同，不能
在一起运算。（ ）  
答案：**错**  
**解析**：  
Python表达式``"10"*2``执行时不会报错，输出的是``"1010"``。  
``"10"``是字符串类型，``2``是整数类型，它们数据类型不同，但是可以在一起运算，``"10"*2``表示将字符串``"10"``重复2次。  

**第 7 题** 在Python， break 语句用于提前终止当前层次循环，适用于 while 循环，但不适用于 for-in 循环。（ ）
答案：**错**  
**解析**：  
在Python，``break``语句用于提前终止当前层次循环，适用于``while``循环，也适用于``for-in``循环。

**第 8 题** 以下Python代码默认将绘制一条水平直线。（ ）

```python
import turtle
turtle.goto(50,0)
```

答案：**对**  
**解析**：
turtle 默认的起始位置是画布的中心，即坐标原点(0,0)。  
``turtle.goto(50,0)``表示将画笔移动到坐标(50,0)，默认将绘制一条水平直线。  

**第 9 题**  Python代码执行后，将绘制一个边长为100的等边三角形，且填充颜色为红色。（ ）

```python
import turtle
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(100, steps=3)
turtle.end_fill()
```

答案：**错**  
**解析**：  
上面代码执行后 生成一个等边三角形，填充颜色为红色。 但不是边长为100的等边三角形，而是半径是100的外接圆的等边三角形。

**第 10 题** Python代码 turtle.right() 也可以实现海龟指向左旋转。（ ）

答案：**对**  
**解析**：
如果当前的turtle传递的参数是180，那么turtle.right()和turtle.left()是等价的，都是让海龟向左旋转180度。
