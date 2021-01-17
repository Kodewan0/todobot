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


@client.command(name=RED_BUTTON)
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
        channel = client.get_channel(CHANNEL_ID)
        a = 1
        embed.set_author(name=RED_BUTTON,
                         icon_url='https://pngimg.com/uploads/exclamation_mark/exclamation_mark_PNG35.png')
        embed.add_field(name='Sent by:', value=author, inline=False)

        await channel.send(embed=embed)
    else:
        print("error")


@client.command(name=YELLOW_BUTTON)
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
        channel = client.get_channel(CHANNEL_ID)
        a = 1
        embed.set_author(name=YELLOW_BUTTON)

        embed.add_field(name='Sent by:', value=author, inline=False)

        await channel.send(embed=embed)
    else:
        print("error")


@client.command(name=PURPLE_BUTTON)
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
        channel = client.get_channel(CHANNEL_ID)
        a = 1
        embed.set_author(name=PURPLE_BUTTON)

        embed.add_field(name='Advice from:', value=author, inline=False)

        await channel.send(embed=embed)
    else:
        print("error")


client.run(TOKEN)
