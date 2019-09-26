from discord.ext import commands
import re


def setup(bot):
    bot.add_cog(IdeasCog(bot))


class IdeasCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def newtrade(self, context, url=None):
        if url is None:
            await context.send(f'Looks like you forgot the idea link after the command!')
        elif not re.match(r"https://www\.tradingview\.com/x/.*", url):
            await context.send(f'Sorry, that does not look like a tradingview screenshot link! Only those are '
                               f'supported at the moment')
        else:
            await context.message.delete()
            ideas_channel = self.bot.get_channel(self.bot.config['ideas_channel'])
            new_message = await ideas_channel.send(f'New trade idea from {context.message.author.mention}: {url}')
            await new_message.add_reaction('\N{THUMBS UP SIGN}')
            await new_message.add_reaction('\N{THUMBS DOWN SIGN}')
