GESP Python一级冲刺阶段！编程题常考知识点汇总，助你一战必过！
 

### 1 循环读取n个正整数
#### 1.1 举例 输入一个数`n`,接下来输入`n`个正整数，累加这些正整数的和并输出

**参考代码**   
```python
# 读取正整数个数n
n = int(input())
# 初始化总和变量
total_sum = 0
# 循环读取n个正整数并累加
for _ in range(n):
    # 读取正整数a
    a = int(input())
    # 计算a的数位和
    total_sum += a
# 输出总和
print(total_sum)
```


### 2 两个逻辑判断组合的逻辑运算
#### 2.1 逻辑与（logical AND）运算
举例：判断一个数是否被7，5同时整除
```python
num = int(input("请输入一个整数: "))
if num % 7 == 0 and num % 5 == 0:
    print(f"{num} 能被7和5同时整除")
else:
    print(f"{num} 不能被7和5同时整除")
```

#### 2.2 逻辑或（logical OR）运算   
举例：判断一个数是否被7或5整除
```python
num = int(input("请输入一个整数: "))
if num % 7 == 0 or num % 5 == 0:
    print(f"{num} 能被7或5整除")
else:
    print(f"{num} 不能被7或5整除")
```


### 3 整数除法和取模运算
举例：计算一个数除以3的商和余数
```python
num = int(input("请输入一个整数: "))
# 计算商
quotient = num // 3
# 计算余数
remainder = num % 3 
print(f"{num} 除以3的商是 {quotient}, 余数是 {remainder}")


```

### 4 取一个数的数位
举例：输入一个两位数，分别取出十位和个位数字
```python
num = int(input("请输入一个两位正整数: "))
tens = num // 10  # 取出十位数字
ones = num % 10   # 取出个位数字
print(f"十位数字是 {tens}, 个位数字是 {ones}")
```

### 5 累加数字和
举例：输入`n`个正整数，计算每个正整数之和，并输出
```python
n = int(input("请输入正整数的个数: "))
total_sum = 0
for _ in range(n):
    num = int(input("请输入一个正整数: "))
    total_sum += num
print(f"所有正整数的和是: {total_sum}")

```
### 6 显示一个浮点数，保留两位小数
```python
num = float(input("请输入一个浮点数: "))
# 保留两位小数输出
print(f"{num:.2f}")
```