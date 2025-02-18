查找完美数(perfact number)--python解决数学问题

### Python完全数编程

### 一、完全数的定义

完全数（Perfect Number）是指一个数恰好等于其所有真因子（即除了自身以外的约数）之和。例如，6是一个完全数，因为它的真因子1、2、3之和等于6。

### 二、Python编程实现

#### 1. 基本思路

* 遍历指定范围内的所有整数。
  * 对于每个整数，计算其所有真因子的和。
  * 如果真因子的和等于该整数，则它是一个完全数。

**判断一个数是否是完全的编程逻辑如下**：

* 初始化因子和为0
* 遍历从1到num-1的所有数，检查是否为num的因子
  * 如果是因子，则将**因子**加到**因子和**中
  * 如果不是因子，则继续遍历下一个数
* 完成遍历后 判断因子和是否等于num 是则是完全数，否则不是完全数

#### 2. 代码实现

以下是一个Python程序，用于找出10000以内的所有完全数：

```python
# 定义一个函数来检查一个数是否是完全数
def is_perfect_number(num):
    # 初始化因子和为0
    factor_sum = 0
    # 遍历从1到num-1的所有数，检查是否为num的因子
    for i in range(1, num):
        if num % i == 0:
            factor_sum += i
    # 如果因子和等于num，则返回True，否则返回False
    return factor_sum == num

# 初始化一个空列表来存储完全数
perfect_numbers = []

# 遍历从1到10000的所有数，检查每个数是否是完全数
for num in range(1, 10001):
    if is_perfect_number(num):
        perfect_numbers.append(num)

# 打印出所有找到的完全数
print("10000以内的完全数为:", perfect_numbers)
```

### 三、代码解释

1. **is_perfect_number函数**：这个函数接受一个整数作为输入，并返回一个布尔值，表示该整数是否是完全数。它通过一个循环来计算输入整数的所有真因子的和，并将该和与输入整数进行比较。

3. **perfect_numbers列表**：这个列表用于存储所有找到的完全数。

4. **主循环**：这个循环遍历从1到10000的所有整数，并使用is_perfect_number函数来检查每个数是否是完全数。如果是，则将该数添加到perfect_numbers列表中。

5. **打印结果**：最后，程序打印出10000以内的所有完全数。

### 四、优化方案

虽然上述程序可以正确地找出完全数，但在处理大数时可能会变得较慢。这是因为对于每个数，我们都需要遍历其所有小于它的数来检查是否为因子。

优化方案如下：

* 循环从1到num的平方根的所有数，检查是否为num的因子，
  * 如果是因子，则将这个**因数**和**num//因数**加到因子和中
  * 如果不是因子，则继续遍历下一个数
* 最后判断因子和是否等于num，是则是完全数，否则不是完全数

```python
import math

# 定义一个函数来检查一个数是否是完全数
def is_perfect_number(num):
    # 初始化因子和为0
    factor_sum = 1
    # 遍历从2到num的平方根的所有数，检查是否为num的因子
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factor_sum += i
            if i != num // i:
                factor_sum += num // i
    # 如果因子和等于num，则返回True，否则返回False
    return factor_sum == num

# 初始化一个空列表来存储完全数
perfect_numbers = []

# 遍历从1到10000的所有数，检查每个数是否是完全数
for num in range(1, 10001):
    if is_perfect_number(num):
        perfect_numbers.append(num)

# 打印出所有找到的完全数
print("10000以内的完全数为:", perfect_numbers)
```
