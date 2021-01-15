import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from datetime import datetime

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command(name='총기')
async def _myinfo(ctx):
  await ctx.send("```구매자의 고유번호를 입력하세요.```")
  msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)
  await ctx.send("```구매자의 닉네임을 입력하세요.```")
  msg2 = await client.wait_for('message', check=lambda message: message.author == ctx.author)
  await ctx.send("```cs\n판매한 총기종류를 입력하세요.\n(ex ak 1정 , smg 1정)```")
  msg3 = await client.wait_for('message', check=lambda message: message.author == ctx.author)
  await ctx.send("```cs\n판매한 총알개수를 입력하세요.\n(ex ak 1000발 , smg 1000발)```")
  msg4 = await client.wait_for('message', check=lambda message: message.author == ctx.author)
  await ctx.send("```총기공장 장부 업로드 완료. - made by 정인```")
  channel = client.get_channel(799606539241259018)
  user_name = ctx.message.author.display_name
  await channel.send("```cs\n구매자 고유번호 : " + msg.content + "\n구매자 닉네임 : " + msg2.content + "\n총기종류 : " + msg3.content + "\n총알개수 : " + msg4.content + "\n\n담당 조직원 - " + user_name + "\n```")

client.run('Nzk5NTUxNDYzNjA0NjE3MjI2.YAFOUw.iogbsAFwEMs_-XcBhpiBBcapjzE')