### python基础教程--列表(数组)
<p>列表或数组是数据的集合。 它们可以由变量、数字、字符串或不同数据类型的混合组成。</p>
<p>列表中的项目称为元素。</p>
<p>列表中项目的位置是它的索引。 Python 从 0 开始计数，因此列表中的第一个元素位于索引 0 处。</p>

#### 1 创建列表
> 像变量一样，在创建列表时为其命名。 列表中的元素放在方括号内，每个元素间用逗号分隔：
``` python
numbers = ['zero', 'one', 2]
```
* 字符串必须包含在引号中。

>您可以创建一个空列表，稍后再添加内容：
``` python
numbers = []
```

#### 2 获取列表元素
1. **随机**获取列表元素
>导入 random 模块，以便您可以使用 random.choice() 从列表中获取一个随机元素：
``` python
import random

students = ['小张', '小李', '小王']
chooseOneStudent= random.choice(students)
print("随机抽取的中奖的同学是"+chooseOneStudent)

```
2. **数字索引**获取列表元素
>可以使用数字索引访问列表中的元素，第一项从 0 开始。
``` python
students = ['小张', '小李', '小王']
print("队列中的第二位同学是"+students[1])
```
3. **循环**依次访问列表全部数据
>您可以使用“for”循环依次访问列表的所有元素：
``` python
students = ['小张', '小李', '小王']
print("队列中的同学有：")
for student in students:
    print(student)
```

#### 3 更改列表元素
这将用字符串**two**  替换索引**2**处的值：
``` python
numbers = ['zero', 'one', 2]
numbers[2] = 'two'
print(numbers[2])
```

#### 4 增加队列元素
1. 使用insert （插入）在列表中的给定点添加元素：
``` python
letters = ['a', 'b', 'd']
letters.insert(2,'c')
```
这将在索引2位置中插入字母“c”，这其实是在以0开始计数的列表中的第三个位置。

2. 将项目添加或追加到列表的末尾，如下所示：
``` python
letters = ['a', 'b', 'c']
letters.append('d')
```

#### 5从列表中删除元素
选择方法 按索引 (pop)  按值（remove） 清空列表
1. 按索引删除元素
您可以使用 pop(): 按列表中的位置依次删除项目
``` python
letters = ['a', 'b', 'c', 'd']
letters.pop(1)
```
>这将从列表中删除索引 1 处的项目，即字母“b”。

2. 按值删除元素
如果您知道元素的值但不知道它在列表中的位置，请使用 remove() 删除元素：
``` python
letters = ['a', 'b', 'c', 'd']
letters.remove('c')
```
>这将从列表的任何位置删除“c”。

3. 清空列表
使用 clear() 从列表中删除所有元素：
``` python
letters = ['a', 'b', 'c', 'd']
letters.clear()
```

#### 6排序列表
1. 按**字母数字**排序
使用 sort() 对列表进行字母数字排序：
``` python
letters = ['c', 'd', 'b', 'a']
letters.sort()
print(letters) ## 当前的数组值
```
这会将列表按字母顺序排序：'a'、'b'、'c'、'd'。

2. **反转**数组
 
您可以反转由不同数据类型组成的列表，但您只能按字母数字顺序对包含相同数据类型的列表进行排序，比如所有元素必须是字符串或整数。  

使用reverse()反转列表的顺序：
```python
letters = ['a', 'b', 'c', 'd']
letters.reverse()
print(letters) ## 当前的数组值
```
这会将列表的顺序颠倒为“d”、“c”、“b”、“a”。

#### 7 获取列表的长度
使用 len() 函数获取列表的长度：
``` python
letters = ['a', 'b', 'c', 'd']
print(len(letters))
##这将显示 4 ，因为列表中有 4 个元素。
```

#### 8 计算列表中出现的次数
使用count()计算特定元素在列表中出现的次数：
``` python
numbers = [5, 7, 0, 5]
print(numbers.count(5))
```
因为 5 在列表中出现了两次，所以显示 2。









