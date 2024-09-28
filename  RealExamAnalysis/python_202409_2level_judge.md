24年GESP 9月认证 Python二级真题解析(二判断题部分)  

**第 1 题** 小杨最近开始学习Python编程，老师说Python是一门高级语言。（ ）  
答案：**对**  
**解析**：  
python是一门高级语言，它的语法简洁，易于学习，适合初学者入门。 同样是高级语言的还有Java、C++、C#等。
图形化编程语言有Scratch等。

**第 2 题** 在Python中，```print(3, 4, 5)```可以输出 ```3 4 5``` 每个输出项之间用空格分开。( )  
答案：**对**  
**解析**：  
print()函数输入多个参数时，会用空格分开输出。  

**第 3 题** Python表达式 ```12 % 10 % 10``` 的值为2。( )  
答案：**对**  
**解析**：
```12 % 10 % 10```，先计算12%10=2，再计算2%10=2，所以结果为2。

**第 4 题** Python表达式 round(12.56) 的值为13。（ ）  
答案：**对**  
**解析**：  
round()函数是四舍五入取整数的函数，参数为12.56，四舍五入后为13。  

**第 5 题** Python语句 print(input() + input()) 能将先后输入的内容拼接在一起。 ( )  
答案：**对**  
**解析**：  
input()函数用于接收用户输入并转化成字符串，input()+input() 等同于两个字符串相加，即拼接字符串，所以答案时对的。

**第 6 题**  下面的Python将导致死循环。（ ）  

```python
while True:
    break   
```

答案：**错**  
**解析**  
while True: 会一直循环，但是在循环体内有break语句，所以不会导致死循环。

**第 7 题** 下面Python代码执行后将输出10。（ ）  

```python
for i in range(10):
    continue
else:
    print(i)
```

答案：**错**  
**解析**  
for循环中的continue语句会跳过本次循环，继续下一次循环，i 最后的值时9，所以else语句执行的print(i)输出的是9。

**第 8 题** 下面Python代码能求整数N和M之间所有整数之和，包含N和M。（ ）  

```python
N = int(input())
M = int(input())
if N > M:
    N, M = M, N
Sum = 0
for i in range(N, M + 1):
    Sum += i
print(Sum)
```

答案：**对**  
**解析**  
阅读以上的代码,程序的执行过程如下：  

1. 读取用户输入的两个整数N和M，如果N大于M，交换两个数的值。保证N小于M，方便后面的循环。
2. 初始化变量Sum为0。
3. 从N开始循环到M，每次循环将i的值加到Sum上。
所以，以上代码能求整数N和M之间所有整数之和，包含N和M。

**第 9 题** 将下面Python代码中的range(1, 5)调整为range(5)输出结果相同。（ ）  

```python
loopCount = 0
for i in range(1, 5):
    for j in range(i):
        loopCount += 1
print(loopCount) 
```

答案：**对**  
**解析**  
如果将range(1, 5)调整为range(5)，则代码比原来多执行了一次``i=0``，当``i=0``时，``range(0)``为空，所以不会进入内层循环，所以结果相同。

**第 10 题** 某一系列数据的规律是从第3个数值开始是前两个数之和。下面的代码求第N个数的值，N限定为大于2。（ ）  

```python
start1 = int(input()) #第1个数
start2 = int(input()) #第2个数
N = int(input()) #求N个数的值
for i in range(2, N):
    start1, start2 = start2, start1 + start2
print(start2)

```

答案：**对**  
**解析**  
阅读以上的代码,程序的执行过程如下：  

1. 读取用户输入的两个整数start1和start2，分别表示第1个数和第2个数。
2. 读取用户输入的整数N，表示求第N个数的值。
3. 从第3个数开始，每个数是前两个数之和，所以从第3个数开始，每次循环将start1和start2的值交换，start2的值变为start1和start2的和。
4. 循环结束后，打印出第N个数的值，即start2的值。
