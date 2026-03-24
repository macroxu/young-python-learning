### 在 GESP 考试中 如何在无调试功能的情况下，快速的实现复杂编程题

在 GESP 编程考试中，我们没有调试功能，无法直接在考试界面调试代码。  

但我们可以通过将一个复杂的问题切分成多个独立的小问题来逐步解决。每个小问题都可以单独编写代码来解决，这样我们就可以在 PyCharm 中测试每个小问题的代码，确保它们都能正确运行，然后再将它们组合成一个完整的程序。

#### 举例，将复杂问题切分成多个小问题
**比如下面是一个复杂的问题**：  
输入一个数，判断这个数的各个数位中是否包含数字**7**，如果包含数字7，则输出这个数的每个数位的**平方和**，否则输出这个数的每个数位的**立方和**。

**输入例子**：
```
1276
```

**输出例子**：
``` 
这个数包含数字7
数位的平方和是:90
```


这个问题可以切分成以下几个小问题：
1. 输入一个数，并判断这个数的各个数位中是否包含数字7。
2. 给定一个数，输出这个数的每个数位的平方和。
3. 给定一个数，输出这个数的每个数位的立方和。

#### 2 编写代码解决每个小问题

##### 2.1 判断数位中是否包含数字7
```python

num=int(input("请输入一个数："))
flag=False
while num>0:
    digit=num%10
    if digit==7:
        flag=True
    num//=10
if flag:
    print("这个数包含数字7")
else:
    print("这个数不包含数字7")
```

##### 2.2 输出数位的平方和
```python
num=int(input("请输入一个数："))
sum_of_squares=0
while num>0:
    digit=num%10
    sum_of_squares+=digit**2
    num//=10
print("数位的平方和是：", sum_of_squares)
```

##### 2.3 输出数位的立方和
```python
num=int(input("请输入一个数："))
sum_of_cubes=0
while num>0:
    digit=num%10
    sum_of_cubes+=digit**3
    num//=10
print("数位的立方和是：", sum_of_cubes)
```


#### 3 将小问题的代码组合成一个完整的程序
```python
# 1. 输入数字后，先保存原始值（关键修改！）
num = int(input("请输入一个数："))
original_num = num  # 保存原始输入的数，避免被第一个循环修改
flag = False

# 2. 第一个循环：判断是否包含数字7（这里修改的是num，不影响original_num）
while num > 0:
    digit = num % 10
    if digit == 7:
        flag = True
    num = num // 10

# 3. 第二个/第三个循环：用保存的original_num计算平方和/立方和
if flag:
    print("这个数包含数字7")
    sum_of_squares = 0
    temp = original_num  # 用原始值计算
    while temp > 0:
        digit = temp % 10
        sum_of_squares += digit ** 2
        temp = temp // 10
    print("数位的平方和是：", sum_of_squares)
else:
    print("这个数不包含数字7")
    sum_of_cubes = 0
    temp = original_num  # 用原始值计算
    while temp > 0:
        digit = temp % 10
        sum_of_cubes += digit ** 3
        temp = temp // 10
    print("数位的立方和是：", sum_of_cubes)
```

> 这样我们就成功地将一个复杂的问题切分成了多个小问题，并且通过编写代码解决每个小问题，最终将它们组合成了一个完整的程序。在 GESP 考试中，这种方法可以帮助我们更快地实现复杂的编程题，避免在编写代码时遇到困难。