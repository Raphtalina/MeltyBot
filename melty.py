import discord
import os

class Bot(discord.Client):
    async def on_ready(self):
        print('{0.user} olarak giriş yapıldı!'.format(self))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.channel.id == 670995249207836690:
            if message.content.startswith(str(os.environ.get('PASSWORD'))):
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

        if message.channel.id == 672587798783721522:
            if message.content.startswith('.lolhentai'):
                title = message.content.split()[1]
                source = message.content.split()[2]
                artist = message.content.split()[3]
                test = message.content.split()[4]
                e = discord.Embed(color=0x662d4b)
                if test == '1':
                    e.add_field(name='Champion', value=title)
                elif test == '2':
                    e.add_field(name='Champions', value=', '.join(list(title.split(','))))
                e.add_field(name='Artist', value=artist)
                e.set_image(url=source)
                await message.channel.send(embed=e)

if __name__ == '__main__':
    bot = Bot()
    bot.run(str(os.environ.get('BOT_TOKEN')))
