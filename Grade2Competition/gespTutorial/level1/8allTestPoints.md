
Python一级中的高频必考知识点--(GESP考级)
1 input()函数
2 算数运算
3 字符串格式化输出
4 range()函数
5 turtle 库 转向和移动
6 turtle 库 画圆
7 集合range()函数和for循环

### 1 input()函数

input()函数用于接收用户输入的内容，返回值是一个字符串类型。

* 两个请求形式：1 **有提示信息** 2 **无提示信息**
* 如果需要获取**输入的数字**，需要使用**int()函数**进行类型转换。

```python
# 无提示信息
name = input() 
name = input('请输入您的姓名：') # 有提示信息

age = int(input('请输入您的年龄：')) # 有提示信息,且

```

### 2 算术运算

算术计算中常考的是**余数**和**整数运算**

```python
# 除法运算
a = 10
b = 3
d = a // b  # 取整数
e = a % b  # 取余数
```

### 3 字符串格式化输出

**字符串格式化**输出是Python中常用的输出方式，**f-string**。
**f-string规则**是Python3.6版本新增的一种字符串格式化方式，使用f开头，**{}**中放入变量名或表达式。

```python
name = '小明'
age = 18
# f-string格式化输出 关键点是f开头 {}中放入变量名或表达式
print(f'姓名：{name}，年龄：{age}')
```

### 4 range()函数

range()函数用于生成一个整数序列，常用于**for循环**中。

range()函数的参数格式如下：
**range(start, stop[, step])**
**1 start**：序列的起始值，默认为0。
**2 stop**：序列的结束值，**不包含在序列中**。 一定要注意**stop的数**不在序列中。
**3 step**：序列的步长，这个参数可以添加也可以不添加。不添加默认为1。

```python

cheap
for i in range(1, 10, 2):
    print(i)
# 输出结果为：1 3 5 7 9

#默认从0开始，步长为1 到10结束
for i in range(10):
    print(i)
# 输出结果为：0 1 2 3 4 5 6 7 8 9

for i in range(10, 0, -1):
    print(i)
# 输出结果为：10 9 8 7 6 5 4 3 2 1
```

### 5 turtle 库 转向和移动

turtle常规的画**长方形**，**正方形**等

```python
import turtle

# 画长方形
#向前走100个单位
turtle.forward(100)
#向右转90度(顺时针90度)
turtle.right(90)
#向前走50个单位
turtle.forward(50)
#向右转90度
turtle.right(90)
#向前走100个单位
turtle.forward(100)
#向右转90度
turtle.right(90)
#向前走50个单位
turtle.forward(50)
#向右转90度
turtle.right(90)
#画完长方形
 

# 向前走200个单位，为下面的正方形做准备
turtle.forward(200)

# 画正方形
for i in range(4):
    #向前走100个单位
    turtle.forward(100)
    #向右转90度
    turtle.right(90)
```

### 6 turtle 库 画圆

turtle库中的**circle()**函数用于画圆，参数为**半径**和**角度**。
turtle画的圆是当前乌龟的方向的**逆时针方向**画圆。

```python
import turtle

#先向前走100个单位，确认方向 设置颜色red
turtle.color('red')
turtle.forward(100)


# 画一个半径为100的圆 设置颜色blue
turtle.color('blue')
turtle.circle(100)


```

### 7 集合range()函数和for循环

for循环中常用的是**range()**函数，range()函数用于生成一个**整数序列**。

```python
# 1到9的的数列循环
for i in range(1, 10):
    print(i)
# 输出结果为：1 2 3 4 5 6 7 8 9
```
