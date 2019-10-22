# Help command that uses discord's embed feature
# Load this file in your cogs

import discord
from discord.ext import commands

from descriptions import bot_title, bot_description

class Help(commands.Cog):
    """ Help commands """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help',
        description='Help command',
        aliases=['-h'],
        case_insensitive=True)
    async def help_command(self, ctx, *commands : str):
        """ Shows this message """
        bot = ctx.bot
        destination = ctx.message.author if bot.pm_help else ctx.message.channel
        embed = discord.Embed(title=bot_title, description=bot_description)

        def repl(obj):
            return _mentions_transforms.get(obj.group(0), '')

        # Help by itself just lists our own commands.
        # if len(commands) == 0:
            # pages = bot.formatter.format_help_for(ctx, bot)
        # elif len(commands) == 1:
            # try to see if it is a cog name
            # name = _mention_pattern.sub(repl, commands[0])
            # command = None
            # if name in bot.cogs:
                # command = bot.cogs[name]
            # else:
            #     command = bot.commands.get(name)
            #     if command is None:
            #         yield from bot.send_message(destination, bot.command_not_found.format(name))
            #         return

            # pages = bot.formatter.format_help_for(ctx, command)
        # else:
            # name = _mention_pattern.sub(repl, commands[0])
            # command = bot.commands.get(name)
            # if command is None:
                # yield from bot.send_message(destination, bot.command_not_found.format(name))
                # return

            # for key in commands[1:]:
            #     try:
            #         key = _mention_pattern.sub(repl, key)
            #         command = command.commands.get(key)
            #         if command is None:
            #             yield from bot.send_message(destination, bot.command_not_found.format(key))
            #             return
            #     except AttributeError:
            #         yield from bot.send_message(destination, bot.command_has_no_subcommands.format(command, key))
            #         return

            # pages = bot.formatter.format_help_for(ctx, command)

        # if bot.pm_help is None:
        #     characters = sum(map(lambda l: len(l), pages))
        #     # modify destination based on length of pages.
        #     if characters > 1000:
        #         destination = ctx.message.author

        # for page in pages:
        #     yield from bot.send_message(destination, page)
        
        await ctx.send(embed=embed)
        return

# Cog setup
def setup(bot):
    bot.add_cog(Help(bot))