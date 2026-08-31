# 常用命令词汇表

本文件集中记录课程中反复出现的命令、符号、概念和目录约定；不按学习日期划分。每遇到一个新词，就补充它的“作用、使用方式和目标”。

## 终端与项目目录

| 词汇 / 命令 | 含义 | 示例 | 目标 |
| --- | --- | --- | --- |
| 终端（Terminal） | 用文字向操作系统发出命令的程序。Windows 上本课程使用 PowerShell。 | 在 VS Code 中打开“终端”面板 | 创建文件、进入目录、运行 Python 程序。 |
| `mkdir` | `make directory` 的缩写：创建文件夹。 | `mkdir src` | 为项目建立有组织的目录。 |
| `src` | `source` 的缩写：通常用来存放源代码的文件夹名称。它不是一条命令。 | `src/hello.py` | 让程序代码与笔记、资料等其他文件分开保存。 |
| `.` | 代表“当前目录”（终端此刻所在的文件夹）。 | `code .` | 告诉命令对当前课程项目执行操作。 |
| `code` | 启动 Visual Studio Code 的终端命令。 | `code .` | 用 VS Code 打开当前项目文件夹。 |
| `dir` | 显示当前目录里的文件和文件夹。 | `dir` | 确认文件或目录是否已经创建。 |
| `cd` | `change directory` 的缩写：进入或切换文件夹。 | `cd src` | 改变终端的工作位置。 |
| `New-Item` | PowerShell 的“动词-名词”命令：创建一个新对象。 | `New-Item hello.py -ItemType File` | 创建文件或文件夹。 |
| `-ItemType` | 为 `New-Item` 指定要创建的对象类型的参数。 | `-ItemType File` | 明确告诉 PowerShell 创建文件而非文件夹。 |
| `File` | 文件类型；与目录（`Directory`）不同。 | `New-Item hello.py -ItemType File` | 创建空的 Python 代码文件。 |
| PowerShell 的动词-名词形式 | PowerShell 常以 `动词-名词` 为命令命名，便于从名称看出动作和对象。 | `New-Item` | 理解并发现 PowerShell 命令。 |

## `dir` 输出中的列

| 名称 | 含义 | 如何阅读 |
| --- | --- | --- |
| `Mode` | 文件或文件夹的属性标记。 | 用来快速分辨条目的类别和某些属性。 |
| `d` | `directory` 的缩写：这是一个文件夹。 | `d----- src` 表示 `src` 是文件夹。 |
| `a` | `archive`（存档）属性：Windows 用它标记该文件自上次备份后可能有变化。 | `-a---- README.md` 仍然就是普通文件；日常学习中通常无需处理这个标记。 |
| `-` | 这一位置没有对应属性。 | 它不是减号命令，只表示该属性未设置。 |
| `LastWriteTime` | 最后修改时间。 | 用来判断文件最近何时被修改。 |
| `Length` | 文件大小，单位是字节（byte）。 | 文件夹通常不在此列显示大小。 |
| `Name` | 文件或文件夹名称。 | 例如 `src`、`README.md`。 |

## 阅读命令的小方法

把一条命令拆成两部分理解：**动词**和**对象/参数**。例如 `mkdir src` 中，`mkdir` 是“创建文件夹”，`src` 是要创建的文件夹名；`code .` 中，`code` 是“打开 VS Code”，`.` 是“当前文件夹”。

## VS Code

| 词汇 | 含义 | 目标 |
| --- | --- | --- |
| VS Code | 用于编辑代码的开发工具。 | 查看项目文件、编辑代码、运行和调试程序。 |
| Explorer（资源管理器） | VS Code 左侧显示项目文件和文件夹的面板。 | 打开和管理项目文件。 |
| 集成终端 | VS Code 底部内置的 PowerShell 命令行。 | 不离开编辑器即可运行程序。 |
| `Ctrl + S` | 保存当前文件。 | 让终端运行最新代码。 |
| ``Ctrl + ` `` | 显示或隐藏 VS Code 的集成终端。 | 快速运行命令。 |
| `U` / Untracked | Git 已发现但尚未提交的新文件标记。 | 提醒新文件需要在合适时提交。 |

## Python 第一个程序

| 词汇 / 语法 | 含义 | 示例 |
| --- | --- | --- |
| `.py` | Python 源代码文件的扩展名。 | `hello.py` |
| `python 文件路径` | 调用 Python 解释器执行指定代码文件。 | `python src/hello.py` |
| `input()` | 显示提示、暂停等待用户输入，并返回输入的文字。 | `name = input("你叫什么名字？")` |
| `print()` | 将内容输出到终端。 | `print("你好")` |
| 变量 | 给一个值取的名称，方便后续使用。 | `name` |
| `=` | 赋值：把右侧结果保存到左侧变量。 | `name = input(...)` |
| 字符串 | 用英文直引号包住的一段文字。 | `"你好"` |
| `f-string` | `formatted string`（格式化字符串）的简称；可插入变量或表达式。 | `f"你好，{name}！"` |
| `{name}` | 在 f-string 中插入变量 `name` 当前保存的值。 | `f"你好，{name}！"` |
| `SyntaxError` | Python 发现代码写法不符合语法规则。 | 缺少结尾引号时出现。 |
| `unterminated string literal` | 字符串没有结束，通常是缺少匹配的英文引号。 | `print("文字)` |
