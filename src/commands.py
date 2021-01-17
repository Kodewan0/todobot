import discord
from discord.ext import commands
from main_config import *

client = commands.Bot(command_prefix)
client.remove_command('help')

@client.event
async def on_ready():
    game = discord.Game(GAME)
    if STATUS == "idle":
        await client.change_presence(status=discord.Status.idle, activity=game)
        print('Bot is ready.')
    elif STATUS == 'online':
        await client.change_presence(status=discord.Status.online, activity=game)
        print('Bot is ready.')

@client.command(name='Обязательно')
async def suka(ctx, *args):
    author = ctx.message.author
    output = ''
    a = 0

    for word in args:
        output += word
        output += ' '
    if a == 0:
        await ctx.message.delete()
        embed = discord.Embed(
            title='{}'.format(output),
            descriptoin='This is a description',
            colour=discord.Colour.red()
        )
        channel = client.get_channel(788898442688069692)
        a = 1
        embed.set_author(name='Обязательно:',
                         icon_url='https://pngimg.com/uploads/exclamation_mark/exclamation_mark_PNG35.png')
        embed.add_field(name='Отправил:', value=author, inline=False)

        await channel.send(embed=embed)
    else:
        print("error")


@client.command(name='Желательно')
async def suka(ctx, *args):
    author = ctx.message.author
    output = ''
    a = 0

    for word in args:
        output += word
        output += ' '
    if a == 0:
        await ctx.message.delete()
        embed = discord.Embed(
            title='{}'.format(output),
            descriptoin='This is a description',
            colour=discord.Colour.orange()
        )
        channel = client.get_channel(788898442688069692)
        a = 1
        embed.set_author(name='Желательно:')

        embed.add_field(name='Отправил:', value=author, inline=False)

        await channel.send(embed=embed)
    else:
        print("error")


@client.command(name='советую')
async def suka(ctx, *args):
    author = ctx.message.author
    output = ''
    a = 0

    for word in args:
        output += word
        output += ' '
    if a == 0:
        await ctx.message.delete()
        embed = discord.Embed(
            title='{}'.format(output),
            descriptoin='This is a description',
            colour=discord.Colour.purple()
        )
        channel = client.get_channel(788898442688069692)
        a = 1
        embed.set_author(name='Совет:')

        embed.add_field(name='Советует:', value=author, inline=False)

        await channel.send(embed=embed)
    else:
        print("error")

client.run(TOKEN)