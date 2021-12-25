from discord.ext import commands

class testcog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    def test(self, ctx):
        ctx.reply("ur mom")

def setup(bot):
    bot.add_cog(testcog(bot))