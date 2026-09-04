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

## Python 数据类型与运算

| 词汇 / 运算 | 含义 | 示例 |
| --- | --- | --- |
| `str` | 字符串：文字数据类型。 | `"125"`、`"你好"` |
| `int` | 整数数据类型；`int()` 也可把纯数字文字转换为整数。 | `int("125")` 得到 `125` |
| `float` | 小数数据类型；`float()` 可把带小数的数字文字转换为小数。 | `float("3.5")` 得到 `3.5` |
| `bool` | 布尔数据类型，只有 `True`（真）和 `False`（假）。 | `is_finished = True` |
| `+` | 加法。 | `2 + 3` 得到 `5` |
| `-` | 减法。 | `5 - 2` 得到 `3` |
| `*` | 乘法。 | `3.5 * 6 * 24` 得到 `504.0` |
| `/` | 普通除法，结果通常是小数。 | `5 / 2` 得到 `2.5` |
| `//` | 整除，只保留完整份数。 | `257 // 60` 得到 `4` |
| `%` | 取余数，得到整除后剩余的部分。 | `257 % 60` 得到 `17` |
| `#` | 注释的开始；其后的文字供人阅读，Python 不执行。 | `# 计算 24 周总时长` |

### 常用换算公式

```text
完整小时数 = 总分钟数 // 60
剩余分钟数 = 总分钟数 % 60
24 周理论总时长 = 每天学习小时数 × 每周学习天数（6）× 周数（24）
```

## Python 条件判断

| 词汇 / 语法 | 含义 | 示例 |
| --- | --- | --- |
| `if` | 当条件为真时，执行其缩进代码块。 | `if minutes == 0:` |
| `elif` | 前面的条件不成立时，继续检查这个条件。 | `elif minutes < target:` |
| `else` | 前面所有条件都不成立时执行。 | `else:` |
| 缩进 | 行首的 4 个空格；Python 用它表示哪些代码属于某个条件。 | `if` 下方的 `print(...)` |
| `==` | 比较左右两边是否相等。 | `minutes == 60` |
| `!=` | 比较左右两边是否不相等。 | `minutes != 0` |
| `<` / `>` | 小于 / 大于。 | `minutes < target` |
| `<=` / `>=` | 小于等于 / 大于等于。 | `minutes >= target` |
| `and` | 两个条件都为真时，整个条件才为真。 | `minutes > 0 and minutes < 60` |
| `or` | 两个条件至少一个为真时，整个条件为真。 | `minutes == 0 or minutes > 120` |
| `not` | 反转一个真/假结果。 | `not is_finished` |

### 判断顺序

`if / elif / else` 从上到下检查，遇到第一个为真的条件就停止。因此范围更窄、特殊的条件应优先写。例如 `minutes == 0` 必须写在 `minutes < target` 前面，否则 0 会先被归入“未达标”。

## Python 循环

| 词汇 / 语法 | 含义 | 示例 |
| --- | --- | --- |
| 循环 | 按规则重复执行一段代码。 | 连续列出 7 天的学习计划。 |
| `for` | 依次取得一组值，并对每个值执行循环体。 | `for day in range(1, 8):` |
| `range()` | 产生整数序列；结束值不包含在内。 | `range(1, 8)` 产生 1 到 7。 |
| `for day in ...` | `day` 是循环变量；每轮自动接收当前值。 | 首轮为 1，最后一轮为 7。 |
| `while` | 只要条件为 `True`，就持续执行循环体。 | `while day < 7:` |
| `day = day + 1` | 更新计数变量，让 `while` 条件最终变为假。 | 1 变 2，直到 7。 |
| 无限循环 | `while` 的条件永远为真时，循环不会结束。 | 忘记更新 `day` 时可能发生。 |
| `py` | Windows 的 Python 启动器；可运行 Python 文件。 | `py week_plan.py` |

### 循环中的累计

```text
累计值 = 累计值 + 本次值
```

例如 `total_minutes = total_minutes + daily_minutes` 每次循环都将当天计划加入总时长。循环内缩进的 `print()` 每轮执行一次；循环外未缩进的 `print()` 只在循环结束后执行一次。

