GESP Python一级冲刺阶段！编程题常考知识点汇总，助你一战必过！
 

### 1 循环读取n个正整数
#### 1.1 举例 输入一个数`n`,接下来输入`n`个正整数，累加这些正整数的和并输出

**参考代码**   
```python
# 读取正整数个数n
n = int(input())
# 初始化总和变量
total_sum = 0
# 循环读取n个正整数并累加
for _ in range(n):
    # 读取正整数a
    a = int(input())
    # 计算a的数位和
    total_sum += a
# 输出总和
print(total_sum)
```


### 2 两个逻辑判断组合的逻辑运算