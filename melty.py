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

        if message.channel.id == 670998063220916234:
            if message.content.startswith('.upload'):
                title = message.content.split()[1].replace('-', ' ')
                source = message.content.split()[2]
                model = message.content.split()[3].replace('-', ' ')
                link = message.content.split()[4]
                e = discord.Embed(title=title)
                e.add_field(name='Model', value=f'[{model}]({link})')
                e.set_image(url=source)
                await message.channel.send(embed=e)

            if message.content.startswith('.r'):
                id = message.content.split()[1]
                msg = await message.channel.fetch_message(id)
                await msg.delete()

if __name__ == '__main__':
    bot = Bot()
    bot.run(str(os.environ.get('BOT_TOKEN')))
