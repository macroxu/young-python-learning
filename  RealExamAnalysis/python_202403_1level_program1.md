
24年GESP 3月认证 Python一级真题解析(编程题1-小杨买书)  

### 3.1 编程题 1  
**试题名称**：小杨买书  
#### 3.1.1 题面描述    
小杨同学想用零花钱购买图书，已知图书单价为13元，请根据输入的零花钱数量，编写程序计算出最多可以购买多少本图书，以及还剩余多少零花钱。  

#### 3.1.2 输入格式  
只输入一个正整数，表示小杨零花钱的数量。【注意：零花钱的数量大于0但小于200，该条件不必体现在程序之
中】
#### 3.1.3 输出格式  
输出为两行。  
第1行，最多购买图书的数量，  
第2行为购买图书后剩余的零花钱数量。
#### 3.1.4 样例1
```
100
```
```
7
9
```
#### 3.1.5 样例1解释  
**100**为小杨可用于购买图书的金额，**7**为最多可以购买图书的数量，每本**13**元，最多可以购买**7**本，剩余**9**元不够购买一本，**9**为购买图书后的剩余零花钱数量。
 
#### 3.1.6 样例2
```
199
```
```
15
4
```

### 解题思路

#### 1 根据题目描述，分析题目要求

``题目主要内容``：小杨同学想用零花钱购买图书，已知图书单价为13元，请根据输入的零花钱数量，编写程序计算出最多可以购买多少本图书，以及还剩余多少零花钱。  
``输入->零花钱数量``:输入的零花钱数量  
``计算->最多购买图书的数量``:零花钱数量除以图书单价  
``计算->购买图书后剩余的零花钱数量``:零花钱数量取余图书单价  
``输出``: 最多购买图书的数量，购买图书后剩余的零花钱数量
``[计算小杨买书的算法]``:  

* 【小杨零花钱的数量】除以【图书单价】，得到最多购买图书的数量
* 【小杨零花钱的数量】取余【图书单价】，得到购买图书后剩余的零花钱数量
* 输出最多购买【图书的数量】，购买图书后剩余的【零花钱数量】
 

#### 2 伪代码过程
* 第一步：获取小杨零花钱的数量
* 第二步：计算最多购买图书的数量
* 第三步：计算购买图书后剩余的零花钱数量
* 第四步：输出最多购买图书的数量，购买图书后剩余的零花钱数量

 

#### 3 代码实现

```python 
# 获取小杨零花钱的数量
money = int(input())
# 计算最多购买图书的数量
bookNum = money // 13
# 计算购买图书后剩余的零花钱数量
leftMoney = money % 13
# 输出最多购买图书的数量，购买图书后剩余的零花钱数量
print(bookNum)
print(leftMoney)
```
