Python 有许多内置函数，如 sleep() 和 int()，但您可以创建自己的函数，以便在您的程序中重用代码段。

函数使代码更易于阅读和修改。 在程序开头附近定义您的函数，给它取一个描述性强的名字，然后用它的名字加上圆括号来调用它。
程序
过程，也称为子例程，是执行一组固定指令的函数。

```python
### 定义一个简单函数例子

def sayHello():
    print('Hello, world!')
    sleep(1000)
    print('Goodbye, world!')

sayHello()


这个函数称为sayHello()。 它打印“Hello, world!”，然后等待 1 秒，然后打印“Goodbye, world!”。

带参数的函数
您可以将数据放在括号中将其传递给函数，然后函数才可以处理这些数据。
#这个函数接受一个字符串参数，并将其打印到控制台：
def print_message(message):  
    """  
    这个函数接受一个字符串参数，并将其打印到控制台。  
    """  
    print(message)  
  
# 使用函数  
print_message("这是一个测试消息")  # 输出: 这是一个测试消息

 

在本例中，我们定义了一个函数，名为image_wait()。 它将显示我们传递给函数的任何图像。

传递给函数的数据被称为参数。 参数使函数更加灵活。

您可以向函数传递多个参数。 此函数允许您指定图像和函数等待的时间。 默认延迟为 1 秒，但您可以通过在调用函数时指定新时间来覆盖它：
def greet(name, greeting="Hello"):  
    """  
    这个函数接受一个名字参数和一个可选的问候语参数（默认为"Hello"），  
    并在控制台上打印出问候消息。  
    """  
    print(f"{greeting}, {name}!")  
  
# 使用函数，只提供必需参数  
greet("Alice")  # 输出: Hello, Alice!  
  
# 使用函数，提供必需参数和默认参数  
greet("Bob", "Hi")  # 输出: Hi, Bob!
 

带返回值的函数
函数可以处理信息并返回信息。
此函数接受您传递给它的任何数字，使用将摄氏度转换为华氏度的公式对其进行修改，然后将其返回。

def add_numbers(num1, num2):  
    """  
    这个函数接受两个参数并返回它们的和。  
    """  
    sum = num1 + num2  
    return sum  
  
# 使用函数  
result = add_numbers(5, 3)  
print(result)  # 输出: 8

函数 convertCtoF() 在 display.scroll() 语句中被调用。 以摄氏度为单位的当前温度被传递给函数。

“Function” （函数）是一个数学术语，用于描述一个或多个变量的关系或表达式，例如 F = C x 1.8 + 32。

计算机程序中的函数以类似的方式工作，这就是它们适合执行计算和转换的原因。

变量作用域
变量并不总是适用于程序的所有部分。 有时候这是您想要的，但它可能会导致问题。 变量可以是 全局 或 局部的。

程序的任何部分都可以访问全局变量。 局部变量仅在程序的一部分（例如函数）内起作用。

作用域：全局变量
更少
如果您在函数定义之外创建变量，它将是可以被函数使用的全局变量。

def greeting():
    display.scroll('Hello ' + name)

name = 'Sam'
greeting()

在本例中，显示屏显示“Hello Sam”（你好，山姆）。

虽然name是全局变量，但必须先定义它，然后函数greeting()才能被调用，否则会报错。

如果您想在函数中修改一个全局变量的值，您必须声明您想使用的那个名字的全局变量为global。

这里我们使用全局变量 count 来跟踪函数被调用的次数：

# 定义一个全局变量  global_count 统计次数
global_count = 0  
  
def clickEvent():  
    # 使用global关键字声明我们要修改的是全局变量  
    global global_count  
    # 修改全局变量的值  
    global_count += 1  
    print(f"在函数内部，全局变量 global_count 的值为: {global_count}")  
  
# 调用函数修改全局变量  
clickEvent()  
print(f"在函数外部，全局变量 global_count 的值为: {global_count}")

作用域：局部变量
除非您另有说明，函数内的变量将被假定为local（局部）变量。

def count():
    number = 9
    display.show(number)

number = 5
count()
sleep(1000)
display.show(number)

这里我们有两个名为 number 的变量实例。 在count()函数内部，number是一个局部变量，其值为9。

在函数外部有一个全局变量，也叫number，其值为 5。

您可能期望调用该函数会将 number 的值更改为 9 ，并显示 9 两次。 但实际上这会在显示屏上显示 9 和 5，因为存在两个都叫做number的不同变量。 一个是函数的局部变量，其值为 9，另一个是函数的全局变量，其值为 5。