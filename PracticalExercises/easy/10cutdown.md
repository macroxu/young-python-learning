10 倒计时程序（while 循环模拟）---python 实战初级

### 一、倒计时程序（while 循环模拟）  

#### 1 题目描述

实现一个 10 秒倒计时，每秒打印剩余秒数，结束后提示 “时间到！”。  

#### 2 示例输出

```
倒计时：10秒
倒计时：9秒
倒计时：8秒
倒计时：7秒
倒计时：6秒
倒计时：5秒
倒计时：4秒
倒计时：3秒
倒计时：2秒
倒计时：1秒
时间到！
```

#### 3 解题逻辑

1. **初始化倒计时**：设置一个变量 `countdown` 初始值为 10。
2. **使用 while 循环**：当 `countdown` 大于 0 时，打印当前倒计时秒数，并将 `countdown` 减 1。 同时使用 `time.sleep(1)` 函数实现每秒延时。
3. **结束提示**：当循环结束后，打印 “时间到！”。

#### 4 代码实现

```python
 
import time
countdown = 10
while countdown > 0:
    print(f"倒计时：{countdown}秒")
    time.sleep(1)  # 暂停1秒
    countdown -= 1

print("时间到！")

 

```
