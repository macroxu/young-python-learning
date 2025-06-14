
《数学神器SymPy实战：Python秒解初高中因式分解》

### 1 初中高中数学因式分解的定义、核心要点及与其他运算的区别

在初高中数学中，**因式分解**（又称“分解因式”）是一种重要的代数恒等变形，其核心是将一个多项式表示为**几个整式乘积**的形式。以下是其严格定义、核心要点及与其他运算的区别：

#### **一、因式分解的定义**

**定义**：  
把一个**多项式** $f(x)$ 化成**几个整式**  $p_1(x), p_2(x), \dots, p_n(x)$  的**乘积**形式，即  
$
f(x) = p_1(x) \cdot p_2(x) \cdot \dots \cdot p_n(x),
$
其中每个 $p_i(x)$ 均为整式，且分解后的整式次数低于原多项式的次数（或为常数）。这种变形过程称为**因式分解**。

#### **二、常见数域范围**

因式分解的结果依赖于所指定的**数域**（即允许使用的数的范围）：  

1. **有理数域**：仅允许使用有理数作为系数，例如 $x^2 - 4 = (x - 2)(x + 2)$（合法），但 $x^2 - 3$ 不可分解。  
2. **实数域**：允许使用实数作为系数，例如 $x^2 - 3 = (x - \sqrt{3})(x + \sqrt{3})$。  
3. **复数域**（高中拓展）：允许使用复数，例如 $x^2 + 1 = (x + i)(x - i)$（$i$) 为虚数单位）。  

**初中阶段**一般默认在**有理数域**内分解，**高中阶段**可能扩展到实数域或复数域。

#### **三、学习意义与应用**

1. **简化运算**：  
   例如计算 $\frac{x^2 - 2x + 1}{x - 1}$ 时，因式分解后可约分为 $x - 1$（$x \neq 1$）。  
2. **解方程与不等式**：  
   例如方程 $x^2 - 5x + 6 = 0$ 可分解为 $(x - 2)(x - 3) = 0$，直接得解 $x = 2$ 或 $x = 3$。  
3. **代数推理基础**：  
   在分式化简、根式运算、函数解析式变形中广泛应用，是高中数学（如数列、导数）的重要工具。

>**因式分解**是将多项式转化为**整式乘积**的恒等变形，需遵循“**对象为多项式、结果为整式乘积、分解彻底**”的原则。  
其核心是通过观察多项式结构，选择合适的方法（如**提取公因式**、**公式法**、**十字相乘法**等），体现了“**化复杂为简单**”的数学思想，是连接代数运算与实际应用的关键纽带。

### 2 使用 SymPy 进行因式分解

#### **1. 安装与导入**

首先安装 SymPy（若未安装）：

```bash
pip install sympy
```

在 Python 脚本中导入所需功能：

```python
from sympy import symbols, factor, factorint, simplify
```

#### **2. 多项式因式分解**

##### **2.1基本用法**

定义符号变量并分解多项式 $x^2 - 4$：

```python
from sympy import symbols, factor
x = symbols('x')
expr = x**2 - 4  # 定义多项式
factored = factor(expr)  # 分解
print(factored)  # 输出: (x - 2)*(x + 2)
```

##### **2.2 高次多项式**

SymPy 可处理高次多项式$x^3 - 6*x^2 + 11*x - 6$：

```python
from sympy import symbols, factor
x = symbols('x')
expr = x**3 - 6*x**2 + 11*x - 6
factored = factor(expr)
print(factored)  # 输出: (x - 1)*(x - 2)*(x - 3)
```

##### **2.3多元多项式**

支持多变量分解(**二元的因式分解**)：

```python
from sympy import symbols, factor
x, y = symbols('x y')
expr = x**2 - y**2
factored = factor(expr)
print(factored)  # 输出: (x - y)*(x + y)
```

#### **3 无理数域因式分解**

对于无理数域的多项式，例如 $x^2 - 2$，可以使用 `extension` 参数指定扩展域：**sqrt(2)**：

```python
from sympy import symbols, factor, sqrt
x = symbols('x')
expr = x**2 - 2
factored = factor(expr,extension=sqrt(2))
print(factored)  # 输出: (x - sqrt(2))*(x + sqrt(2))
```

#### **4 复数域因式分解**

若需在复数域分解，指定扩展参数**I 代表数学中的虚数单位**：

```python
from sympy import symbols, factor, I
x = symbols('x')
expr = x**2 + 1
factored = factor(expr, extension=[I])
print(factored)  # 输出: (x - I)*(x + I)
```
