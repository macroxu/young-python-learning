11 计算班级平均分---python 实战初级

### 一、计算班级平均分  

#### 1 题目描述

给定一组班级同学的成绩，计算班级平均分，根据班级学生的成绩列表，计算出平均分。

#### 2 示例输出

```
班级平均分: 86.71
```

#### 3 解题逻辑

1. **给定一组同学成绩**：可以使用一个列表来存储同学的成绩。
2. **计算总分**：使用循环遍历列表，累加每个同学的成绩。
3. **计算平均分**：将总分除以同学人数。
4. **输出结果**：使用格式化字符串输出平均分，保留两位小数。

#### 4 代码实现

```python
# 班级分数列表
scores = [85, 92, 78, 90, 88, 95, 79]
# 计算总分
total = 0

for score in scores:
    total += score
# 计算平均分
average = total / len(scores)

print(f"班级平均分: {average:.2f}") 
 
```
