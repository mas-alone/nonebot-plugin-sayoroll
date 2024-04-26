import re
import random
import difflib
from typing import List
import unicodedata
import string
import json
from pathlib import Path

from nonebot import on_command, require, on_endswith
from nonebot.internal.adapter import Message
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require('nonebot_plugin_alconna')
from nonebot_plugin_alconna import UniMessage

__plugin_meta__ = PluginMetadata(
    name='sayoroll',
    type='application',
    homepage='https://github.com/mas-alone/nonebot-plugin-sayoroll',
    description='随机数字或随机事件',
    usage='roll[数字] / 事件1 事件2 .../ xxx要不要xxx/ xxx还是xxx',
    supported_adapters=inherit_supported_adapters(
        "nonebot_plugin_alconna"
    )
)

roll = on_command(
    'roll',
    priority=2,
    block=True
)

roll_suffix = on_endswith(("概率"))


def normalize_str(s):
    return unicodedata.normalize('NFKC', s)


def get_blocked_words() -> List:
    words_path = Path(__file__).parent / 'words.json'
    if not words_path.exists():
        with open(words_path.absolute(), 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False)
        return []
    else:
        with open(words_path.absolute(), 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data


@roll_suffix.handle()
async def _(args: Message = CommandArg()):
    user_input = args.extract_plain_text()
    user_input = user_input.replace('我', '你')
    blocked = re.findall('|'.join(get_blocked_words()), user_input, re.IGNORECASE)
    if len(blocked) > 0:
        await UniMessage.text('[{}] 为屏蔽词'.format('] ['.join(blocked))).send(reply_to=True)
        return
    probability = random.uniform(0.01, 100.00)
    msg = '{}为：{:.2f}%'.format(user_input, probability)
    await UniMessage.text(msg).send(reply_to=True)


@roll.handle()
async def _(args: Message = CommandArg()):
    user_input = args.extract_plain_text().strip()
    args = args.extract_plain_text().strip()

    blocked = re.findall('|'.join(get_blocked_words()), user_input, re.IGNORECASE)
    if len(blocked) > 0:
        await UniMessage.text('[{}] 为屏蔽词'.format('] ['.join(blocked))).send(reply_to=True)
        return
    if not args:
        msg = '{}'.format(random.randint(1, 100))
    elif args.isdigit():
        num = int(args)
        if num > 99999:
            msg = '数字太大了，你真的需要这么大的随机数吗？'
        else:
            msg = '{}'.format(random.randint(1, num))
    elif re.search(r'([\u4e00-\u9fff])[不没].*?\1(.*?)', args):
        result = re.search(r'([\u4e00-\u9fff])[不没].*?\1(.*?)', args)
        options = [result.group()[:1], result.group()[1:]]
        first_params = args[:result.span()[0]].replace('我', 'temp').replace('temp', '你')
        second_params = args[result.span()[1]:].replace('我', 'temp').replace('temp', '你')
        similarity = difflib.SequenceMatcher(None, first_params.lower(), second_params.lower()).ratio()
        if similarity > 0.8:
            msg = '总共就{}个参数..还这么相似..怎么roll都一样啊'.format(len(options))
        else:
            msg = '我觉得'
            msg += first_params
            msg += random.choice(options)
            msg += second_params
    elif re.search(r'(.+)还是(.+)', args):
        options = re.split(r'还是', args)
        similarity = difflib.SequenceMatcher(None, options[0].lower(), options[1].lower()).ratio()
        if similarity > 0.8:
            msg = '总共就2个参数..还这么相似..怎么roll都一样啊'
        else:
            msg = '当然是{}咯'.format(random.choice(options))
            msg = msg.replace('我', 'temp').replace('temp', '你')
    else:
        args = normalize_str(args)
        args_without_punctuation = args.translate(str.maketrans('', '', string.punctuation))
        if len(args_without_punctuation.split(' ')) == 1:
            msg = '未匹配到参数！'
        else:
            options = [x for x in args.split(' ') if x.strip()]
            if len(options) > 1:
                similarities = [difflib.SequenceMatcher(None, option1.lower(), option2.lower()).ratio() for i, option1 in enumerate(options) for option2 in options[i+1:]]
                if any(similarity > 0.8 for similarity in similarities):
                    msg = '总共就{}个参数..还这么相似..怎么roll都一样啊'.format(len(options))
                else:
                    msg = '当然是{}咯'.format(random.choice(options))
            else:
                msg = '未匹配到参数！'
    await UniMessage.text(msg).send(reply_to=True)
