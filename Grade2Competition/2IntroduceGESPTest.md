GESP Python认证考试注意事项和考试界面介绍

### 一、**GESP Python考点机器环境**

1. 操作系统：**win7及以上**
2. 浏览器: **Chrome最新版**
3. Python编辑器：**PyCharm**
4. 通用编辑器：**VSCode**

>官方下载机器环境软件版本地址：<https://cloud.tsinghua.edu.cn/d/a3db8d5efcf042a98055/>

**<span style="color:red;"> 第一次考试重要提示</span>**  

1. **考点机器**里面的Python编辑软件**<span style="color:red;">PyCharm</span>**,是考试的**<span style="color:red;">必备工具</span>**，考试过程中使用**PyCharm**编辑器编写代码，<span style="color:red;">不算作弊的</span>。  
2. GSEP 编程题答题界面不带**编译,提示**等功能，不能提示代码错误，所以建议考生在**<span style="color:red;">PyCharm中编写代码，然后复制到考试界面</span>**。

### 二、**GESP 考试代码题评测环境**

1. Docker Image：Ubuntu 24.04
2. Linux Kernel：5.15.0-107-generic
3. Python：Python 3.12.3（不包含 numpy 等第三方库）

### 三 **GESP Python考试界面介绍

#### 3.1 **GESP Python登录界面

1. 选择Python编程考试入口 还是图形化编程考试入口


2. 选择语言[**python**],[**考试等级**],[**考点**]


3. 输入考生的准考证号,密码**身份证号后六位**，如最后一位X，输入**大写X**


#### 3.2 **GESP Python答题主界面

主界面上面是三个Tab导航栏，分别是**题目列表**、**提交状态**、**提前交卷**， 默认**题目列表**

1. **题目列表**：


>点击对应的相应题目，进入答题界面

* CCF GESP 2024年9月认证 Python 1级 选择题
* CCF GESP 2024年9月认证 Python 1级 判断题
* CCF GESP 2024年9月认证 Python 1级 编程题1
* CCF GESP 2024年9月认证 Python 1级 编程题2

2. **提交状态**：
  显示考试的提交答案的记录列表。


3. **提前交卷**：
显示当前考试的【选择题】【判断题】【编程题】 提交情况。

交卷后将自动退出考试系统，不可再登录考试系统作答和提交。
请务必确认所有题目均已提交后再点击交卷。  
考试开始一小时内不允许提前交卷。  

点击**红色按钮**可以提前交卷。

#### 3.3 **选择题答题界面

答题界面上面是题目的题干，下面是四个选项，选择正确的选项。  
点击**提交测评**按钮，提交答案。

#### 3.4 **判断题答题界面

答题界面上面是题目的题干，下面是两个选项，选择正确的选项。
点击**提交测评**按钮，提交答案。

#### 3.5 **编程题答题界面

答题界面上面是题目的题干，下面是代码编辑框，编写代码。
>编程题答题界面没有**编译功能**，不能提示提交代码是否可以编译通过并运行。 需要考生自行在PyCharm中编写代码，然后复制到考试界面。
**上传代码的三种方式**：

1. 在PyCharm中编写代码，copy 代码到考试界面的代码编辑框中。
2. 在PyCharm中编写代码，保存为.py文件，点击上传文件按钮，选择文件上传。
3. 直接缩小答题的web界面，将py文件拖拽到答题界面。

点击**提交测评**按钮，提交答案。