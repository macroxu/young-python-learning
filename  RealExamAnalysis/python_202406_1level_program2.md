
24年GESP 6月认证 Python一级真题解析(编程题2-立方数)  

### 3.2 编程题 2

**试题名称**：立方数  
**时间限制**：1.0 s  
**内存限制**：512.0 MB  

#### 3.2.1 题面描述

小杨有一个正整数 ，他想知道 是否是一个立方数。
一个正整数 是立方数当且仅当存在一个正整数``x``满足``x*x*x=n`` 。

#### 3.2.2 输入格式

第一行包含一个正整数 ``n``。

#### 3.2.3 输出格式

如果正整数``n``是一个立方数，输出 ``Yes``，否则输出 ``No``。

#### 3.2.4 样例1

``` python
8
Yes
```

#### 3.2.5 样例2

``` python
9
No
```

#### 3.2.6 样例解释

对于样例1，存在正整数2使得``2*2*2=8``，因此``8``为立方数。  
对于样例2，不存在满足条件的正整数，因此``9``不为立方数。

#### 3.2.7 数据范围

对于全部数据，保证有 $1 \leq s \leq 1000$ 。

### 解题思路

#### 1 根据题目描述，分析题目要求

>``题目主要内容``：小杨有一个正整数 ，他想知道 是否是一个立方数。  
``输入->正整数``:输入一个正整数n  
``计算->是否是立方数``:判断是否存在一个正整数 满足 $n = m*m*m$  
``输出：是否是立方数``:输出Yes或No  
``[判断是否是立方数的算法]``:* 从1开始遍历到n，判断是否存在一个正整数m满足$n = m*m*m$，如果存在则输出Yes，否则输出No。

#### 2 伪代码过程

* 第一步：输入一个正整数n
* 第二步：从1开始遍历到n，判断是否存在一个正整数m满足$n = m*m*m$
* 第三步：如果存在则输出Yes，否则输出No。

#### 3 代码实现

```python
n = int(input()) # 输入一个正整数n
是否是立方数 = False   # 定义一个变量是否是立方数=False
for i in range(1,n+1): # 从1开始遍历到n
    if i*i*i == n:   # 判断是否存在一个正整数m满足m*m*m=n
        是否是立方数 = True # 如果存在则输出Yes
        break  # 跳出循环
if 是否是立方数: # 如果存在则输出Yes
    print("Yes") # 输出Yes
else:          # 否则输出No
    print("No") # 输出No
```

>补充说明：上述的代码还可以优化，加入遍历的数``m``,当``m*m*m>n``时，可以直接跳出循环，因为``m*m*m``是递增的，当``m*m*m>n``时，就不可能存在满足条件的``m``了。
但这个优化可以作为扩展知识点，不是必须的。

优化后的代码如下：

```python
n = int(input()) # 输入一个正整数n
是否是立方数 = False   # 定义一个变量是否是立方数=False
for i in range(1,n+1): # 从1开始遍历到n
    if i*i*i == n:   # 判断是否存在一个正整数m满足m*m*m=n
        是否是立方数 = True # 如果存在则输出Yes
        break  # 跳出循环
    if i*i*i > n:  # 如果m*m*m>n
        break  # 跳出循环
if 是否是立方数: # 如果存在则输出Yes
    print("Yes") # 输出Yes
else:          # 否则输出No
    print("No") # 输出No
```
