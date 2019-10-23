# Help command that uses discord's embed feature
# Load this file in your cogs

import discord
from discord.ext import commands

bot_title = ''
bot_description = ''
footer = 'Use `!blue help [command]` or `!blue help [category]` for more information'

class Help(commands.Cog):
    """ Help commands """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help',
        description='Help command',
        case_insensitive=True)
    async def help_command(self, ctx, *commands : str):
        """ Shows this message """
        bot = ctx.bot
        embed = discord.Embed(title=bot_title, description=bot_description)

        def repl(obj):
            return _mentions_transforms.get(obj.group(0), '')
        
        def generate_usage(command_name):
            """ Generates a string of how to use a command """
            temp = f'!b '
            command = bot.get_command(command_name)
            # Aliases
            if len(command.aliases) == 0:
                temp += f'{command_name}'
            elif len(command.aliases) == 1:
                temp += f'[{command.name}|{command.aliases[0]}]'
            else:
                t = '|'.join(command.aliases)
                temp += f'[{command.name}|{t}]'
            # Parameters
            params = f' '
            for param in command.clean_params:
                print(param)
                params += f'<{command.clean_params[param]}> '
            temp += f'{params}'
            return temp

        # Help by itself just lists our own commands.
        if len(commands) == 0:
            for cog in bot.cogs:
                temp = ""
                for command in bot.get_cog(cog).get_commands():
                    if command.help is not None:
                        temp += f' `{command}` \0\0 {command.help}\n'
                    else:
                        temp += f'`{command}`\n'
                embed.add_field(name=f'**{cog}**', value=temp, inline=True)
            embed.add_field(name= "\0", value=footer, inline=False)
        elif len(commands) == 1:
            # try to see if it is a cog name
            name = commands[0]
            command = None
            
            if name in bot.cogs:
                cog = bot.get_cog(name)
                msg = ""
                for command in cog.get_commands():
                    if command.help is not None:
                        msg += f' `{command}` \0\0 {command.help}\n'
                    else:
                        msg += f'`{command}`\n'
                embed.add_field(name=name, value=msg, inline=False)
                msg = f'{cog.description}\n'
                embed.add_field(name="\0", value=msg, inline=False)
            else:
                command = bot.get_command(name)
                if command is not None:
                    embed.add_field(name=f'**{command}**', value=f'{command.description}```{generate_usage(name)}```', inline=False)
                else:
                    msg = ' '.join(commands)
                    embed.add_field(name="Not found", value=f'Command/category `{msg}` not found.')
        else:
            msg = ' '.join(commands)
            embed.add_field(name="Not found", value=f'Command/category `{msg}` not found.')
        
        await ctx.send(f'{ctx.author.mention}', embed=embed)
        return

# Cog setup
def setup(bot):
    bot.add_cog(Help(bot))