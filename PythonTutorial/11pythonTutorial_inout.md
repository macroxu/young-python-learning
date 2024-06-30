Python 提供了多种方法来处理输入和输出。最常见的输入和输出函数是 `input()` 和 `print()`。下面是一个简单的 Python 输入输出教程。

### 输入（Input）

在 Python 中，`input()` 函数用于从用户那里获取输入。这个函数将等待用户输入一些文本，然后按回车键。输入的文本将作为字符串返回。

示例：

```python
# 获取用户输入的姓名
user_name = input("请输入你的姓名: ")

# 输出用户输入的姓名
print("你输入的是: " + user_name)
```

```python
# 获取用户输入的年龄
user_age = input("请输入你的年龄: ")

# 用户五年后的年龄
future_age = int(user_age) + 5
print("你五年后的年龄是: " + future_age)
```

注意：`input()` 函数总是返回字符串。如果你需要其他类型的数据（如整数或浮点数），你需要使用适当的函数（如 `int()` 或 `float()`）将字符串转换为所需的数据类型。

### 输出（Output）

在 Python 中，`print()` 函数用于在屏幕上显示文本或变量的值。你可以传递一个或多个参数给 `print()` 函数，它们将被转换为字符串并输出到屏幕上。

示例：

```python
# 输出字符串
print("Hello, World!")

# 输出变量的值
name = "张晓明"
age = 11
print("我的名字是 " + name + "，我 " + str(age) + " 岁了。")

# 使用格式化字符串（Python 3.6+）
print(f"我的名字是 {name}，我 {age} 岁了。")
```

#### 格式化输出

注意：在上面的示例中，我们使用 `str()` 函数将整数 `age` 转换为字符串，以便与字符串进行连接。但是，从 Python 3.6 开始，你可以使用格式化字符串（也称为 f-string）来**更简洁地**实现相同的效果。

除了简单的字符串连接外，Python 还提供了多种方法来格式化输出，包括使用 `%` 运算符、`str.format()` 方法以及 f-string。

* 使用 `%` 运算符：

```python
name = "张晓明"
age = 11
print("我的名字是 %s，我 %d 岁了。" % (name, age))
```

* 使用 `str.format()` 方法：

```python
name = "张晓明"
age = 11
print("我的名字是 {}, 我 {} 岁了。".format(name, age))
```

* 使用 f-string（Python 3.6+）：

```python
name = "张晓明"
age = 11
print(f"我的名字是 {name}，我 {age} 岁了。")
```

这些格式化方法允许你以更灵活和可读的方式创建和显示字符串。
