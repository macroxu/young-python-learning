07 身体BMI指数判断(嵌套条件)---python 实战初级

### 一、身体BMI指数判断(嵌套条件)

#### 1 题目描述

BMI 计算公式：**体重 (kg)**/ **身高 (m)²**，判断标准：

- BMI < 18.5：偏瘦
- 18.5 ≤ BMI < 24：正常
- 24 ≤ BMI < 28：超重
- BMI ≥ 28：肥胖

输入身高和体重，输出 BMI 值及健康状态。

#### 2 示例输出

**例子 1**

```
身高（米）：1.41
体重（公斤）：40
BMI值：20.12
健康状态：正常
```

**例子 2**

```
身高（米）：1.41
体重（公斤）：50
BMI值：25.15
健康状态：超重
```

#### 3 解题逻辑

1. **输入身高和体重**：使用 `input()` 函数获取用户输入的身高和体重，并转换为浮点数。
2. **计算 BMI**：使用公式 `BMI = weight / (height *height)` 计算 BMI 值。
3. **判断健康状态**：使用嵌套条件 `if-elif-else` 结构判断 BMI 值所在的区间，并输出对应的健康状态。
4. **输出结果**：使用 `print()` 函数格式化输出 BMI 值和健康状态。

#### 4 代码实现

```python
height = float(input("身高（米）："))
weight = float(input("体重（公斤）："))
bmi = weight / (height * height)    
print(f"BMI值：{bmi:.2f}")
if bmi < 18.5:
    status = "偏瘦"
elif bmi < 24:
    status = "正常"
elif bmi < 28:
    status = "超重"
else:
    status = "肥胖"
print(f"健康状态：{status}")

```
