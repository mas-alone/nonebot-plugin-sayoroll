import re
import random
import unicodedata
import string

from nonebot import on_command, require, on_regex
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
    ),
)


roll = on_command(
    'roll',
    priority=2,
    block=True
)


def normalize_str(s):
    return unicodedata.normalize('NFKC', s)


blocked_words = ["打胶"]
roll_suffix = on_regex(r'[!！/]roll.*概率$', priority=1, block=True)


@roll_suffix.handle()
async def _(args: Message = CommandArg()):
    user_input = args.extract_plain_text().replace('我', '你').replace('!roll', '').replace('！roll', '').replace('/roll', '')
    blocked = [word for word in blocked_words if word in args]
    if blocked:
        await UniMessage.text('[{}] 为屏蔽词'.format('] ['.join(blocked))).send(reply_to=True)
        return
    probability = random.uniform(0.01, 100.00)
    msg = '{}为：{:.2f}%'.format(user_input, probability)
    await UniMessage.text(msg).send(reply_to=True)


@roll.handle()
async def _(args: Message = CommandArg()):
    user_input = args.extract_plain_text().strip()
    if user_input.endswith('概率'):
        return
    args = args.extract_plain_text().strip()
    blocked = [word for word in blocked_words if word in args]
    if blocked:
        await UniMessage.text('[{}] 为屏蔽词'.format('] ['.join(blocked))).send(reply_to=True)
        return
    if not args:
        msg = '{}'.format(random.randint(0, 100))
    elif args.isdigit():
        num = int(args)
        if num > 99999:
            msg = '数字太大了，你真的需要这么大的随机数吗？'
        else:
            msg = '{}'.format(random.randint(0, num))
    elif re.search(r'([\u4e00-\u9fff])[不没].*?\1(.*?)', args):
        result = re.search(r'([\u4e00-\u9fff])[不没].*?\1(.*?)', args)
        options = [result.group()[:1], result.group()[1:]]
        msg = '我觉得' + args[:result.span()[0]].replace('我', 'temp').replace('temp', '你') + random.choice(
            options) + args[result.span()[1]:]
    elif re.search(r'(.+)还是\1', args):
        msg = '总共就2个参数..还都相同..怎么roll都一样啊'
    elif re.search(r'(.+)还是(.+)', args):
        options = re.split(r'还是', args)
        msg = '当然是{}咯'.format(random.choice(options))
    else:
        args = normalize_str(args)
        args_without_punctuation = args.translate(str.maketrans('', '', string.punctuation))
        if len(args_without_punctuation.split(' ')) == 1:
            msg = '未匹配到参数！'
        elif len(set(args_without_punctuation.split(' '))) == 1:
            msg = '总共就{}个参数..还都相同..怎么roll都一样啊'.format(len(args_without_punctuation.split(' ')))
        elif any(args_without_punctuation.split(' ').count(x) >= 2 for x in set(args_without_punctuation.split(' '))):
            duplicate_options = [x for x in set(args_without_punctuation.split(' ')) if
                                 args_without_punctuation.split(' ').count(x) >= 2]
            msg = '[{}] 出现次数过多,想增大概率是吧'.format(','.join(duplicate_options))
        else:
            options = [x for x in args.split(' ') if x.strip()]
            if len(options) > 1:
                msg = '当然是{}咯'.format(random.choice(options))
            else:
                msg = '未匹配到参数！'
    await UniMessage.text(msg).send(reply_to=True)
