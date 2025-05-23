Python教程：如何查找并识别水仙花数（Narcissistic Number）

**水仙花数**（Narcissistic Number），又称阿姆斯特朗数（Armstrong Number），是指一个三位数，其各位数字的立方和等于该数本身。  
例如，**$153 = 1^3 + 5^3 + 3^3$**，因此**153**是一个水仙花数。

### 一、水仙花数的定义

水仙花数是一个三位数，满足以下条件：

$ \text{百位数字}^3 + \text{十位数字}^3 + \text{个位数字}^3 = \text{该数本身}$

### 二、基本思路

* **确定范围**：通常我们会先确定一个范围，比如找出所有三位数的水仙花数（范围是 100 到 999）。
* **遍历范围内的每个数**：对于范围内的每一个数，我们需要将其各个位上的数字分离出来。
* **计算立方和**：将各个位上的数字的立方和计算出来。
* **判断是否为水仙花数**：将计算得到的和与原数进行比较，如果相等，则该数是水仙花数。

### 三、Python实现方法

#### 使用整除和取余操作

这种方法通过整除和取余操作分解出每个数位的数字，然后计算它们的立方和。

```python
# 查找水仙花数
def find_narcissistic_numbers():
    # 用于存储水仙花数的列表
    narcissistic_numbers = []
    # 遍历100到999之间的所有数
    for num in range(100, 1000):
        # 获取百位、十位、个位
        bai = num // 100 # 百位
        shi = (num // 10) % 10 # 十位
        ge = num % 10 # 个位
        # 计算立方和
        # 判断是否为水仙花数
        if bai ** 3 + shi ** 3 + ge ** 3 == num:
            # 将水仙花数添加到列表中
            narcissistic_numbers.append(num)
    # 返回水仙花数列表
    return narcissistic_numbers

# 输出结果
print("100到999之间的所有水仙花数为:", find_narcissistic_numbers())
```

### 四、运行结果

以上三种方法都会输出100到999之间的所有水仙花数，结果如下：

```
100到999之间的所有水仙花数为: [153, 370, 371, 407]
```
