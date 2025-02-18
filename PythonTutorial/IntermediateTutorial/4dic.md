以下是对Python中字典(dict)的详细教程：

python中级教程--字典(dict)

Python字典(dict)是一种常用的数据结构，用于存放具有映射关系的数据，由键（key）和值（value）成对组成。
Python字典(dict)具有以下特点：

1. 字典中的键是**唯一的**，不允许重复。
2. 字典中的键是**不可变的**，通常使用字符串、数字或元组作为键。
3. 字典中的值可以是**任意数据类型**，如字符串、数字、列表、元组等。
4. 字典是**无序的**（Python 3.6及之前版本），但从Python 3.7开始，字典默认是**有序的**，即按照插入顺序排列。

Python字典(dict)的使用场景非常广泛，例如存储配置信息、缓存数据、映射关系等。

### 一、字典的创建

#### 1. **使用花括号{}**

这是创建字典最简单和直观的方法。

```python
d1 = {'apple': 3, 'orange': 5, 'grape': 10}
```

#### 2. **使用dict()函数**

使用dict()函数可以通过关键字参数创建字典：

```python
d2 = dict(apple=3, orange=5, grape=10)
print(d2)  # 输出: {'apple': 3, 'orange': 5, 'grape': 10}

```

或者通过包含**键值对元组**的列表来创建字典：

```python
lst = [('Author', '张三'), ('age', 21), ('sex', '男'), ('height', 175)]
d3 = dict(lst)
print(d3)  # 输出: {'Author': '张三', 'age': 21, 'sex': '男', 'height': 175}
```

3. **使用fromkeys()方法**：  
fromkeys()方法用于创建一个新字典，其中包含指定键的默认值。

```python
d4 = dict.fromkeys(('tomato', 'potato'), 10)
print(d4)  # 输出: {'tomato': 10, 'potato': 10}

```

### 二、字典元素的访问

#### 1. 通过键来访问字典中的值,如果访问不存在的键，会抛出KeyError异常

```python
d1 = {'apple': 3, 'orange': 5}
print(d1['apple'])  # 输出: 3
```

##### 2. 使用get()方法,如果访问不存在的键，不会抛出异常，而是返回默认值None

```python
print(d1.get('banana', 0))  # 输出: 0，'banana'键不存在，返回默认值0
```

### 三、字典元素的操作

#### 1. **添加或更新元素**

- 通过键添加新元素：

```python
d1['banana'] = 2  # 添加新键值对
```

- 通过键更新已有元素的值：

```python
d1['apple'] = 4  # 更新'apple'键对应的值
```

- 使用update()方法添加或更新多个键值对：

```python
d1.update(pear=3, peach=6)
```

#### 2. **删除元素**

- 使用del语句删除指定键的元素：

```python
del d1['orange']
```

- 使用pop()方法删除指定键的元素，并返回其值，如果键不存在，会抛出KeyError异常：
  
```python
value = d1.pop('grape')
```

- 使用popitem()方法删除并返回字典中的最后一个键值对（Python 3.7+保证有序）：

```python
key, value = d1.popitem()
```

- 使用clear()方法清空字典中的所有元素：

```python
d1.clear()
```

#### 3. **判断键是否存在**

判断字典中是否存在某个键，可以使用**in**关键字：

```python
if 'apple' in d1:
    print('Apple exists in the dictionary')
```

### 四、字典的遍历操作

#### 1. **查询所有元素items()方法**

items()方法返回一个包含所有键值对的元组列表。

```python
d1 = {'apple': 1, 'orange': 5, 'grape': 10}
for key, value in d1.items():
    print(f'{key}: {value}')
# 输出:
# apple: 1
# orange: 5
# grape: 10

```

#### 2. **查询所有键方法**

可以直接遍历字典的键：

```python
d1 = {'apple': 1, 'orange': 5, 'grape': 10}
for key in d1:
    print(key, end=' ')
# 输出: apple orange grape
```

或者，keys()方法返回一个包含所有键的列表。

```python
d1 = {'apple': 1, 'orange': 5, 'grape': 10}
for key in d1.keys():
    print(key, end=' ')
# 输出: apple orange grape
```

#### 3. **查询所有值values()方法**

values()方法返回一个包含所有值的列表。

```python
d1 = {'apple': 1, 'orange': 5, 'grape': 10}
for value in d1.values():
    print(value, end=' ')
# 输出: 1 5 10
```

#### 4. **计算字典长度**

len()函数可以用来计算字典中键值对的数量。

```python
d1 = {'apple': 1, 'orange': 5, 'grape': 10}
length = len(d1)
print(length)  # 输出: 3

```

### 四、字典的集合操作

#### 1. **合并字典**

python合并字典有多种方法：

- 在Python 3.9及以上版本，可以使用|运算符合并字典：

>如果两个集合有相同的键，则后一个字典的值将覆盖前一个字典的值。

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = dict1 | dict2  # {'a': 1, 'b': 3, 'c': 4}
```

- 在较早版本的Python中，可以使用update()方法合并字典：

```python
dict1.update(dict2)
```

### 五 **字典推导式**

 python中，字典推导式是一种快速创建字典的方法，类似于列表推导式。  
 比如，我们可以通过列表推导式创建一个字典，如下所示：

```python
squares = {x: x*x for x in range(6)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 也可以通过过滤条件创建字典
even_squares = {x: x*x for x in range(6) if x % 2 == 0}  # {0: 0, 2: 4, 4: 16}

```
