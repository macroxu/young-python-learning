字符串操作
在 Python 中处理文本

## 1 连接字符串

用 + 号连接或串联字符串：

``` python
print('hello ' + 'world')

```

``` shell
# 输出
hello word

```

## 2 切割字符串

您可以使用字符的数字位置对字符串进行切片，从 0 开始计数。

### 2.1  按范围切割字符串

这从字符 1 打印到 3，因此显示“el”：

``` python
print('hello'[1:3])
```

``` shell
# 输出
el
```

### 2.2  按单个字符切割字符串

这将显示“h”，因为它是字符串中从 0 开始计数的第一个字符：

``` python
print('hello'[0])
```

``` shell
# 输出
h
```

### 2.3  切割After(之后)的字符串

这将显示从字符 2 开始的所有内容，因此显示“llo”：

``` python
print('hello'[2:])
```

``` shell
# 输出
llo
```

### 2.4  切割before(之前)的字符串

此处显示字符 2 前的所有内容，所以显示“he”：

``` python
print('hello'[:2])
```

``` shell
# 输出
he
```

## 3 字符串重复

您可以通过将字符串相乘来重复字符串：

``` python
print('hello ' * 3)
```

``` shell
# 输出
hello hello hello
```

像这样将字符串相乘对于在串行控制台中打印简单的条形图很有用：

``` python
#打印一个条形图
print('*' * 10)
```

``` shell
# 输出
**********

```

## 4 替换部分字符串

使用 replace() 将字符串的某些部分按其内容换出：

``` python
print('Hello world'.replace('Hello', 'Hola'))
```

``` shell
# 输出
Hola world

```

### 5 修剪字符串

使用strip()从字符串的开头或结尾修剪字符：

``` python
print('wowow'.strip('w'))
```

``` shell
# 输出
owo
```

这会从字符串的开头和结尾删除“w”，因此会显示“owo”。

您还可以使用此功能去除字符串开头或结尾的空格。 lstrip() 和 rstrip() 也会从字符串的左侧或右侧修剪空格。

### 6 字符串长度

使用 len() 来获取一个字符串的长度：

``` python
print(len('hello'))
```

``` shell
# 输出
5
```

因为该字符串长度为 5 个字符，所以将显示 5。

### 7 字符串转换大小写

您可以将字符串转换为大写或小写。

这显示“HELLO”：

``` python
print('hello'.upper())
```

``` shell
# 输出
HELLO
```

这显示“hello”:

``` python
print('HELLO'.lower())
```

``` shell
# 输出
hello
```

### 8 搜索字符串

可以查找一个字符（或多个字符）的第一次和最后一次出现的位置。

#### 8.1 第一次出现

您可以使用 find()来定位一个字符或一组字符第一次出现的位置。

因为第一个“i”位于字符位置 1，所以这里显示 1。

``` python
print('micro:bit'.find('i'))
```

如果使用 find() 或 rfind() 未找到任何内容，则返回 -1。

#### 8.2 最后一次出现

使用 rfind() 查找一个字符或一组字符的最后一次出现。

因为最后一次出现的“i”位于字符位置 7，所以这里显示 7：

``` python
print('micro:bit'.rfind('i'))

```

如果使用 find() 或 rfind() 未找到任何内容，则返回 -1。

### 9 计算出现次数

使用count()计算一个字符或一组字符在字符串中出现的次数：

这将显示 2 ，因为字母 “i” 在 'micro:bit.' 中出现了两次。

``` python
print('micro:bit'.count('i'))

```

您还可以使用count() 来计算一个单词在字符串中出现的次数。 这将显示 2:

``` python
print('The rain it raineth every day'.count('rain'))

```

### 10 测试字符串

您可以测试字符串，以确定它们包含什么样的字符，或者它们是否包含某些字符。

#### 10.1 测试小写大写

``` python
if 'hello'.islower():
    print('lower case')
```

``` shell
# 输出
lower case
```

#### 10.2 测试是否包含数字

``` python
if '123'.isdigit():
    print('all digits')
```

``` shell
# 输出
all digits
```

#### 10.3 测试是否包含特定字符串

``` python
if 'hello'.startswith('he'):
    print('starts with he')
```

``` shell
# 输出
starts with he
```

#### 10.4 测试是否已特定字符串开始

``` python
if 'hello'.endswith('lo'):
    print('ends with lo')
```

``` shell
# 输出
ends with lo
```

#### 10.5 测试是否已特定字符串结束

``` python
if 'hello'.endswith('lo'):
    print('ends with lo')
```

``` shell
# 输出
ends with lo
```

### 11 字符串占位符

您可以在字符串中放置占位符，然后用变量的值替换放置的占位符：

``` python
name = 'Hana'
score = 17
time = 23.67
print('Hi %s you scored %i points in %1.2f seconds' % (name, score, time))
```

``` shell
# 输出
Hi Hana you scored 17 points in 23.67 seconds
```

在此示例中，%s 用于字符串，%i 用于整数，%f 用于浮点数。 %1.2f 用于显示两位小数。

### 12 字符的 ASCII 值

ASCII 是一个用于将存储在计算机系统中的数字编码为字母和符号的系统。

使用ord()来获取一个字符的ASCII值：

``` python
print(ord('a'))

```

``` shell
# 输出
97
```

因为字母“a”在 ASCII 中编码为数字 97，所以在此示例中显示 97。

### 13 根据 ASCII 值打印字符

使用chr()将数字 ASCII 值转换为字符串：

``` python
print(chr(98))

```

``` shell
# 输出
b
```

在本例中显示字母“b”。
