
24年GESP 9月认证 Python一级真题解析(编程题1-小杨购物)  

### 3.1 编程题 1

试题名称：小杨购物  
时间限制：1.0 s  
内存限制：512.0 MB  

#### 3.1.1 题面描述  

小杨有``n``元钱用于购物。商品``A``的单价是``a``元，商品``B`` 的单价是``b``元。小杨想购买``相同数量``的商品``A``和商品``B``。  
请你编写程序帮小杨计算出他最多能够购买多少个商品``A``和商品``B``。  

#### 3.1.2 输入格式  

第一行包含一个正整数``n`` ，代表小杨用于购物的钱的金额。  
第二行包含一个正整数``a`` ，代表商品``A``的单价。
第三行包含一个正整数``b`` ，代表商品``B``的单价。

#### 3.1.3 输出格式

输出一行，包含一个整数，代表小杨最多能够购买的商品``A``和商品``B``的数量。

#### 3.1.4 样例

```
12
1
2
```

```
4
```

在样例1中，  
第1行输入的12表示小杨拥有的资金总额为12元，  
第2行的1表示第一种商品（即商品A）的单价，  
第3行的2表示第二种商品（即商品B）的单价。  

对于样例1，由于需要购买相同数量的两种商品，因此小杨最多能够购买``A``件商品 和``B``件商品 ，共花费$1*4+2*4=12$元。因此，样例1的答案为 4。  

对于本题，输入皆为大于0的正整数，不必考虑其他情况。

#### 3.1.5 样例2

```
13
1
2
```

```
4
```

对于样例2，由于需要购买相同数量的两种商品，因此小杨最多能够购买 ``4`` 件商品``A`` 和``B`` 件商品 ，共花费
$1*4+2*4=12$元。如果小杨想购买5件商品``A`` 和``5``件商品``B`` ，则需花费 $1*5+2*5=15$元，超过了小杨的预算``13``元。因此，样例2的答案为``4``。

对于全部数据，保证有$1 \leq n$, $a \leq 10^5 \text{ 且 } b \leq 10^5$,【此处为严谨题目所需，本级考生不必考虑本行描述】。

### 解题思路

#### 1 根据题目描述，分析题目要求

``题目主要内容``：小杨有``n``元钱用于购物。商品``A``的单价是``a``元，商品``B`` 的单价是``b``元。小杨想购买``相同数量``的商品``A``和商品``B``。  
**> **题目的关键词 购买同等数量的商品A和商品B，说明最后购买的商品A和商品B的数量是相同的。**  
``输入->小杨购物金额``:输入的时刻,包含一个参数，代表小杨用于购物的钱的金额``n``  
``输入->商品A单价``:输入的时刻,包含一个参数，代表商品``A``的单价``a``  
``输入->商品B单价``:输入的时刻,包含一个参数，代表商品``B``的单价``b``  
``计算->小杨购买商品A和商品B的数量``:小杨购买商品A和商品B的数量  
``输出：小杨购买商品A和商品B的数量``:输出的时刻,包含一个参数，代表小杨最多能够购买的商品``A``和商品``B``的数量  

``[计算小杨购买商品A和商品B的数量的算法]``:  

* 计算小杨购买商品A和商品B的单价总和
* 计算小杨购物金额n除以商品A和商品B的单价总和，并取整数部分

#### 2 伪代码过程

第一步：获取小杨购物金额n  
第二步：获取商品A单价a  
第三步：获取商品B单价b  
第四步：计算小杨购买商品A和商品B的数量  
第五步：输出小杨购买商品A和商品B的数量  

#### 3 代码实现

```python
# 小杨购物的总金额
n = int(input())  
# 商品A的单价
a = int(input())
# 商品B的单价
b = int(input())
# 小杨购买商品A和商品B的单价总和
abPrice = int(a)+int(b)
# 小杨购买商品A和商品B的数量
goodsNum = n//abPrice
# 输出小杨购买商品A和商品B的数量
print(goodsNum)
```