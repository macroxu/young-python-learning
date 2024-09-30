Python 中的输入输出语句主要依赖于内置的 `input()` 函数用于接收用户输入，以及 `print()` 函数用于向用户显示输出。下面分别介绍这两个函数的基本用法和一些进阶技巧。

### 1. `print()` 函数

`print()` 函数用于在屏幕上输出信息。它可以将传入的多个参数转换成字符串（如果它们不是字符串的话），并在每个字符串之间添加空格，然后输出到屏幕，并在末尾自动添加换行符。

#### 1.1 基本用法

```python
#输出单一字符串
print("Hello, World!") # 输出 Hello, World!

# 输出多个值
print("Hello,", "World!")  # 输出 Hello, World!

# 使用变量
name = "Alice"
print("Hello,", name)  # 输出 Hello, Alice

# 不换行输出
print("Hello,", end=" ")  # 注意这里 end 参数改变了默认的换行行为
print("World!")  # 这将紧接着上一行输出
# 输出结果：Hello, World!

#换行输出
print("第一行")
print("第二行")
# 输出结果：
# 第一行
# 第二行

# 输出数字
age = 30
print("你今年", age, "岁了.")  # 输出 你今年 30 岁了.


```

#### 1.2 带变量格式化输出

Python 提供了多种格式化输出的方式，比如使用 `%` 操作符、`str.format()` 方法以及 f-string（Python 3.6+）。
>f-string 是 Python 3.6 引入的一种新的字符串格式化方法，它使用 `{}` 和 `:` 来代替 `%` 操作符，使得字符串格式化更加简洁和直观。

- f-string（格式化字符串字面量）：

  ```python
  name = "李四"
  age = 28
  print(f"姓名是: {name}, 年龄: {age}")
  ```

- `%` 操作符：

  ```python
  name = "张三"
  age = 30
  print("姓名是: %s, 年龄: %d" % (name, age))
  ```

- `str.format()` 方法：

  ```python
  name = "张三"
  age = 25
  print("姓名是: {}, 年龄: {}".format(name, age))
  # 或者使用关键字参数
  print("Name: {name}, Age: {age}".format(name=name, age=age))
  ```

#### 1.3 输出不换行

如果你不想在 `print()` 调用之后自动换行，可以在 `print()` 函数中使用 `end` 参数来指定字符串的结尾，
`end` 参数的默认值是换行符 `\n`，你可以将其设置为任何你想要的字符串。
例如：

```python
print("Hello,", end=" ")
print("World!")
# 输出结果：Hello, World!

print("张三", end=",")
print("李四")
# 输出结果：张三,李四
```

### 2. `input()` 函数

`input()` 函数用于接收用户的输入。当程序执行到 `input()` 函数时，程序会暂停并等待用户输入一些文本。用户输入文本后按下回车键，`input()` 函数就会读取这个文本，并将其作为一个```字符串```返回。
>特别提醒 input() 函数返回的是字符串，如果需要其他类型的数据，需要进行```类型转换```。

#### 2.1 基本用法

```python
账号 = input("请输入你的账号: ")
print("欢迎您", 账号)
```

#### 2.2 注意事项

- `input()` 函数读取的是字符串（即使看起来像是数字）。如果你需要将其转换为其他类型（如整数或浮点数），你需要使用相应的类型转换函数，如 `int()` 或 `float()`。

  ```python
  num1 = int(input("请输入第一个数num1: "))
  num2 = int(input("请输入第二个数num2: "))
  sum = num1 + num2
  print("num1和num2的和是：", sum)
  ```

- 用户输入的内容是原始的，包括空格和特殊字符。因此，你可能需要在使用之前对用户输入进行```清理```或```验证```。

以上就是 Python 中输入输出语句的基本教程。通过这些基本的输入输出操作，你可以开始构建与用户交互的 Python 程序了。
