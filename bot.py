import asyncio
import random
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('上線')
    status_w = discord.Status.idle
    activity_w = discord.Activity(type = discord.ActivityType.watching, name="")

    await client.change_presence(status = status_w, activity = activity_w)


@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return
    if message.content.startswith("[say"):
      tmp = message.content.split(' ',1)
      print(tmp)
      if len(tmp) == 1:
        async with message.channel.typing():
          type_time = random.uniform(0.5, 0.5)
          await asyncio.sleep(type_time)
          await message.channel.send(f"{message.author.mention} 蛤你要我說什麼")

      else:
        async with message.channel.typing():
          type_time = random.uniform(0.5, 2.5)
          await asyncio.sleep(type_time)
          msgone = await message.channel.send(f"{tmp[1]}")
        async with message.channel.typing():
          type_time = random.uniform(0.8, 0.8)
          await asyncio.sleep(type_time)
          msgtwo = await message.channel.send(f"{message.author.mention} 逼我說的")
          await asyncio.sleep(0.5)
          await msgtwo.delete()
          await asyncio.sleep(0.5)
          await msgone.delete()
        async with message.channel.typing():
          type_time = random.uniform(0.5, 0.5)
          await asyncio.sleep(type_time)
          await message.channel.send(f"啊哈哈沒事")


client.run('OTc5MDQ5ODg0NjcxOTQ2ODEy.Gfd4HC.5a8jZZ3NMGd_Gtc82GpwcPvusRW0L-OCGlGHr0')