## Python 列表与字典

| 词汇 / 语法 | 含义 | 示例 |
| --- | --- | --- |
| 列表（list） | 按顺序保存多个值的容器。 | `weekly_tasks = [任务1, 任务2]` |
| 字典（dict） | 使用“键: 值”描述一个对象的容器。 | `{"name": "学习 Python", "completed": True}` |
| 键（key） | 字典中用来标记一项数据的名称。 | `"estimated_minutes"` |
| 值（value） | 与键对应的实际数据。 | `60`、`False` |
| `字典["键"]` | 按键从字典中取出对应值。 | `task["name"]` |
| `列表[位置]` | 按位置从列表中取项目；第一个位置是 0。 | `weekly_tasks[0]` |
| `len()` | 返回容器中项目的数量。 | `len(prompt_tests)` 得到 `3` |
| `True` / `False` | 布尔值；常用于记录“是否完成”等状态。 | `"completed": False` |

## 常见括号与符号

| 写法 | 常见用途 | 示例 |
| --- | --- | --- |
| `()` | 调用函数；也可用于数学分组。 | `print("你好")`；`(2 + 3) * 4` |
| `[]` | 创建列表；或从列表、字典中取值。 | `["苹果", "香蕉"]`；`tasks[0]`；`task["name"]` |
| `{}` | 创建字典；或在 f-string 中插入变量/计算结果。 | `{"name": "任务"}`；`f"状态：{status}"` |
| `"..."` / `'...'` | 创建字符串（文字）；同一段字符串须使用匹配的引号。 | `"学习 Python"` |

### 容易混淆的嵌套写法

```python
print(f"{task['name']}：{task['estimated_minutes']} 分钟，{status}")
```

- 最外层 `print(...)` 的 `()`：调用输出功能。
- `f"..."`：一段可插入值的文字。
- `{...}`：计算并插入其中的结果。
- `task['name']`：从当前任务字典取出 `name` 对应的值；这里的 `[]` 是取值，不是创建列表。

### 列表与循环变量的层级

```python
for test in prompt_tests:
    score = test["score"]
```

- `prompt_tests` 是整个列表，不能直接用 `prompt_tests["score"]` 取值。
- `test` 是当前循环取出的一个字典，所以用 `test["score"]` 取分数。

## 列表追加与循环控制

| 词汇 / 语法 | 含义 | 示例 |
| --- | --- | --- |
| `.append()` | 列表的方法：将一个值添加到列表末尾，直接修改原列表。 | `records.append(record)` |
| `break` | 立刻结束当前循环，程序接着执行循环之后的代码。 | `if answer != "y": break` |
| `\n` | 字符串中的换行符；输出前可留出空行。 | `print("\n今天的学习记录：")` |
| 方法调用 | 用 `对象.方法(参数)` 调用对象自带的功能。 | `records.append(record)` |

## Git 基础工作流

| 命令 / 词汇 | 含义 | 示例 |
| --- | --- | --- |
| `git status` | 查看仓库、暂存区和工作区的当前状态。 | 查看未跟踪或未提交的文件。 |
| Untracked | Git 发现了文件，但尚未开始跟踪它。 | `learning_logger.py` 初建后。 |
| `git add 文件名` | 将文件放入暂存区，准备提交。 | `git add learning_logger.py` |
| Staged / Changes to be committed | 已暂存，下一次提交会包含这些改动。 | `new file: learning_logger.py` |
| `git commit -m "说明"` | 将暂存内容保存为一条本地版本历史，并附提交说明。 | `git commit -m "完成第一周学习记录器"` |
| `git push origin main` | 将本地 `main` 分支的新提交上传到远程仓库 `origin` 的 `main` 分支。 | 同步到 GitHub。 |
| `origin` | 本机给远程 GitHub 仓库起的默认别名。 | `https://github.com/Zarielanda/ai-apps-from-zero.git` |
| `main` | 当前仓库的主分支名称。 | `On branch main` |

### Git 提交流程

```text
文件修改 / 新建
  → git status（检查）
  → git add（暂存）
  → git commit（保存本地历史）
  → git push（公开同步到 GitHub）
```
