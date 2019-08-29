#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""c01_python简介.py"""
import handout
doc = handout.Handout('doc/c01_python简介', 'c01_python简介')
"""
# Python 简介

Python 由 `Guido van Rossum` 于1989年底发明，第一个公开发行版发行于1991年。

## Python 的特点

* 解释型脚本语言
* 交互式语言（REPL）
* 遵循 `GNU General Public License，GPL` 协议



"""

"""
## 第一个 hello world 程序
"""

print('hello, world!')

"""
## 关于脚本声明

`#!/usr/bin/python` 相当于写死了 python 路径。

`#!/usr/bin/env python` 会去环境设置寻找 python 目录，可以增强代码的可移植性，推荐这种写法。

"""

"""
domkn @ 2019-08-29
"""
doc.show()
