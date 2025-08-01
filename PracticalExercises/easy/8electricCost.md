


### 一、电费阶梯计费（多条件分段计算）

#### 1 题目描述

某地电费收费标准：  

- 月用电量≤100 度：0.5 元 / 度  
- 100 度 < 用电量≤300 度：超出 100 度部分 0.6 元 / 度  
- 用电量 > 300 度：超出 300 度部分 0.8 元 / 度  

输入月用电量，输出电费。

#### 2 示例输出

**例子 1**

```
月用电量（度）：50
应缴电费：25.00元
```

**例子 2**

```
月用电量（度）：140
应缴电费：74.00元
```

#### 3 解题逻辑

1. **输入月用电量**：使用 `input()` 函数获取用户输入的月用电量，并转换为整数。
2. **计算电费**：使用多条件分段计算，根据用电量的不同区间计算电费。
3. **输出结果**：使用 `print()` 函数格式化输出应缴电费。

#### 4 代码实现

```python
electricity_usage = int(input("月用电量（度）："))
if electricity_usage <= 100:
    # 月用电量≤100 度，按 0.5 元 / 度计费
    cost = electricity_usage * 0.5
elif electricity_usage <= 300:
    # 超出 100 度部分按 0.6 元 / 度计费，其他部分按 0.5 元 / 度计费
    cost = 100 * 0.5 + (electricity_usage - 100) * 0.6
else:
    # 超出 300 度部分按 0.8 元 / 度计费,其他部分按 0.5 元 / 度和 0.6 元 / 度计费
    cost = 100 * 0.5 + 200 * 0.6 + (electricity_usage - 300) * 0.8
print(f"应缴电费：{cost:.2f}元")

```
