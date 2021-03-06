# Embed_help

A rewritten help command for the [discord.py](https://discordpy.readthedocs.io/en/latest/) python library

* [Usage](#usage)
  * [How to use if your bot already has cogs](#how-to-use-if-your-bot-already-has-cogs)
  * [How to add to your bot if it doesn't have cogs](#how-to-add-to-your-bot-if-it-doesnt-have-cogs)
  * [Settings](#settings)
* [Screenshots](#screenshots)

## Usage

### How to use if your bot already has cogs
Clone into your cogs folder
```
git clone https://github.com/zedchance/embed_help.git
```

Add `cogs.embed_help.help` to your cogs array and disable the built in help message like this:
```py
bot.remove_command('help')
cogs = [ ..., 'cogs.embed_help.help']
```

### How to add to your bot if it doesn't have cogs
Create a directory called `cogs` in your project and clone
```
git clone https://github.com/zedchance/embed_help.git
```

Add the command to disable the built in help message and create a list called `cogs` like this:
```py
bot.remove_command('help')
cogs = ['cogs.embed_help.help']
```

Then in your `on_ready` method load the cogs:
```py
@bot.event
async def on_ready():
    # Your existing stuff
    for cog in cogs:
        bot.load_extension(cog)
```

### Settings
There are 4 fields you should fill out in the `help.py` file
```py
prefix = '!'
bot_title = 'Bot title'
bot_description = ''
bottom_info = ''
```
At the very least you should fill out the `prefix` field (and probably the `bot_title`).
`bot_description` adds text beneath the title and `bottom_info` adds a field at the end of the
help command (useful instead of a footer because you can add markdown formatting).

## Screenshots

Here are some examples of what the help messages look like before and after using [!blue](https://github.com/zedchance/blues_bot.py) bot.

Before | After
--- | ---
![before3](screenshots/before3.png) | ![after3](screenshots/after3.png)
![before2](screenshots/before2.png) | ![after2](screenshots/after2.png)
![before1](screenshots/before1.png) | ![after1](screenshots/after1.png)
