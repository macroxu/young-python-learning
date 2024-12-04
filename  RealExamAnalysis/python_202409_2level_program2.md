24 年 GESP 9 月认证 Python 二级真题解析(编程题 2-小杨的N字矩阵)

### 3.2 编程题 2

试题名称：小杨的N字矩阵  
时间限制：1.0 s  
内存限制：512.0 MB

#### 3.2.1 题面描述

小杨想要构造一个$m \times m$ 的 N 字矩阵（m为奇数），这个矩阵的从左上角到右下角的对角线、第``1``列和第``m``列都是半角加号 + ，其余都是半角减号 - 。例如，一个$5 \times 5$ 的 N 字矩阵如下：

```
+---+
++--+
+-+-+
+--++
+---+
```

请你帮小杨根据给定的m打印出对应的 N 字矩阵。

#### 3.2.2 输入格式  

第一行包含一个正整数``m`` 。

#### 3.2.3 输出格式

输出对应的 N 字矩阵。

#### 3.2.4 样例1

```
5
```

```
+---+
++--+
+-+-+
+--++
+---+
```

对于全部数据，保证有$3 \leq m \leq 49$且 ``m`` 为奇数。

### 解题思路

#### 1 根据题目描述，分析题目要求

`题目主要内容`：
构造一个$m \times m$ 的 N 字矩阵（m为奇数），这个矩阵的从左上角到右下角的对角线、第``1``列和第``m``列都是半角加号 + ，其余都是半角减号 - 。

`输入->矩阵的行数`：输入一个3到49之间的奇数`m`，代表矩阵的行数。

`输出->构造的N字矩阵`：输出对应的 N 字矩阵。

`[构造N字矩阵]`：
假设当前的矩阵为$5 \times 5$的矩阵，分析构造的N字矩阵如下：  

* 第一行：`+---+`。两边都是`+`，中间都是`-`。  
* 第二行：`++--+`。两边都是`+`，中间第一个字符为`+`，第二个字符为`-`，第三个字符为`-`。  
* 第三行：`+-+-+`。两边都是`+`，中间第一个字符为`-`，第二个字符为`+`，第三个字符为`-`。  
* 第四行：`+--++`。两边都是`+`，中间第一个字符为`-`，第二个字符为`-`，第三个字符为`+`。  
* 第五行：`+---+`。两边都是`+`，中间都是`-`。  

我们发现规律如下：  

* 每一行有`m`个字符。
* 每一行第一个字符和最后一个字符都是`+`开头和结尾。  
* 第`n`行的第`n`个字符是`+`，比如第`2`行的第`2`个字符是`+`，第`3`行的第`3`个字符是`+`。  

#### 2 伪代码过程

* 输入矩阵的行数`m`。
* 开始循环(执行`m`次)
  * 开始循环(执行`m`次)
    * 判断当前字符是第一个或者最后一个字符。则打印`+`。
    * 判断当前字符是第`n`个字符。则打印`+`。
    * 其余情况打印`-`。
  * 打印换行。

#### 3 代码实现

```python
# 输入矩阵的行数
m = int(input())

# 开始循环(执行m次)
for i in range(m):
    # 开始循环(执行m次)
    for j in range(m):
        # 判断当前字符是第一个或者最后一个字符。则打印+
        if j == 0 or j == m - 1:
            print('+', end='')
        # 判断当前字符是第n个字符。则打印+
        elif j == i:
            print('+', end='')
        # 其余情况打印-
        else:
            print('-', end='')
    # 打印换行
    print()


```