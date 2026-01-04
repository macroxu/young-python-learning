### 0 什么是Python UV
UV 是一个现代的 Python 包和环境管理器，旨在简化 Python 项目的依赖项管理和虚拟环境创建。它结合了包管理器（类似于 pip）和环境管理器（类似于 virtualenv 或 conda）的功能，提供了一种更高效、更用户友好的方式来处理 Python 项目中的依赖项和环境。

* UV的显著特点是其极快的速度和极低的资源占用。
* UV隔离每个项目的依赖项，确保不同项目之间不会发生冲突。
* 它使用现代的依赖项解析器，能够智能地解决依赖项冲突，并确保安装的包版本与项目需求兼容。
* UV还支持多种Python版本，允许用户轻松切换和管理不同的Python环境。


### 1 安装UV

1. **在macOS和Linux系统上，可以使用cURL在全系统范围内安装UV：**  

```bash
curl -LsSf https://astral.sh/uv/install.sh | sudo sh
```

**在macOS上，还可以直接通过brew安装：**

```bash
brew install uv
```


1. **Windows用户可以使用PowerShell安装UV：**  

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

3. **安装后验证是否安装成功**

```bash
uv --version
```


### 2 使用UV 初始化项目并管理依赖项 
1. **初始化UV项目**
```bash
uv init example-project --python "==3.11.4"
```

查看初始化的界面
``` bash
cd example-project
tree .

example-project
├── README.md
├── main.py
└── pyproject.toml
```

2. **向项目中添加初始依赖项**
UV 将环境创建和依赖项安装整合到一个命令中——uv add：  

```bash
explore-uv % uv add SciPy
Resolved 3 packages in 671ms
Prepared 1 package in 3m 03s
Installed 2 packages in 50ms
 + numpy==2.3.3
 + scipy==1.16.2

```

``首次运行add``命令时，UV会在当前工作目录中创建一个新的虚拟环境，并安装指定的依赖项。在后续运行中，UV将重用现有的虚拟环境，只安装或更新新请求的包，从而确保高效的依赖项管理。  

每个add命令都会执行的另一个重要过程是依赖项解析。UV使用现代的依赖项解析器，该解析器会分析整个依赖项图，以找到一组满足所有要求的兼容包版本。这有助于防止版本冲突，并确保环境的可复现性。解析器会考虑版本约束、Python版本兼容性以及特定平台要求等因素，以确定要安装的最佳包集合。  

UV 还会在每次执行 add 命令后更新 pyproject.toml 和 uv.lock 文件。 pyproject.toml 文件包含项目的元数据和依赖项列表，而 uv.lock 文件则锁定了确切的包版本，以确保在不同环境中安装时的一致性。

3. **向项目中移除初始依赖项**
UV 提供了一个方便的命令 uv remove，用于从项目中移除不再需要的依赖项。该命令不仅会卸载指定的包，还会更新项目的依赖项文件，以确保环境的整洁和一致性。 

```bash
uv remove requests      
Removed 1 package in 20ms
 - requests==2.31.0
```

### 3 使用UV 运行Python脚本
要直接运行Python脚本，你可以使用uv run命令，后跟你的脚本名称
```bash
uv run main.py
```
run命令确保脚本在UV为项目创建的虚拟环境中执行。

### 4 使用UV管理Python

1. **列出已安装的包**
由于系统通常已经安装了Python，因此UV默认情况下可以检测到这些已有的安装。例如，要列出UV在您的系统上检测到的所有Python版本，请运行以下命令：
```bash
uv python list --only-installed
```
该命令将显示所有已安装的包及其版本。

2. **修改项目中的Python版本**
* 修改项目中的pyproject.toml文件 的 project.requires-python 字段中 改成 需要的Python版本号
``` toml
[project]
name = "example-project"
version = "0.1.0"
requires-python = ">=3.10,<4.0"
```
* 同时将.python-version文件中的Python版本号改成 需要的Python版本号
* 运行 uv sync 命令 刷新当前的项目环境
``` bash
uv sync
```