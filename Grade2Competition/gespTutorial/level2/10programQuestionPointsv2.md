 
  GESP Python二级冲刺：编程题常考知识点汇总


本文汇总了GESP Python二级冲刺阶段编程题的核心常考知识点，包含输入处理、数字操作、数学计算、时间转换、图形输出等高频考点，并提供可直接运行的参考代码，助力考生高效备考、一战通关。

## 1 一行输入两个整数

### 考点说明

接收一行输入的两个整数（空格分隔），并完成数据提取与输出，是Python输入处理的基础考点。

### 输入示例

```Plain Text

10 20
```

### 参考代码（官方推荐）

```Python

# 读取一行输入，拆分字符串并转换为整数
n, m = map(int, input().split())
 
# 输出结果
print(n)
print(m)
```

### 等效参考代码（仅提取字符串）

```Python

# 读取一行输入，仅拆分为字符串（未转换类型）
n, m = input().split()

# 输出结果
print(n)
print(m)
```

## 2 输入整数，按个位到最高位输出每一位数字

### 考点说明

通过取模、整数除法操作提取整数的每一位数字，逆序输出，考查循环与数字运算的基础应用。

### 输入示例

```Plain Text

12345
```

### 输出示例

```Plain Text

5
4
3
2
1
```

### 参考代码

```Python

# 读取输入的整数并转换为int类型
num = int(input())
# 循环逐一获取每一位数字
while num > 0:
    digit = num % 10  # 获取当前数的个位数字
    print(digit)      # 输出个位数字
    num = num // 10   # 去掉已输出的个位数字
```

## 3 计算一个数的平方根

### 考点说明

考查Python数学计算的两种常用方式：`math`模块调用与幂运算符使用。

### 输入示例

```Plain Text

4
```

### 输出示例

```Plain Text

2.0
```

### 参考代码1（使用math模块）

```Python

import math

# 读取输入的数并转换为int类型
num = int(input())    

# 计算平方根
sqrt_num = math.sqrt(num)

# 输出结果
print(sqrt_num)
```

### 参考代码2（使用幂运算符）

```Python

num = int(input())

# 计算平方根（幂运算符**，0.5次方等价于平方根）
sqrt_num = num ** 0.5

# 输出结果
print(sqrt_num)
```

## 4 时分秒转换为总秒数，累加秒数后输出新时分秒

### 考点说明

考查时间单位换算、整数运算及逆换算，是实际应用类编程题的高频考点。

### 输入示例

```Plain Text

12 30 45 
30
```

### 输出示例

```Plain Text

12 31 15
```

### 参考代码

```Python

# 读取输入的时分秒字符串，拆分为三个整数
h, m, s = map(int, input().split())
# 读取需要累加的整数秒数
n = int(input())

# 将时分秒转换为总秒数
total_seconds = h * 3600 + m * 60 + s

# 累加指定秒数
total_seconds += n

# 逆换算为新的时分秒
h_new = total_seconds // 3600
m_new = (total_seconds % 3600) // 60    
s_new = total_seconds % 60

# 输出新的时分秒
print(h_new, m_new, s_new)
```

## 5 输出n行n列的矩形图案

### 5.1 基础考点：n行n列矩形星号图案

#### 输入示例

```Plain Text

5
```

#### 输出示例

```Plain Text

*****
*****
*****
*****
*****
```

#### 参考代码

```Python

# 读取输入的整数n
n = int(input())
# 输出n行n列的矩形星号图案
for _ in range(n):
    for _ in range(n):
        print("*", end="")
    print()  # 换行，切换到下一行
```

### 5.2 进阶考点：n行n列菱形图案（n为奇数）

#### 输入示例

```Plain Text

5
```

#### 输出示例

```Plain Text

  *  
 * * 
*   *
 * * 
  *  
```

#### 参考代码

```Python

# 读取输入的整数n（需为奇数）
n = int(input())

# 输出n行n列的菱形图案
for i in range(n):
    for j in range(n):
        # 核心逻辑：通过绝对值判断是否输出星号
        if abs(i - n // 2) + abs(j - n // 2) == n // 2:
            print("*", end="")  
        else:
            print(" ", end="")
    print()  # 换行
```

## 6 输出n行三角形数字（1到9循环）

### 考点说明

考查双层循环、数字循环计数的综合应用，是图形输出类编程题的典型考点。

### 输入示例

```Plain Text

9
```

### 输出示例

```Plain Text

1
2 3
4 5 6
7 8 9 1
2 3 4 5 6
7 8 9 1 2 3
4 5 6 7 8 9 1
2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
```

### 参考代码

```Python

# 读取输入的整数n
n = int(input())
num = 1  # 初始化起始数字
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1  # 数字自增
        if num > 9:  # 数字超过9则重置为1，实现1-9循环
            num = 1
    print()  # 换行，切换到下一行
```

 
