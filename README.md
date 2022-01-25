# luogu-random-problem

## 功能

随机跳题，支持一次随机多个题目，以及指定题目的难度和题库来源（主题库，CF，AT，UVA，SP 等）。

如果是第一次使用，速度可能会比较慢，但经过几次使用就会很快。

## 用法

在命令行中输入 `python lg-rand.py --help` 即可得到关于用法的帮助。

**请不要随意改动生成的 `problems.json`。**

## 举例

`python lg-rand.py 1,1,4,5,1,4`：从所有题库中随机难度分别为红，红，绿，蓝，红，绿的六道题。

`python lg-rand.py 1,2,3 -c P,CF`：从主题库和 CF 题库中随机难度分别为红，橙，黄的三道题。

## 环境要求

Python 版本 >= 3.2，并安装了 requests，BeautifulSoup4，colorama 和 lxml。

## To-Do

- 支持动态地更新 `problems.json`；
- 支持在以往的月赛中随机选题；
- 为输出的题号添加颜色。
