import discord
import os

class Bot(discord.Client):
    async def on_ready(self):
        print('{0.user} olarak giriş yapıldı!'.format(self))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('nomor1337'):
            if message.author.id == 595575056592011274:
                await message.author.add_roles(discord.utils.get(message.guild.roles, name='Raphtalina'))
            elif message.author.id == 469263959694770201:
                await message.author.add_roles(discord.utils.get(message.guild.roles, name='Raurora'))
            elif message.author.id == 378636649107816458:
                await message.author.add_roles(discord.utils.get(message.guild.roles, name='Cavamon'))
            await message.delete()
        else:
            if message.author.id == 595575056592011274:
                await message.author.remove_roles(discord.utils.get(message.guild.roles, name='Raphtalina'))
            elif message.author.id == 469263959694770201:
                await message.author.remove_roles(discord.utils.get(message.guild.roles, name='Raurora'))
            elif message.author.id == 378636649107816458:
                await message.author.remove_roles(discord.utils.get(message.guild.roles, name='Cavamon'))
            await message.delete()

if __name__ == '__main__':
    bot = Bot()
    bot.run(str(os.environ.get('BOT_TOKEN')))
