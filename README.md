<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-sayoroll

_✨ NoneBot 高仿小夜roll功能 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/mas-alone/nonebot-plugin-sayoroll.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-sayoroll">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-sayoroll.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 介绍

高仿以前小夜bot的roll功能

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
`-roll`

直接roll会在0-100之间随机一个数字并返回(类似osu的roll)
![1](https://www.showdoc.com.cn/server/api/attachment/visitFile?sign=f2c89a1568a512a44ee55e08d1583ed5&file=file.png)


`-roll [数字]`

带指定的数字的话则会从0到这个数字之间随机roll一个数字
![2](https://www.showdoc.com.cn/server/api/attachment/visitFile?sign=c983dba0d1f5ebc93a9bb0f47a3d733c&file=file.png)


`-roll [文字]`

例如 **-roll 你是不是耳聋**
bot会在 **你是耳聋** ，和 **你不是耳聋** 之间随机一个并返回。

相同道理还有(有没有、去不去、上不上等这种 **x不x** 的规则)
![3](https://www.showdoc.com.cn/server/api/attachment/visitFile?sign=48242d1ec881c0127197c394ed1c5461&file=file.png)


`-roll [参数] [参数] ...`

例如 **-roll 吃饭 睡觉 打游戏 运动 点蚊香**
bot会在 **吃饭 睡觉 打游戏 运动 点蚊香**之间随机一个并返回。

可以是无限多的词
![4](https://www.showdoc.com.cn/server/api/attachment/visitFile?sign=0f8d184f4375e19ef9b7f83f356482ae&file=file.png)
