<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-sayoroll

_✨ NoneBot 随机选择(roll)插件 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/mas-alone/nonebot-plugin-sayoroll.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-sayoroll">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-sayoroll.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 介绍

不知道怎么选择? 让bot帮你决定吧！ ^ ^

(高仿以前小夜bot的roll功能)

## 💿 安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-sayoroll

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-sayoroll
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-sayoroll
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-sayoroll
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-sayoroll
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_sayoroll"]

</details>

## 🎉 使用
### 指令表
`/roll`<br>
直接roll会在0-100之间随机一个数字并返回(类似osu的roll)<br><br>
`/roll [数字]`<br>
带指定的数字的话则会从0到这个数字之间随机roll一个数字<br><br>
`/roll [x不x/x没x]`<br>
例如 **/roll 我是不是耳聋** <br>
bot会在 **我觉得你不是耳聋** 和 **我觉得你是耳聋** 之间随机一个并返回。<br><br>
`/roll [xxx还是xxx] ...`<br>
例如 **/roll 今晚刷pp还是摆烂** <br>
bot会在 **当然是今晚刷pp咯** 和 **当然是摆烂咯** 之间随机一个并返回。只允许两个词<br><br>
`/roll [参数] [参数] ...`<br>
例如 **/roll 吃饭 睡觉 打游戏 运动 点蚊香**<br>
bot会在 **吃饭 睡觉 打游戏 运动 点蚊香**之间随机一个并返回。<br><br>
可以是无限多的词<br>
