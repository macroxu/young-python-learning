
1. **理解问题**：
    两个数的最大公约数（Greatest Common Divisor，简称 GCD）是能够同时整除这两个数的最大正整数。例如，12 和 18 的最大公约数是 6，因为 6 是 12 和 18 的公约数，且没有比 6 更大的公约数。

2. **分解问题**：
   为了更好的理解最大公约数，我们使用循环的方法单独计算每一个数的全部因数，然后找出两个数的公共因数，最后找出最大的公共因数。

3. **设计算法**：

   - 第一步 输入两个整数，分别为 `num1` 和 `num2`。
  
   - 第二步 计算 `num1` 和 `num2` 的全部因数。
      举例：循环 `num1`的全部因数,设置一个变量`i`从1到`num1`，如果`num1`能被`i`整除，那么`i`就是`num1`的一个因数。

   - 第三步，找出两个数的公共因数。
      举例：循环 `num1` 和 `num2` 的全部因数，如果两个数的因数相同，那么这个因数就是两个数的公共因数。

   - 第四步 找出最大的公共因数。

4. **编写代码**：
   - 根据算法步骤，使用具体的编程语言（如 Python）来编写代码。
   下面示例代码 来实现这个算法。

```python while 循环

#定义函数找出全部公约数
def 找出全部公约数function(num):
    num因数 = []
    i = 1
    while i <= num:
        if num % i == 0:
            num因数.append(i)
        i += 1

    # 打印出 num1 的全部因数 
    print(f"{num} 的全部因数是：{num因数}")
    return num因数



# 输入两个整数
num1 = int(input("请输入第一个整数："))
num2 = int(input("请输入第二个整数："))

# 初始化最大公约数
最大公约数 = 1

# 指出 num1 的全部因数，循环逐一找出全部因数
num1因数 = 找出全部公约数function(num1)


# 指出 num2 的全部因数，循环逐一找出全部因数
num2因数 = 找出全部公约数function(num2)

# 找出两个数的公共因数
公共因数 = []
for i in num1因数:
    if i in num2因数:
        公共因数.append(i)

# 打印出两个数的公共因数
print(f"{num1} 和 {num2} 的公共因数是：{公共因数}")

# 找出最大的公共因数
最大公约数 = max(公共因数)
print(f"{num1} 和 {num2} 的最大公约数是：{最大公约数}")

 ```

5. **代码优化扩展**：

- 上面的例子写的比较繁琐，如果纯粹的想得到答案可以用欧几里得算法（Euclid's algorithm），也叫做辗转相除法 ，来求最大公约数。

```python

# 定义函数找出最大公约数

def 最大公约数function(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1
    
# 输入两个整数
num1 = int(input("请输入第一个整数："))
num2 = int(input("请输入第二个整数："))

# 判断num1和num2的大小
# 如果num1小于num2，交换两个数
if num1 < num2:
    num1, num2 = num2, num1

num最大公约数= 最大公约数function(num1, num2)
#显示
print(f"{num1} 和 {num2} 的最大公约数是：{num最大公约数}")

```

- 原来的代码 本身也可以简化,可以在找一个函数的因数的同时再判断是否另外一个数的因数，这样就可以减少循环次数，提高效率

```python
#定义函数找出两个数的最大公约数
def 找出全部公约数function(num1,num2):
    最大num因数=0
    i = 1
    while i <= num1:
        if num1 % i == 0:
             #判断是否是num2的因数
            if num2 % i == 0:
                最大num因数 = i
        i += 1
    return 最大num因数
```
