import discord

print("Welcome!")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="Sending Nuggets"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Chickennugget'):
        await message.channel.send('C h i c k e n n u g g e t')
        await message.channel.send('https://cdn.discordapp.com/emojis/833678092282101780.png?v=1')
        print("Nuggets sent!")

    if message.content.startswith('Kfc'):
        await message.channel.send('KFC ist lecker!')

client.run('Your token here')
