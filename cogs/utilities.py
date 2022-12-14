import discord
from discord import app_commands
from discord.ext import commands
import requests
import Paginator


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = "A bunch of useful utility commands!"
    
    @commands.command(description="Find your ping to SunShine!")
    async def ping(self, ctx):
        embed = discord.Embed(color=discord.Colour.yellow(), title="Ping", description=f':green_apple: Finding ping to bot...\n:alarm_clock: Your ping is {round(self.bot.latency*1000)} ms')
        await ctx.send(embed=embed)
    @app_commands.command(name="ping", description="Find your ping to SunShine!")
    async def pingSlash(self, interaction: discord.Interaction):
        embed = discord.Embed(color=discord.Colour.yellow(), title="Ping", description=f':green_apple: Finding ping to bot...\n:alarm_clock: Your ping is {round(self.bot.latency*1000)} ms')
        await interaction.response.send_message(embed=embed)
    
    @commands.command(description="Get a random quote from someone!")
    async def quote(self, ctx):
        json = requests.get("https://api.quotable.io/random").json()
        await ctx.send(f'"{json["content"]}" -{json["author"]}')
    @app_commands.command(name="quote", description="Get a random quote from someone!")
    async def quoteSlash(self, interaction: discord.Interaction):
        json = requests.get("https://api.quotable.io/random").json()
        await interaction.response.send_message(f'"{json["content"]}" -{json["author"]}')
    
    @commands.command(description="*Holy Music stops...*")
    async def summon(self, ctx, args: discord.Member = None):
        if args:
            await ctx.send(f'Summoning {args.mention}...')
            await ctx.send(f'{args.mention}')
            await ctx.send(f'{args.mention}')
            await ctx.send(f'{args.mention}')
            await ctx.send(f'{args.mention}')
            await ctx.send(f'{args.mention}')
        else:
            await ctx.reply("You need to mention a valid user!")
    @app_commands.command(name="summon", description="*Holy Music stops...*")
    @app_commands.describe(user='the member to summon')
    async def summonSlash(self, interaction: discord.Interaction, user: discord.Member):
        await interaction.response.send_message(f'Summoning {user.mention}...')
        await interaction.channel.send(f'{user.mention}')
        await interaction.channel.send(f'{user.mention}')
        await interaction.channel.send(f'{user.mention}')
        await interaction.channel.send(f'{user.mention}')
        await interaction.channel.send(f'{user.mention}')

    @commands.command(description="Shows my commands!")
    async def help(self, ctx):
        embeds = []
        for i in self.bot.cogs:
            cog = self.bot.get_cog(i)
            embed = discord.embeds.Embed(color=discord.Colour.yellow(), title=f'{i} Commands:', description="")
            for c in cog.get_commands():
                embed.description+=f'{c}: {c.description}\n'
            embeds.append(embed)
        await Paginator.Simple().start(ctx, pages=embeds)
    @app_commands.command(name="help", description="Shows my commands!")
    async def helpSlash(self, interaction: discord.Interaction):
        embeds = []
        for i in self.bot.cogs:
            cog = self.bot.get_cog(i)
            embed = discord.embeds.Embed(color=discord.Colour.yellow(), title=f'{i} Commands:', description="")
            for c in cog.get_commands():
                embed.description+=f'{c}: {c.description}\n'
            embeds.append(embed)
        await Paginator.Simple().start(interaction, pages=embeds)