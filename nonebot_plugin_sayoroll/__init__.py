import re
import random
import unicodedata
import string

from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.adapters.onebot.v11.event import MessageEvent
from nonebot.adapters.onebot.v11.message import Message, MessageSegment

__plugin_meta__ = PluginMetadata(
    name='sayoroll',
    type='application',
    homepage='https://github.com/mas-alone/nonebot-plugin-sayoroll',
    description='随机数字或随机事件',
    usage='roll[数字] / 事件1 事件2 .../ xxx要不要xxx/ xxx还是xxx',
    config={},
    extra={}
)


roll = on_command(
    'roll',
    priority=1,
    block=False
)


def normalize_str(s):
    return unicodedata.normalize('NFKC', s)

@roll.handle()
async def _(bot: Bot, event: MessageEvent, args: Message = CommandArg()):
    args = str(args).strip()

    if not args:
        msg = '你的数字是[{}]'.format(random.randint(0, 100))
        await roll.finish(
            message=MessageSegment.reply(event.message_id) + Message(msg)
        )

    elif args.isdigit():
        num = int(args)
        if num > 99999:
            msg = '数字太大了，你真的需要这么大的随机数吗？'
        else:
            msg = '你的数字是[{}]'.format(random.randint(0, num))
        await roll.finish(
            message=MessageSegment.reply(event.message_id) + Message(msg)
        )

    elif re.search(r'([\u4e00-\u9fff])([\u4e00-\u9fff])\1(.*?)', args):
        result = re.search(r'([\u4e00-\u9fff])([\u4e00-\u9fff])\1(.*?)', args)
        options = [result.group()[:1], result.group()[1:]]
        if args.startswith('你'):
            msg = args[:result.span()[0]].replace('我', 'temp').replace('你', '我').replace('temp', '你') + random.choice(options) + args[result.span()[1]:]
        else:
            msg = '我觉得' + args[:result.span()[0]].replace('我', 'temp').replace('你', '我').replace('temp', '你') + random.choice(options) + args[result.span()[1]:]
        await roll.finish(
            message=MessageSegment.reply(event.message_id) + Message(msg)
        )

    elif re.search(r'(\b.+?\b)还是\1', args):
        await roll.finish(
            message=MessageSegment.reply(event.message_id) + '总共就2个参数..还都相同..怎么roll都一样啊'
        )


    elif re.search(r'(.+)还是(.+)', args):
        result = re.search(r'(.+)还是(.+)', args)
        options = [result.group(1), result.group(2)]
        msg = '当然是' + random.choice(options) + '咯'
        await roll.finish(
            message=MessageSegment.reply(event.message_id) + Message(msg)
        )

    else:
        args = normalize_str(args)
        args_without_punctuation = args.translate(str.maketrans('', '', string.punctuation))
        
        if len(args_without_punctuation.split(' ')) == 1:
            await roll.finish(
                message=MessageSegment.reply(event.message_id) + '未匹配到参数！'
            )
            return

        if len(set(args_without_punctuation.split(' '))) == 1:
            msg = '总共就{}个参数..还都相同..怎么roll都一样啊'.format(len(args_without_punctuation.split(' ')))
            await roll.finish(
                message=MessageSegment.reply(event.message_id) + Message(msg)
            )

        if any(args_without_punctuation.split(' ').count(x) >= 2 for x in set(args_without_punctuation.split(' '))):
            duplicate_options = [x for x in set(args_without_punctuation.split(' ')) if args_without_punctuation.split(' ').count(x) >= 2]
            msg = '[{}] 参数出现次数过多,想增大概率是吧'.format(','.join(duplicate_options))
            await roll.finish(
                message=MessageSegment.reply(event.message_id) + Message(msg)
            )

        options = [x for x in args.split(' ') if x.strip()]
        
        if len(options) > 1:
            msg = '当然是{}咯'.format(random.choice(options))
            await roll.finish(
                message=MessageSegment.reply(event.message_id) + Message(msg)
            )

        else:
            await roll.finish(
                message=MessageSegment.reply(event.message_id) + '未匹配到参数！'
            )
