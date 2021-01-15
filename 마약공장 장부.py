import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from datetime import datetime

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command(name='마약')
async def _myinfo(ctx):
  await ctx.send("```공장 이용자의 고유번호를 입력하세요.```")
  msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)
  await ctx.send("```공장 이용자의 닉네임을 입력하세요.```")
  msg2 = await client.wait_for('message', check=lambda message: message.author == ctx.author)
  await ctx.send("```cs\n공장 이용 시작시간을 입력하세요.\n(ex 오후 01시 01분)```")
  msg3 = await client.wait_for('message', check=lambda message: message.author == ctx.author)
  await ctx.send("```cs\n공장 이용 종료시간을 입력하세요.\n(ex 오후 02시 01분)```")
  msg4 = await client.wait_for('message', check=lambda message: message.author == ctx.author)
  await ctx.send("```마약공장 장부 업로드 완료. - made by 정인```")
  channel = client.get_channel(799609734654197791)
  user_name = ctx.message.author.display_name
  await channel.send("```cs\n이용자 고유번호 : " + msg.content + "\n이용자 닉네임 : " + msg2.content + "\n이용 시작시간 : " + msg3.content + "\n이용 종료시간 : " + msg4.content + "\n\n담당 조직원 - " + user_name + "\n```")

client.run('Nzk5NTUxNDYzNjA0NjE3MjI2.YAFOUw.iogbsAFwEMs_-XcBhpiBBcapjzE')