2025年GESP 12月认证-->Python二级真题解析(编程题2-黄金格)

### 3.2 编程题2
- **试题名称**：黄金格
- **时间限制**：1.0 s
- **内存限制**：512.0 MB


#### 3.2.1 题目描述
小杨在探险时发现了一张神奇的矩形地图,地图有 ``H`` 行和 ``W`` 列｡每个格子的坐标是 ``(r, c)`` ,其中 ``r`` 表示行号从1到 ``H`` , ``c`` 表示列号从1到 ``W`` 。  
小杨听说地图中隐藏着一些“黄金格”,这些格子满足一个神秘的数学挑战:当格子坐标 ``(r, c)`` 代入特定的不等式关系成立时,该格子就是黄金格｡具体来说,黄金格的条件是:
$$\sqrt{r^2+c^2} ≤x+r-c$$  
例如,如果参数``x=5``，那么格子``(4,3)``就是黄金格｡因为左边坐标平方和的平方根``√(4²+3²)``算出来是``5``,而右边``5+4-3``算出来是``6``, ``5``小于等于``6``,符合条件｡

#### 3.2.2 输入格式
三行,每行一个正整数,分别表示 ``H`` , ``W`` , ``x`` 。含义如题面所示｡

#### 3.2.3 输出格式
一行一个整数,代表黄金格数量｡

#### 3.2.4 样例
##### 3.2.4.1 样例输入
```
4
4
2
```
##### 3.2.4.2 样例输出
```
4
```
##### 3.2.4.3 样例解释

<table border="1" cellpadding="8" cellspacing="0">
  <tr>
    <td style="background-color: #fdd835;">(1,1)</td>
    <td style="background-color: #90caf9;">(1,2)</td>
    <td style="background-color: #90caf9;">(1,3)</td>
    <td style="background-color: #90caf9;">(1,4)</td>
  </tr>
  <tr>
    <td style="background-color: #fdd835;">(2,1)</td>
    <td style="background-color: #90caf9;">(2,2)</td>
    <td style="background-color: #90caf9;">(2,3)</td>
    <td style="background-color: #90caf9;">(2,4)</td>
  </tr>
  <tr>
    <td style="background-color: #fdd835;">(3,1)</td>
    <td style="background-color: #90caf9;">(3,2)</td>
    <td style="background-color: #90caf9;">(3,3)</td>
    <td style="background-color: #90caf9;">(3,4)</td>
  </tr>
  <tr>
    <td style="background-color: #fdd835;">(4,1)</td>
    <td style="background-color: #90caf9;">(4,2)</td>
    <td style="background-color: #90caf9;">(4,3)</td>
    <td style="background-color: #90caf9;">(4,4)</td>
  </tr>
</table>

图中标注为黄色的四个格子是黄金格，坐标分别为 (1,1)，(2,1)，(3,1)，(4,1)。



### 解题思路
#### 1. 题目理解
1. 输入三个正整数H、W、x，分别表示地图的行数、列数和不等式中的参数。
2. 遍历地图中的每个格子坐标(r, c)，判断是否满足不等式关系$\sqrt{r^2+c^2} ≤ x + r - c$，如果满足则计数器加1。
3. 最后输出满足条件的格子数量。


#### 2. 程序功能点识别
##### 功能点1： (输入参数和初始化)
- 读取输入参数H、W、x。
  
##### 功能点2： (遍历格子坐标并判断条件)
- 使用两层嵌套的for循环，外层循环遍历行号r从1到H，内层循环遍历列号c从1到W。
- 对于每个格子坐标(r, c)，计算不等式左右两边的值：
  - 左边：$\sqrt{r^2+c^2}$，可以使用`(r**2 + c**2)**0.5`计算。
  - 右边：`x + r - c`。
- 判断左边是否小于等于右边，如果满足条件，则计数器加1。

 

##### 参考代码1
```python
# 读取输入参数
H = int(input())
W = int(input())
x = int(input())

count = 0  # 黄金格计数器
# 遍历每一个格子
for r in range(1, H + 1):
    for c in range(1, W + 1):
        # 计算不等式左右两边
        left = (r ** 2 + c ** 2) ** 0.5
        right = x + r - c
        # 判断是否符合黄金格条件
        if left <= right:
            count += 1
# 输出结果
print(count)
```

##### 考点说明
本题考查 ``Python嵌套for循环``、``数学运算``、``条件判断``，核心是理解题目中的数学公式，正确实现遍历与条件校验，同时考察对浮点数精度问题的处理能力。