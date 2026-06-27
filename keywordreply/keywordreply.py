import discord
from redbot.core import commands


class KeywordReply(commands.Cog):
    """Reply when specific words appear in selected channels."""

    def __init__(self):
        self.channel_keywords = {
            123456789012345678: {
                "hello": "Hi there!",
                "redbot": "Redbot is online.",
            },
            987654321098765432: {
                "ping": "Pong!",
                "bot": "I am here.",
            },
        }

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.guild or message.author.bot:
            return

        triggers = self.channel_keywords.get(message.channel.id)
        if not triggers:
            return

        content = message.content.lower()

        for keyword, response in triggers.items():
            if keyword in content:
                await message.reply(response, mention_author=False)
                break


def setup(bot):
    bot.add_cog(KeywordReply())
