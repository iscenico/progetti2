import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '$')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('Aspettando un comando: $comandi!'))
    print('{0.user} è on'.format(bot))

@bot.command()
async def clear(ctx, amount=2):
  await ctx.channel.purge(limit=amount)

@bot.command
async def ban(ctx, member=discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send('{0.user} bannato correttamente!')

@bot.command
async def kick(ctx, member=discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send('{0.user} kickato correttamente!')

@bot.command()
async def unban(ctx, *, member): 
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user

    if {user.name, user.discriminator} == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send('{0.user} è stato sbannato correttamente')
      return

@bot.command()
async def comandi(ctx):
    await ctx.send(embed=embed)
embed=discord.Embed(title="Ecco a te i comandi!", url="", description="Hai richiesto la lista dei comandi, eccoti accontentato!", color=discord.Color.blue())
embed.set_author(name="Moderator Bot", url="", icon_url="")
embed.set_thumbnail(url="")
embed.add_field(name="Per bannare i membri:", value="`$ban <membro> <motivo>`", inline=True) 
embed.add_field(name="Per espellere i membri:", value="`$kick <membro> <motivo>`", inline=False)
embed.add_field(name="Per cancellare un determinato numero di messaggi:", value="`$clear <messaggi>`", inline=False)
embed.add_field(name="Per sbannare un membro:", value="`$unban <membro#1234>`", inline=False)
embed.set_footer(text="By danio#7394")

bot.run('OTI4OTU1MDY2MzMxODQ4NzQ0.YdgS0g.I07SFDj7zn1qkY6tHQPIWwahEso')