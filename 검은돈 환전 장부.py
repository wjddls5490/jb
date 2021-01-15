import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from datetime import datetime

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command(name='검은돈')
async def _myinfo(ctx):
  await ctx.send("```환전자의 고유번호를 입력하세요.```")
  msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)
  await ctx.send("```환전자의 닉네임을 입력하세요.```")
  msg2 = await client.wait_for('message', check=lambda message: message.author == ctx.author)
  await ctx.send("```cs\n환전한 금액을 입력하세요.\n```")
  msg3 = await client.wait_for('message', check=lambda message: message.author == ctx.author)
  await ctx.send("```검은돈 환전 장부 업로드 완료. - made by 정인```")
  channel = client.get_channel(799612809989193798)
  user_name = ctx.message.author.display_name
  await channel.send("```cs\n환전자 고유번호 : " + msg.content + "\n환전자 닉네임 : " + msg2.content + "\n환전금액 : " + msg3.content + "\n\n담당 조직원 - " + user_name + "\n```")

client.run('Nzk5NTUxNDYzNjA0NjE3MjI2.YAFOUw.iogbsAFwEMs_-XcBhpiBBcapjzE')