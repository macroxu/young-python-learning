字符串操作
在 Python 中处理文本
连接字符串
更少
用 + 号连接或串联字符串：

display.scroll('hello ' + 'world')


分割字符串
更多
您可以使用字符的数字位置对字符串进行切片，从 0 开始计数。
切片类型：
这从字符 1 打印到 3，因此显示“el”：
display.scroll('hello'[1:3])

这将显示“h”，因为它是字符串中从 0 开始计数的第一个字符：

display.scroll('hello'[0])

这将显示从字符 2 开始的所有内容，因此显示“llo”：
display.scroll('hello'[2:])
此处显示字符 2 前的所有内容，所以显示“he”：
display.scroll('hello'[:2])

您可以采用同样方式分割字符串 变量。 这会将字符串从字符位置 1 分割到 3 并显示“el”：
word = 'hello'
display.scroll(word[1:3])

字符串相乘
您可以通过将字符串相乘来重复字符串：
display.scroll('hello' * 3)
上面的示例在 LED 显示屏上滚动 3 次 “hello”，无空格。

像这样将字符串相乘对于在串行控制台中打印简单的条形图很有用：

while True:
    print('X' * temperature())
    sleep(1000)

替换部分字符串
使用 replace() 将字符串的某些部分按其内容换出：
display.scroll('Hello world'.replace('Hello', 'Hola'))
这将显示“Hola world”。


修剪字符串
使用strip()从字符串的开头或结尾修剪字符：
display.scroll('wowow'.strip('w'))

这会从字符串的开头和结尾删除“w”，因此会显示“owo”。

您还可以使用此功能去除字符串开头或结尾的空格。 lstrip() 和 rstrip() 也会从字符串的左侧或右侧修剪空格。


字符串长度
使用 len() 来获取一个字符串的长度：
display.scroll(len('hello'))
因为该字符串长度为 5 个字符，所以将显示 5。

转换大小写
您可以将字符串转换为大写或小写。
选择转换：
这显示“HELLO”：
display.scroll('hello'.upper())

这显示“hello”:
display.scroll('HELLO'.lower())


搜索字符串
可以查找一个字符（或多个字符）的第一次和最后一次出现的位置。
选择位置:

第一次出现
您可以使用 find()来定位一个字符或一组字符第一次出现的位置。

因为第一个“i”位于字符位置 1，所以这里显示 1。
display.scroll('micro:bit'.find('i'))

如果使用 find() 或 rfind() 未找到任何内容，则返回 -1。

选择位置:

最后一次出现
使用 rfind() 查找一个字符或一组字符的最后一次出现。

因为最后一次出现的“i”位于字符位置 7，所以这里显示 7：
display.scroll('micro:bit'.rfind('i'))
如果使用 find() 或 rfind() 未找到任何内容，则返回 -1。


计算出现次数
使用count()计算一个字符或一组字符在字符串中出现的次数：
display.scroll('micro:bit'.count('i'))
这将显示 2 ，因为字母 “i” 在 'micro:bit.' 中出现了两次。

您还可以使用count() 来计算一个单词在字符串中出现的次数。 这将显示 2:
display.scroll('The rain it raineth every day'.count('rain'))

测试字符串
您可以测试字符串，以确定它们包含什么样的字符，或者它们是否包含某些字符。

选择测试

小写
if 'hello'.islower():
    display.scroll('lower case')


//

占位符
您可以在字符串中放置占位符，然后用变量的值替换放置的占位符：
name = 'Hana'
score = 17
time = 23.67
display.scroll('Hi %s you scored %i points in %1.2f seconds' % (name, score, time))

此示例中的输出是 ‘Hi Hana you scored 17 points in 23.67 seconds’（“Hana，您好，您在 23.67 秒内得到 17 分”）。

它使用%1.2f来指定显示两位小数。

使用 %s代表字符串，%i代表整数，%f 代表浮点数

字符的 ASCII 值
ASCII 是一个用于将存储在计算机系统中的数字编码为字母和符号的系统。

使用ord()来获取一个字符的ASCII值：
display.scroll(ord('a'))
因为字母“a”在 ASCII 中编码为数字 97，所以在此示例中显示 97。


根据 ASCII 值打印字符
使用 chr() 将数字 ASCII 值转换为字符串：
display.scroll(chr(98))

在本例中显示字母“b”。

在 Python 程序中使用 chr() 和 ord() 来编写像凯撒密码这样的代码时很有用。

此示例将字母“a”沿字母表中的顺序移动 5 个位置，使其变为“f”：

display.scroll(chr(ord('a') + 5))

以下示例使用偏移量 13 对字符串“hello”进行编码。 这种凯撒密码也被称为 ROT13。 您可以使用相同的代码对消息进行编码和解码：
plaintext = 'hello'
 
for letter in plaintext:
    if ord(letter) > 109:
        offset = -13
    else:
        offset = 13
    display.scroll(chr(ord(letter) + offset))




http://10.145.220.107:8113/50010373/vjsphtml/web/specialty_bill/detail_apply_bill.html?djid=2182fd7e06214f6b985ce3e086596ef8














