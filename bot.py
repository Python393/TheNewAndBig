from discord.ext import commands
bot = commands.Bot(command_prefix='!')
bot.load_extension("cogs.testcog")
bot.run()