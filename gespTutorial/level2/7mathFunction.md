### Python简单数学函数---GESP教程Python二级

在 Python 中，有许多``内置函数``和``标准库函数``可以用于执行各种``数学运算``。以下是关于一些简单``数学函数``的教程，包括``绝对值函数``、``平方根函数``、``最大值函数``、``最小值函数``和``随机数函数``。

#### 1. 绝对值函数

绝对值函数用于返回一个数的正值，不考虑其原始符号。

**内置函数**：`abs()`

**用法**：

```python
x = -12
result = abs(x)#abs()函数返回x的绝对值 
print(result)  # 输出: 12
```

#### 2. 平方根函数

什么是平方根？  
平方根是一个数的平方根。例如，16的平方根是4，因为4的平方是16。  

平方根函数用于计算一个数的平方根。

**标准库函数**：`math.sqrt()`

**用法**：

```python
import math

x = 16
result = math.sqrt(x)
print(result)  # 输出: 4.0
```

**注意**：`math.sqrt()` 只能计算非负数的平方根，如果传入负数会引发 `ValueError`。

#### 3. 最大值函数

最大值函数用于返回一组数中的最大值。

**内置函数**：`max()`

**用法**：

```python
numbers = [1, 3, 5, 7, 2, 8]
result = max(numbers)
print(result)  # 输出: 8
```

**注意**：`max()` 函数可以接受任意数量的参数，包括可迭代对象（如列表、元组等）。

#### 4. 最小值函数

最小值函数用于返回一组数中的最小值。

**内置函数**：`min()`

**用法**：

```python
numbers = [1, 3, 5, 7, 2, 8]
result = min(numbers)
print(result)  # 输出: 1
```

**注意**：`min()` 函数同样可以接受任意数量的参数，包括可迭代对象。

#### 5. 随机数函数

随机数函数用于生成指定范围内的随机整数或浮点数。

**标准库模块**：`random`

**常用函数**：

- `random.randint(a, b)`：生成一个范围在 `[a, b]` 内的随机整数（包括 `a` 和 `b`）。
- `random.uniform(a, b)`：生成一个范围在 `[a, b]` 内的随机浮点数（包括 `a`，但不包括 `b` 的上限，但非常接近）。

**用法**：

```python
import random

# 生成随机整数
result_int = random.randint(1, 10)
print(result_int)  # 输出: 例如 7

# 生成随机浮点数
result_float = random.uniform(1.0, 10.0)
print(result_float)  # 输出: 例如 5.23456789
```
