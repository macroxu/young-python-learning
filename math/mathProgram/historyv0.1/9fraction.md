Python里实现数学分数运算，这篇教程和指南就够了

在Python中，你可以使用内置的`fractions`模块来处理分数。这个模块提供了一种精确表示分数的方式，避免了浮点数计算可能出现的问题，如舍入误差。

### 一、导入`fractions`模块

首先，你需要导入`fractions`模块中的`Fraction`类。这可以通过以下代码实现：

```python
from fractions import Fraction
```

### 二、创建分数对象

`Fraction`类可以接受多种形式的输入来创建分数对象，包括整数、浮点数、字符串等。

#### 1. **使用整数创建分数**：

```python
from fractions import Fraction

frac1 = Fraction(1, 3)  # 创建分数1/3
frac2 = Fraction(3, 4)  # 创建分数3/4
```

如果只输入一个参数，则默认分母为1：

```python
from fractions import Fraction

frac1 = Fraction(3)  # 创建分数3/1，即整数3
```

#### 2. **使用字符串创建分数**：

```python
from fractions import Fraction

frac1 = Fraction('2/5')  # 创建分数2/5
frac2 = Fraction('0.75')  # 创建分数3/4，因为0.75等于3/4

```

注意，当使用字符串形式的浮点数创建分数时，`Fraction`类会尝试将其转换为最简分数形式。

#### 3. **使用浮点数创建分数**：

虽然可以使用浮点数创建分数，但由于浮点数的精度问题，结果可能不是最简分数形式，且可能引入微小的误差。因此，通常建议使用整数或字符串形式来创建分数。

```python
from fractions import Fraction

frac6 = Fraction(0.5)  # 创建分数1/2，尽管输入是浮点数0.5
print(frac6)  # 输出结果：1/2
```

### 三、分数运算

`Fraction`类支持基本的数学运算，包括加、减、乘、除等。运算结果仍然是一个`Fraction`对象。

```python
# 导入Fraction类
from fractions import Fraction

# 创建两个分数对象
frac1 = Fraction(1, 3) # 1/3
frac2 = Fraction(3, 4) # 3/4

# 加法
result_add = frac1 + frac2  # 1/3 + 3/4 = 13/12
print(result_add)  # 输出结果：13/12

# 减法
result_sub = frac1 - frac2  # 1/3 - 3/4 = -5/12
print(result_sub)  # 输出结果：-5/12

# 乘法
result_mul = frac1 * frac2  # 1/3 * 3/4 = 1/4
print(result_mul)  # 输出结果：1/4

# 除法
result_div = frac1 / frac2  # 1/3 ÷ 3/4 = 4/9
print(result_div)  # 输出结果：4/9
```

### 四、分数与浮点数的转换

`Fraction`类可以与浮点数进行转换，但需要注意浮点数的精度问题。

#### 1. **分数转换为浮点数**：

```python
from fractions import Fraction

frac2 = Fraction('3/4')  # 创建分数3/4

float_value = float(frac2)  # 将分数3/4转换为浮点数0.75

print(float_value)  # 输出结果：0.75
```

#### 2. **浮点数转换为分数**：

当将浮点数转换为分数时，`Fraction`类会尝试找到最接近该浮点数的分数表示。可以使用`limit_denominator()`方法来限制分母的长度，以获得更简洁的分数表示。

```python
from fractions import Fraction

frac_from_float = Fraction(0.333333333333).limit_denominator()  # 将浮点数0.333333333333转换为分数1/3

print(frac_from_float)  # 输出结果：1/3

frac_from_float=Fraction(0.25)
print(frac_from_float)  # 输出结果：1/4

```

### 五、获取分数的分子和分母

可以通过访问`Fraction`对象的`numerator`和`denominator`属性来获取分数的分子和分母。

```python
from fractions import Fraction
frac2 = Fraction(3, 4)  # 创建分数3/4
numerator = frac2.numerator  # 获取分数3/4的分子3
print(numerator)
denominator = frac2.denominator  # 获取分数3/4的分母4
print(denominator)
```

### 六、分数的实际应用

**分数题目**:
从$\frac{1}{2}  +\frac{1}{3}+\frac{1}{4} ....+ \frac{1}{9} =?$

```python
from fractions import Fraction
# 初始化分数和
sum = Fraction(0)
for i in range(2, 10):
    # 累加分数
    sum += Fraction(1, i)

print(sum)  # 输出结果：4609/2520
```
