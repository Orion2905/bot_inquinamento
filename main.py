import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Come vengono smaltite le plastiche?'):
        await message.channel.send(f'Ciao! Io sono un bot{client.user}!')
    elif  message.content.startswith('$heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
        await message.channel.send("he" * count_heh)
    
        
client.run("MTE2NTk0OTQyMzIxMDIxMzM4Ng.Gxs9rh.Xjfd7_4pAavc4VMNcFqMok61IuhuYzMinHofVs")
