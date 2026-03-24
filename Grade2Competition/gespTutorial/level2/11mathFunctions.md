 
GESP Python 二级 简单数学函数：防超纲・冷门知识点考前扫盲


本文介绍了GESP Python二级考试考纲涉及到的简单数学函数，包含绝对值、平方根、最大最小值等常用函数。

### 1 绝对值函数 abs()
绝对值函数 abs() 用于返回一个数的绝对值，即该数与零的距离。对于正数和零，绝对值等于其本身；对于负数，绝对值等于其相反数。
```Python
# 绝对值函数示例
print(abs(-5))  # 输出: 5
print(abs(3))   # 输出: 3
print(abs(0))   # 输出: 0
```

### 2 平方根函数 math.sqrt()
平方根函数 math.sqrt() 用于返回一个数的平方根。需要注意的是，在使用前需要导入 math 模块。
```Python
import math
# 平方根函数示例
print(math.sqrt(16))  # 输出: 4.0

```

### 3 最大值和最小值函数 max() 和 min()
最大值函数 max() 用于返回一组数中的最大值，最小值函数 min() 用于返回一组数中的最小值。
```Python
# 最大值和最小值函数示例
# 最大值示例
print(max(1, 5, 3))  # 输出: 5
# 最小值示例
print(min(1, 5, 3))  # 输出: 1
```

### 4 四舍五入函数 round()
四舍五入函数 round() 用于将一个数四舍五入到指定的小数位。默认情况下，round() 会将数值四舍五入到最接近的整数。
round() 函数的语法如下：

round(number, ndigits)
- number：要进行四舍五入的数。
- ndigits：可选参数，指定要保留的小数位数。如果省略该参数，默认值为0，即四舍五入到最接近的整数。
  

```Python
# 四舍五入函数示例

print(round(3.14159, 2))  # 输出: 3.14
print(round(3.14159))     # 输出: 3
```

### 5 向下取整函数 math.floor() 
向下取整函数 math.floor() 用于返回小于或等于给定数的最大整数。需要注意的是，在使用前需要导入 math 模块。
```Python
import math
# 向下取整函数示例
print(math.floor(3.7))  # 输出: 3
print(math.floor(-3.7)) # 输出: -4
```

### 6 向上取整函数 math.ceil()
向上取整函数 math.ceil() 用于返回大于或等于给定数
的最小整数。需要注意的是，在使用前需要导入 math 模块。
```Python
import math
# 向上取整函数示例
print(math.ceil(3.2))  # 输出: 4
print(math.ceil(-3.2)) # 输出: -3
```
